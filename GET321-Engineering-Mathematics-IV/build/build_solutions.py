"""Build GET321-Theory-Marking-Scheme.docx (Questions 2-7, Types 1-5) with native Word equations.

Usage: python3 build/build_solutions.py [output.docx]

Needs pandoc (for example `pip install pypandoc_binary`). The Markdown sources in
theory-solutions/ use LaTeX maths ($...$ and $$...$$); pandoc turns these into Word (OMML)
equations that can be edited with Word's built-in equation editor. A line `!include name`
in a type file is replaced by theory-solutions/parts/name.md (a solution shared by several types).
"""
import os, re, shutil, subprocess, sys, tempfile, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC_DIR = os.path.join(ROOT, 'theory-solutions')
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'GET321-Theory-Marking-Scheme.docx')


def pandoc_path():
    try:
        import pypandoc
        return pypandoc.get_pandoc_path()
    except ImportError:
        return 'pandoc'


def raw(xml):
    return f'\n```{{=openxml}}\n{xml}\n```\n'


PAGE_BREAK = raw('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')


def para(text, size, color, bold=False, before=0, after=120):
    b = '<w:b/>' if bold else ''
    return (f'<w:p><w:pPr><w:spacing w:before="{before}" w:after="{after}"/><w:jc w:val="center"/></w:pPr>'
            f'<w:r><w:rPr>{b}<w:color w:val="{color}"/><w:sz w:val="{size}"/><w:szCs w:val="{size}"/></w:rPr>'
            f'<w:t xml:space="preserve">{text}</w:t></w:r></w:p>')


TITLE_PAGE = raw(
    para('GET 321', 80, '000000', bold=True, before=3200, after=0)
    + para('Engineering Mathematics IV', 48, '000000', bold=True, after=360)
    + '<w:p><w:pPr><w:pBdr><w:bottom w:val="single" w:sz="12" w:space="1" w:color="000000"/></w:pBdr>'
      '<w:spacing w:after="360"/><w:ind w:left="2800" w:right="2800"/><w:jc w:val="center"/></w:pPr></w:p>'
    + para('Marking Scheme for the Theory Questions', 36, '000000', after=120)
    + para('Questions 2 to 7  ·  Types 1 to 5', 28, '000000', after=2400)
    + para('2024/2025 &amp; 2025/2026 Second Semester B. Eng. Examination', 22, '000000', after=60)
    + para('September 2026', 22, '000000', after=0)
) + PAGE_BREAK

TOC = raw(
    '<w:p><w:pPr><w:pStyle w:val="TOCHeading"/></w:pPr><w:r><w:t>Contents</w:t></w:r></w:p>'
    '<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>'
    '<w:r><w:instrText xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText></w:r>'
    '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
    '<w:r><w:rPr><w:color w:val="000000"/></w:rPr><w:t>Right-click here and choose Update Field to show the table of contents.</w:t></w:r>'
    '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>'
) + PAGE_BREAK


def check_bars(name, text):
    """Bare | in maths shows as a logic symbol in some viewers; use \\left| ... \\right| or \\lvert."""
    for m in re.finditer(r'\$\$(.+?)\$\$|\$(.+?)\$', text, re.S):
        body = m.group(1) or m.group(2)
        body = re.sub(r'\\(left|right)\\?\||\\\||\\[lr]vert', '', body)
        if '|' in body:
            sys.exit(f'{name}: bare | in maths: {body.strip()[:80]}')


def expand(name):
    def include(m):
        part = os.path.join(SRC_DIR, 'parts', m.group(1) + '.md')
        if not os.path.exists(part):
            sys.exit(f'{name}: no part {m.group(1)}')
        return '\n' + open(part, encoding='utf-8').read().strip() + '\n\n'
    text = open(os.path.join(SRC_DIR, name), encoding='utf-8').read()
    return re.sub(r'^!include (\S+)\s*$', include, text, flags=re.M)


def solutions_markdown():
    parts = [TITLE_PAGE, TOC]
    for i in range(1, 6):
        name = f'type-{i}.md'
        text = expand(name)
        check_bars(name, text)
        found = re.findall(r'^## Question (\d):', text, re.M)
        if found != [str(n) for n in range(2, 8)]:
            sys.exit(f'{name}: expected Questions 2-7, found {found}')
        parts += [text if i == 1 else PAGE_BREAK + text]
    return '\n'.join(parts)


def tidy(path):
    """Fix two schema slips in pandoc's equation markup so the file validates.

    Text inside equations gets both m:nor and m:sty (the schema allows only one), and matrix
    column properties put m:mcJc before m:count (the schema wants m:count first).
    """
    tmp = path + '.tmp'
    with zipfile.ZipFile(path) as src, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as dst:
        for item in src.infolist():
            data = src.read(item.filename)
            if item.filename == 'word/document.xml':
                data = data.replace(b'<m:nor /><m:sty m:val="p" />', b'<m:nor />')
                data = re.sub(rb'(<m:mcJc [^>]*/>)(<m:count [^>]*/>)', rb'\2\1', data)
            dst.writestr(item, data)
    os.replace(tmp, path)


def main():
    work = tempfile.mkdtemp()
    ref = os.path.join(work, 'reference.docx')
    src = os.path.join(work, 'solutions.md')
    pandoc = pandoc_path()
    subprocess.run([sys.executable, os.path.join(HERE, 'make_reference.py'), pandoc, ref], check=True)
    with open(src, 'w', encoding='utf-8') as f:
        f.write(solutions_markdown())
    run = subprocess.run([pandoc, src, '-f', 'markdown-auto_identifiers', '-o', OUT, '--reference-doc', ref,
                          '--metadata', 'title-meta=GET 321 Theory Marking Scheme', '--metadata', 'lang=en-GB'],
                         capture_output=True, text=True)
    if run.returncode or 'WARNING' in run.stderr:
        sys.exit(run.stderr or f'pandoc failed ({run.returncode})')
    tidy(OUT)
    shutil.rmtree(work)
    print('wrote', OUT)


if __name__ == '__main__':
    main()
