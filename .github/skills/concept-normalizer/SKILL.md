---
name: concept-normalizer
description: "Use when: a Markdown document contains external Learn references or related concept links that should be normalized into a final 'Concepts' section, with brief online mentions and direct local links to project files when available."
---

# Concept normalizer for Microsoft Learn Azure content

## Goal

Keep the original Markdown content intact and preserve examples, code blocks, commands, and technical details. The only change should be a final section named `Concepts` that gathers related references and useful background context without rewriting the article itself.

This is especially useful for Microsoft Learn content, Azure service concepts, and certification-oriented study notes, where the main body should remain faithful to the source and the final section acts as a lightweight conceptual bridge rather than a duplicate summary.

## When to use this skill

Use this when:
- a `.md` file contains references to Azure Learn concepts, service terms, or related topics
- you want to keep the original explanations and examples unchanged
- the file already contains the necessary technical detail and examples
- you need a short conceptual recap that adds missing context, not a verbatim summary
- the goal is to help revision without rewriting the document itself

## Workflow

1. Read the target Markdown file.
2. Identify references to external online resources and adjacent concepts scattered through the page.
3. Add a final `## Concepts` section containing only short, direct concept entries.
   - Each bullet should be a concept label followed by a brief explanatory phrase, not a generic list of unrelated references.
   - For any external online reference, keep it to a micro mention inside the same bullet: short and contextual, never a full explanation or a second article.
   - If there is a matching local note in the project, include the link directly in the same bullet as part of the concept entry, in the form `Concept: [local note](...)`.
   - Do not create a separate “Related notes” list or a separate “Local project note” block.
   - Prefer adjacent concepts that help contextualize the topic without repeating the exact headings already in the page.
4. Do not rewrite the core content. Preserve the original text, code examples, commands, and technical sections as they are.
5. Only add a final concept section at the end of the file.
6. In that section, list useful background ideas such as lifecycle, immutability, reuse, governance, dependency tracking, or distribution, depending on the topic.
7. Keep each bullet brief and conceptual.
8. Check that the final page still reads like the original material, with one added section at the end and no deep synthesis.

## Quality checks

Before finishing, verify that:
- the body of the file is still intact and unchanged
- code blocks, examples, and commands were preserved
- the added `Concepts` section does not duplicate the exact main headings of the file
- external online references are only lightly mentioned, not expanded into a second article
- local project files are linked directly when available, instead of being described in prose
- the concepts are complementary to the article and improve understanding
- no deep synthesis or large rewrite was introduced

## Example output pattern

```md
## Address an artifact

...existing content remains unchanged...

## Concepts

- Dependency tracking: a registry can react to base image updates and trigger rebuilds of downstream artifacts.
- Image lifecycle: images move from build to push to pull to deployment, and the same pattern is often represented across registry workflows. See [Additional Resources/About registries, repositories, and artifacts.md](../../Additional%20Resources/About%20registries,%20repositories,%20and%20artifacts.md).
- Governance: access control and naming discipline are essential in real registries.
```

## Example prompts

- "Mantieni il contenuto originale e aggiungi solo una sezione final Concepts con micro-rimandi ai riferimenti esterni e link locali quando disponibili."
- "Non riscrivere il documento: lascia esempi e comandi invariati e aggiungi in fondo una sezione Concepts con riferimenti leggeri e link locali."
- "Trasforma i riferimenti sparsi in una sezione Concepts senza toccare il resto del markdown, usando solo accenni brevi per risorse online e link diretti per file locali."

## Azure-specific notes

This variant is meant for:
- Azure Learn modules
- Microsoft certification study material
- service concepts and terminology
- course notes that should stay faithful to the original technical explanation

## Related customizations

- a version focused only on keeping examples and code blocks untouched
- a version optimized for course recap sections
- a version specialized for Azure service terminology review
