"""Create the Word reference template (styles, page setup, footer) used by build_solutions.py."""
import os, re, shutil, subprocess, sys, tempfile, zipfile

NAVY, BLUE, GREY = '1F3864', '2E74B5', '404040'
PANDOC = sys.argv[1]
OUT = sys.argv[2]

def style(sid, name, kind='paragraph', based='Normal', nxt=None, ppr='', rpr='', extra=''):
    b = f'<w:basedOn w:val="{based}"/>' if based else ''
    n = f'<w:next w:val="{nxt}"/>' if nxt else ''
    return (f'<w:style w:type="{kind}" w:customStyle="1" w:styleId="{sid}"><w:name w:val="{name}"/>{b}{n}'
            f'<w:qFormat/>{extra}<w:pPr>{ppr}</w:pPr><w:rPr>{rpr}</w:rPr></w:style>') if kind == 'paragraph' else \
           (f'<w:style w:type="character" w:customStyle="1" w:styleId="{sid}"><w:name w:val="{name}"/>{b}<w:rPr>{rpr}</w:rPr></w:style>')

font = '<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="Calibri" w:cs="Calibri"/>'
box = lambda fill, line: (f'<w:pBdr><w:left w:val="single" w:sz="24" w:space="8" w:color="{line}"/></w:pBdr>'
                          f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>'
                          '<w:spacing w:before="80" w:after="160" w:line="276" w:lineRule="auto"/><w:ind w:left="220" w:right="220"/>')

styles = [
  '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/>'
  '<w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr>'
  f'<w:rPr>{font}<w:color w:val="1A1A1A"/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr></w:style>',
  style('BodyText', 'Body Text', nxt='BodyText'),
  style('FirstParagraph', 'First Paragraph', based='BodyText', nxt='BodyText'),
  style('Compact', 'Compact', based='BodyText', ppr='<w:spacing w:before="20" w:after="40"/>'),
  style('Title', 'Title', nxt='BodyText', ppr='<w:spacing w:before="0" w:after="120"/><w:jc w:val="center"/>',
        rpr=f'<w:b/><w:color w:val="{NAVY}"/><w:sz w:val="64"/><w:szCs w:val="64"/>'),
  style('Subtitle', 'Subtitle', nxt='BodyText', ppr='<w:spacing w:after="120"/><w:jc w:val="center"/>',
        rpr=f'<w:color w:val="{BLUE}"/><w:sz w:val="32"/><w:szCs w:val="32"/>'),
  style('Author', 'Author', nxt='BodyText', ppr='<w:jc w:val="center"/>', rpr=f'<w:color w:val="{GREY}"/><w:sz w:val="24"/>'),
  style('Date', 'Date', nxt='BodyText', ppr='<w:jc w:val="center"/>', rpr=f'<w:color w:val="{GREY}"/>'),
  style('Heading1', 'heading 1', nxt='BodyText',
        ppr=f'<w:keepNext/><w:keepLines/><w:pBdr><w:bottom w:val="single" w:sz="12" w:space="6" w:color="{BLUE}"/></w:pBdr>'
            '<w:spacing w:before="0" w:after="240"/><w:outlineLvl w:val="0"/>',
        rpr=f'<w:b/><w:color w:val="{NAVY}"/><w:sz w:val="36"/><w:szCs w:val="36"/>'),
  style('Heading2', 'heading 2', nxt='BodyText',
        ppr=f'<w:keepNext/><w:keepLines/><w:shd w:val="clear" w:color="auto" w:fill="{NAVY}"/>'
            '<w:spacing w:before="360" w:after="160"/><w:ind w:left="0"/><w:outlineLvl w:val="1"/>',
        rpr='<w:b/><w:color w:val="FFFFFF"/><w:sz w:val="26"/><w:szCs w:val="26"/>'),
  style('Heading3', 'heading 3', nxt='BodyText',
        ppr='<w:keepNext/><w:keepLines/><w:spacing w:before="240" w:after="80"/><w:outlineLvl w:val="2"/>',
        rpr=f'<w:b/><w:color w:val="{BLUE}"/><w:sz w:val="23"/><w:szCs w:val="23"/>'),
  style('Heading4', 'heading 4', nxt='BodyText',
        ppr='<w:keepNext/><w:spacing w:before="160" w:after="60"/><w:outlineLvl w:val="3"/>',
        rpr=f'<w:b/><w:color w:val="{GREY}"/>'),
  style('QuestionBox', 'Question Box', ppr=box('EEF3FA', BLUE), rpr=f'<w:color w:val="{NAVY}"/>'),
  style('BlockText', 'Block Text', nxt='BodyText', ppr=box('EAF5EC', '2E7D32'), rpr='<w:color w:val="1B4D20"/>'),
  style('SourceCode', 'Source Code', ppr='<w:shd w:val="clear" w:color="auto" w:fill="F4F4F4"/>'
        '<w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:left="220" w:right="220"/>',
        rpr='<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/><w:sz w:val="19"/>'),
  style('VerbatimChar', 'Verbatim Char', kind='character', based=None,
        rpr='<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/><w:sz w:val="20"/>'),
  style('TOCHeading', 'TOC Heading', based='Heading1', nxt='BodyText', ppr='<w:outlineLvl w:val="9"/>'),
  style('TOC1', 'toc 1', nxt='BodyText', ppr='<w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9016"/></w:tabs><w:spacing w:before="120" w:after="40"/>',
        rpr=f'<w:b/><w:color w:val="{NAVY}"/>'),
  style('TOC2', 'toc 2', nxt='BodyText', ppr='<w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9016"/></w:tabs><w:spacing w:after="20"/><w:ind w:left="360"/>'),
  style('Caption', 'Caption', ppr='<w:spacing w:after="120"/>', rpr='<w:i/>'),
  style('TableCaption', 'Table Caption', based='Caption'),
  style('Footer', 'footer', ppr='<w:jc w:val="center"/>', rpr='<w:color w:val="7F7F7F"/><w:sz w:val="18"/>'),
  style('FootnoteText', 'Footnote Text', rpr='<w:sz w:val="18"/>'),
  style('FootnoteReference', 'Footnote Reference', kind='character', based=None, rpr='<w:vertAlign w:val="superscript"/>'),
  style('Hyperlink', 'Hyperlink', kind='character', based=None, rpr=f'<w:color w:val="{BLUE}"/>'),
  '<w:style w:type="character" w:default="1" w:styleId="DefaultParagraphFont"><w:name w:val="Default Paragraph Font"/><w:uiPriority w:val="1"/><w:semiHidden/><w:unhideWhenUsed/></w:style>',
  # Tables: thin grey grid, light blue header row.
  '<w:style w:type="table" w:default="1" w:styleId="Table"><w:name w:val="Table"/>'
  '<w:pPr><w:spacing w:before="40" w:after="40"/><w:jc w:val="center"/></w:pPr>'
  '<w:tblPr><w:jc w:val="center"/><w:tblBorders>'
  + ''.join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>' for s in ('top','left','bottom','right','insideH','insideV')) +
  '</w:tblBorders><w:tblCellMar><w:top w:w="40" w:type="dxa"/><w:left w:w="120" w:type="dxa"/>'
  '<w:bottom w:w="40" w:type="dxa"/><w:right w:w="120" w:type="dxa"/></w:tblCellMar></w:tblPr>'
  f'<w:tblStylePr w:type="firstRow"><w:rPr><w:b/><w:color w:val="{NAVY}"/></w:rPr><w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="DCE6F2"/></w:tcPr></w:tblStylePr>'
  '</w:style>',
]

