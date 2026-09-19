---
name: concept-normalizer
description: "Use when: a Markdown document contains concept links that should be rewritten as plain explanatory text and finished with a short 'Concetti' section listing the main concepts and their brief meaning."
---

# Concept normalizer for Microsoft Learn Azure content

## Goal

Keep the original Markdown content intact and preserve examples, code blocks, commands, and technical details. The only change should be a final section named `Concetti` that adds broader, useful context concepts not explicitly repeated in the body of the page.

This is especially useful for Microsoft Learn content, Azure service concepts, and certification-oriented study notes, where the main body should remain faithful to the source and the final summary acts as a conceptual bridge rather than a duplicate summary.

## When to use this skill

Use this when:
- a `.md` file contains references to Azure Learn concepts, service terms, or related topics
- you want to keep the original explanations and examples unchanged
- the file already contains the necessary technical detail and examples
- you need a short conceptual recap that adds missing context, not a verbatim summary
- the goal is to help revision without rewriting the document itself

## Workflow

1. Read the target Markdown file.
2. Identify the concept references that are scattered throughout the page, but do not treat the main terms as the only items to include.
3. Add a final `## Concetti` section containing concepts that are useful for understanding the topic more broadly, even if they are not restated in the body in the same wording.
   - Prefer adjacent concepts that help contextualize the topic.
   - Do not simply repeat the exact terms already explained in the page.
   - Keep the list short and selective.
4. Do not rewrite the core content. Preserve the original text, code examples, commands, and technical sections as they are.
5. Only add a final recap section at the end of the file.
6. In that section, list useful background ideas such as lifecycle, immutability, reuse, governance, or distribution, depending on the topic.
7. Keep each bullet brief and conceptual.
8. Check that the final page still reads like the original material, with one added recap section at the end.

## Quality checks

Before finishing, verify that:
- the body of the file is still intact and unchanged
- code blocks, examples, and commands were preserved
- the added `Concetti` section does not duplicate the exact main headings of the file
- the concepts are complementary to the article and improve understanding
- no deep synthesis or large rewrite was introduced

## Example output pattern

```md
## Address an artifact

...existing content remains unchanged...

## Concetti

- Immutability: a digest or exact version reference prevents ambiguity during deployment.
- Lifecycle management: images move from build to push to pull to deployment.
- Reuse optimization: common layers reduce duplication and improve efficiency.
- Governance: access control and naming discipline are essential in real registries.
```

## Example prompts

- "Mantieni il contenuto originale e aggiungi solo una sezione Concetti finale con i concetti principali del file."
- "Non riscrivere il documento: lascia esempi e comandi invariati e aggiungi alla fine una mini sintesi dei concetti."
- "Trasforma i riferimenti sparsi in una sezione Concetti senza toccare il resto del markdown."

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
