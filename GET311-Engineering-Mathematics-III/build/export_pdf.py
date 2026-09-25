"""Export the solutions .docx to PDF with LibreOffice, filling in the table of contents first.

Usage: python3 build/export_pdf.py [input.docx] [output.pdf]

Needs LibreOffice (Writer and Math) and its Python bridge (python3-uno).
"""
import os, subprocess, sys, tempfile, time

import uno
from com.sun.star.beans import PropertyValue

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'GET311-Engineering-Mathematics-III-Solutions.docx'))
OUT = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(SRC)[0] + '.pdf')


def prop(name, value):
    p = PropertyValue()
    p.Name, p.Value = name, value
    return p


def main():
    profile = tempfile.mkdtemp()
    port = 2002 + os.getpid() % 1000
    office = subprocess.Popen(['soffice', '--headless', '--invisible', '--norestore',
                               f'-env:UserInstallation=file://{profile}',
                               f'--accept=socket,host=localhost,port={port};urp;'],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        resolver = uno.getComponentContext().ServiceManager.createInstanceWithContext(
            'com.sun.star.bridge.UnoUrlResolver', uno.getComponentContext())
        for _ in range(60):
            try:
                ctx = resolver.resolve(f'uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext')
                break
            except Exception:
                time.sleep(0.5)
        else:
            sys.exit('could not connect to LibreOffice')
        desktop = ctx.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop', ctx)
        doc = desktop.loadComponentFromURL(uno.systemPathToFileUrl(SRC), '_blank', 0, (prop('Hidden', True),))
        indexes = doc.getDocumentIndexes()
        for _ in range(2):  # the second pass picks up page numbers shifted by the first
            for i in range(indexes.getCount()):
                indexes.getByIndex(i).update()
            doc.refresh()
        doc.storeToURL(uno.systemPathToFileUrl(OUT), (prop('FilterName', 'writer_pdf_Export'),))
        doc.close(True)
        print('wrote', OUT)
    finally:
        office.terminate()
        office.wait()


if __name__ == '__main__':
    main()