tmp = tempfile.mkdtemp()
ref = os.path.join(tmp, 'default.docx')
subprocess.run([PANDOC, '-o', ref, '--print-default-data-file', 'reference.docx'], check=True)
src = zipfile.ZipFile(ref)
files = {n: src.read(n) for n in src.namelist()}

st = files['word/styles.xml'].decode()
head = st[:st.index('<w:style ')]
head = re.sub(r'<w:sz w:val="24" />\s*<w:szCs w:val="24" />', '<w:sz w:val="22"/><w:szCs w:val="22"/>', head)
files['word/styles.xml'] = (head + ''.join(styles) + '</w:styles>').encode()

W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
files['word/footer1.xml'] = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:ftr {W}><w:p><w:pPr><w:pStyle w:val="Footer"/>'
    f'<w:pBdr><w:top w:val="single" w:sz="4" w:space="6" w:color="BFBFBF"/></w:pBdr></w:pPr>'
    '<w:r><w:t xml:space="preserve">GET 311: Engineering Mathematics III  ·  Worked Solutions  ·  Page </w:t></w:r>'
    '<w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
    '<w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>1</w:t></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r>'
    '</w:p></w:ftr>').encode()
rels = files['word/_rels/document.xml.rels'].decode()
files['word/_rels/document.xml.rels'] = rels.replace('</Relationships>',
    '<Relationship Id="rIdFooter1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/></Relationships>').encode()
ct = files['[Content_Types].xml'].decode()
files['[Content_Types].xml'] = ct.replace('</Types>',
    '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/></Types>').encode()
doc = files['word/document.xml'].decode()
doc = re.sub(r'<w:sectPr>.*?</w:sectPr>',
    '<w:sectPr><w:footerReference w:type="default" r:id="rIdFooter1"/><w:footnotePr><w:numRestart w:val="eachSect"/></w:footnotePr>'
    '<w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1300" w:right="1300" w:bottom="1300" w:left="1300" w:header="600" w:footer="600" w:gutter="0"/>'
    '<w:titlePg/></w:sectPr>', doc, flags=re.S)
files['word/document.xml'] = doc.encode()
settings = files['word/settings.xml'].decode()
files['word/settings.xml'] = settings.replace('<w:zoom w:percent="100" />', '<w:zoom w:percent="100" /><w:updateFields w:val="true"/>').encode()

with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    for n, d in files.items():
        z.writestr(n, d)
shutil.rmtree(tmp)
