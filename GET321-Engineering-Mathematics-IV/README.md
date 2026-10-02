# GET 321: Engineering Mathematics IV

## Question One (objective)

- `Type 1.docx` to `Type 5.docx`: the five versions of the Question One paper, with the correct option in each question set in bold.
- `Unmarked/`: the same papers without the answers marked.

## Theory Questions 2 to 7

Worked solutions to Questions 2 to 7 for all five types are in [GET321-Theory-Solutions.pdf](GET321-Theory-Solutions.pdf) and in an editable Word file, [GET321-Theory-Solutions.docx](GET321-Theory-Solutions.docx). Each type starts on a new page and follows that paper's question order. Every equation is a native Word equation, so it can be edited with Word's built-in equation editor. The "Notes for the Examiner" page lists the misprints found in the papers and how the solutions handle them.

The sources are in [`theory-solutions/`](theory-solutions/): one Markdown file per type, plus `parts/` for solutions shared by several types (pulled in with `!include name`). To rebuild:

```
pip install pypandoc_binary
python3 build/build_solutions.py   # Word document
python3 build/export_pdf.py        # PDF, needs LibreOffice Writer and Math and python3-uno
```
