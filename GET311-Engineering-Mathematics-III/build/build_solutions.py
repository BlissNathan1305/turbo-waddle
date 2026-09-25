"""Build GET311-Engineering-Mathematics-III-Solutions.docx with native Word equations.

Usage: python3 build/build_solutions.py [output.docx]

Needs pandoc (for example `pip install pypandoc_binary`). The Markdown sources use
LaTeX maths ($...$ and $$...$$); pandoc turns these into Word (OMML) equations
that can be edited with Word's built-in equation editor.
"""
import os, re, shutil, subprocess, sys, tempfile, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'GET311-Engineering-Mathematics-III-Solutions.docx')


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
    para('GET 311', 80, '1F3864', bold=True, before=3200, after=0)
    + para('Engineering Mathematics III', 48, '1F3864', bold=True, after=360)
    + '<w:p><w:pPr><w:pBdr><w:bottom w:val="single" w:sz="12" w:space="1" w:color="2E74B5"/></w:pBdr>'
      '<w:spacing w:after="360"/><w:ind w:left="2800" w:right="2800"/><w:jc w:val="center"/></w:pPr></w:p>'
    + para('Worked Solutions', 36, '2E74B5', after=120)
    + para('Application questions for the eight engineering departments', 24, '595959', after=2400)
    + para('3 Units  ·  Compulsory  ·  LH 45', 22, '595959', after=60)
    + para('128 questions  ·  8 topics  ·  8 departments', 22, '595959', after=0)
) + PAGE_BREAK

TOC = raw(
    '<w:p><w:pPr><w:pStyle w:val="TOCHeading"/></w:pPr><w:r><w:t>Contents</w:t></w:r></w:p>'
    '<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>'
    '<w:r><w:instrText xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText></w:r>'
    '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
    '<w:r><w:rPr><w:color w:val="7F7F7F"/></w:rPr><w:t>Right-click here and choose Update Field to show the table of contents.</w:t></w:r>'
    '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>'
) + PAGE_BREAK

ABOUT = """# How to Use These Solutions

Each solution sits under the question it answers, in the same order as the question set: eight topics, and within each topic the eight departments with two questions each.

::: {custom-style="Question Box"}
**Question.** The question is repeated in a blue box like this one.
:::

The working follows, step by step. All mathematics is set with Word's built-in equation editor, so any equation can be clicked and edited.

> **Answer.** The key results are collected in a green box like this one at the end of each solution.

Numerical answers were checked with a computer algebra system (SymPy). Where a question as written contains an inconsistency, the solution says so and shows the corrected working. Try each question yourself before reading its solution.
"""


def questions(path):
    """Map 'dept.q' -> question text from a topics file."""
    qs, dept = {}, None
    for line in open(path, encoding='utf-8'):
        m = re.match(r'^### (\d+)\.', line)
        if m:
            dept = m.group(1)
            continue
        m = re.match(r'^(\d)\. (.*)', line)
        if dept and m:
            qs[f'{dept}.{m.group(1)}'] = m.group(2).strip()
    return qs


def check_bars(name, text):
    """Bare | in maths shows as a logic symbol in some viewers; use \\left| ... \\right| or \\mid."""
    for m in re.finditer(r'\$\$(.+?)\$\$|\$(.+?)\$', text, re.S):
        body = m.group(1) or m.group(2)
        body = re.sub(r'\\(left|right)\\?\||\\\|', '', body)
        body = re.sub(r'\\begin\{array\}\{[^}]*\}', '', body)
        if '|' in body:
            sys.exit(f'{name}: bare | in maths: {body.strip()[:80]}')


def solutions_markdown():
    topics = sorted(os.listdir(os.path.join(ROOT, 'topics')))
    sols = sorted(os.listdir(os.path.join(ROOT, 'solutions')))
    parts = [TITLE_PAGE, TOC, ABOUT]
    for tfile, sfile in zip(topics, sols):
        qs = questions(os.path.join(ROOT, 'topics', tfile))
        for name in (os.path.join('topics', tfile), os.path.join('solutions', sfile)):
            check_bars(name, open(os.path.join(ROOT, name), encoding='utf-8').read())
        out, dept, used = [], None, 0
        for line in open(os.path.join(ROOT, 'solutions', sfile), encoding='utf-8'):
            out.append(line.rstrip('\n'))
            m = re.match(r'^## (\d+)\.', line)
            if m:
                dept = m.group(1)
            m = re.match(r'^### Question (\d):', line)
            if m:
                key = f'{dept}.{m.group(1)}'
                if key not in qs:
                    sys.exit(f'{sfile}: no question text for {key}')
                out += ['', '::: {custom-style="Question Box"}', f'**Question.** {qs[key]}', ':::', '']
                used += 1
        if used != len(qs):
            sys.exit(f'{sfile}: {used} solutions for {len(qs)} questions')
        parts += [PAGE_BREAK, '\n'.join(out)]
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
    subprocess.run([pandoc, src, '-f', 'markdown-auto_identifiers', '-o', OUT, '--reference-doc', ref,
                    '--metadata', 'title-meta=GET 311 Worked Solutions', '--metadata', 'lang=en-GB'], check=True)
    tidy(OUT)
    shutil.rmtree(work)
    print('wrote', OUT)


if __name__ == '__main__':
    main()
