from sys import path as python_path
from os import path, makedirs

python_path.insert(0, path.abspath(
        path.join(path.dirname(__file__), path.pardir) ))

from docutils.core import publish_parts
from docutils_tinyhtml import Writer

def test_html_hyperlinks():
    """
Zeropage.cz_

.. _Zeropage.cz: http://zeropage.cz
    """
    writer = Writer()
    parts = publish_parts(source=test_html_hyperlinks.__doc__,
                           writer=writer,
                           writer_name='html')
    for k, v in parts.items():
        print "%s\t:(%d)\t%s" %(k, len(v), str(v)[:60].replace('\n', ' '))
    assert len(parts['html_hyperlinks']) > 0


def test_html_line():
    writer = Writer()
    parts = publish_parts(source=test_html_hyperlinks.__doc__,
                           writer=writer,
                           writer_name='html')
    for k, v in parts.items():
        print "%s\t:(%d)\t%s" %(k, len(v), str(v)[:60].replace('\n', ' '))
    assert len(parts['html_line']) > 0

def test_html_footnotes():
    """
Please RTFM [1]_.

.. [1] Read The Fine Manual
    """
    writer = Writer()
    parts = publish_parts(source=test_html_footnotes.__doc__,
                           writer=writer,
                           writer_name='html')
    for k, v in parts.items():
        print "%s\t:(%d)\t%s" %(k, len(v), str(v)[:60].replace('\n', ' '))
    assert len(parts['html_footnotes']) > 0


def test_html_citations():
    """
Here is a citation reference: [CIT2002]_.

.. [CIT2002] This is the citation.  It's just like a footnote,
   except the label is textual.
    """
    writer = Writer()
    parts = publish_parts(source=test_html_citations.__doc__,
                           writer=writer,
                           writer_name='html')
    for k, v in parts.items():
        print "%s\t:(%d)\t%s" %(k, len(v), str(v)[:60].replace('\n', ' '))
    assert len(parts['html_citations']) > 0


def test_title():
    """
Title
=====
some text
    """
    writer = Writer()
    parts = publish_parts(source=test_title.__doc__,
                           writer=writer,
                           writer_name='html')
    for k, v in parts.items():
        print "%s\t:(%d)\t%s" %(k, len(v), str(v)[:80].replace('\n', ' '))
    assert len(parts['html_title']) > 0

