import argparse
import json
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent
QUESTION_HEADING = re.compile(r"(?m)^###\s+(\d+)\.[ \t]*$")


def parse_assessment(path):
    text = path.read_text(encoding="utf-8-sig")
    headings = list(QUESTION_HEADING.finditer(text))
    questions = []
    errors = []

    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        block = text[heading.end():end]
        answer_match = re.search(r"(?m)^>\s*\[!answer\]-\s*Reveal answer\s*$", block)
        if not answer_match:
            errors.append(f"{path.relative_to(ROOT)}: domanda {heading.group(1)} senza risposta")
            continue

        before_answer = block[:answer_match.start()]
        option_matches = list(re.finditer(r"(?m)^([A-Z])\.\s*", before_answer))
        if not option_matches:
            errors.append(f"{path.relative_to(ROOT)}: domanda {heading.group(1)} senza opzioni")
            continue

        prompt = before_answer[:option_matches[0].start()].strip()
        options = []
        for option_index, option_match in enumerate(option_matches):
            option_end = option_matches[option_index + 1].start() if option_index + 1 < len(option_matches) else len(before_answer)
            option_text = before_answer[option_match.end():option_end].strip()
            option_text = re.sub(r"\n[ \t]*\n", "\n", option_text)
            options.append({"key": option_match.group(1), "text": option_text})

        answer_text = "\n".join(
            re.sub(r"^>\s?", "", line).strip()
            for line in block[answer_match.end():].splitlines()
            if line.lstrip().startswith(">")
        )
        correct_match = re.search(r"(?:^|\s)([A-Z])(?:\.|\s|$)", answer_text)
        option_keys = {option["key"] for option in options}
        if not correct_match or correct_match.group(1) not in option_keys:
            errors.append(f"{path.relative_to(ROOT)}: risposta non valida per domanda {heading.group(1)}")
            continue
        if len(prompt) == 0 or len(options) < 2:
            errors.append(f"{path.relative_to(ROOT)}: contenuto incompleto per domanda {heading.group(1)}")
            continue

        questions.append({
            "id": f"{path.relative_to(ROOT).as_posix()}::{heading.group(1)}",
            "learningPath": path.parent.parent.name,
            "module": path.parent.name,
            "number": int(heading.group(1)),
            "prompt": prompt,
            "options": options,
            "answer": correct_match.group(1),
        })

    return questions, errors


def load_question_bank():
    assessment_files = sorted(
        path for path in ROOT.rglob("*.md")
        if "assessment" in path.name.casefold()
    )
    questions = []
    errors = []
    for path in assessment_files:
        parsed, parse_errors = parse_assessment(path)
        questions.extend(parsed)
        errors.extend(parse_errors)
    return assessment_files, questions, errors


class QuizHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = urlparse(self.path).path
        if route == "/api/questions":
            assessment_files, questions, errors = load_question_bank()
            if errors:
                self.send_json(500, {"errors": errors})
                return
            self.send_json(200, {"assessmentCount": len(assessment_files), "questions": questions})
            return

        if route == "/" or route == "/index.html":
            page = ROOT / "quiz.html"
            if not page.exists():
                self.send_error(404, "quiz.html not found")
                return
            content = page.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return

        self.send_error(404)

    def send_json(self, status, payload):
        content = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, format, *args):
        pass


def main():
    parser = argparse.ArgumentParser(description="Local practice quiz for the AI-200 learning path assessments.")
    parser.add_argument("--check", action="store_true", help="validate all assessment questions without starting the server")
    parser.add_argument("--port", type=int, default=8000, help="local web server port (default: 8000)")
    args = parser.parse_args()

    assessment_files, questions, errors = load_question_bank()
    if args.check:
        print(f"Assessments: {len(assessment_files)}")
        print(f"Questions parsed: {len(questions)}")
        for error in errors:
            print(f"ERROR: {error}")
        return 1 if errors else 0
    if errors:
        parser.error("\n".join(errors))

    server = ThreadingHTTPServer(("127.0.0.1", args.port), QuizHandler)
    print(f"Quiz ready: http://127.0.0.1:{args.port}")
    print(f"Loaded {len(questions)} questions from {len(assessment_files)} assessments. Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nQuiz server stopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    raise SystemExit(main())