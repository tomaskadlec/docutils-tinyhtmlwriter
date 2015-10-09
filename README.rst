Docutils Tiny HTML Writer
-------------------------
Docutils Tiny HTML Writer is another docutils html writer, with very light html
output. It will create mainly for use in other project's like doc generators or
web publishers, which want to use their own html headers and footers.

One of possible use:

.. code-block:: python
    :name: example

    from docutils.core import publish_string
    from docutils_tinyhtml import Writer

    if sys.version_info[0] < 3:
        from io import open

    writer = Writer()
    with open("README.rst", encoding="utf-8") as f:
        rst = f.read()

    # store full html output to html variable
    html = publish_string(source=rst,
                          parser_name='restructuredtext',
                          writer=Writer(),
                          writer_name='html',
                          settings_overrides={'link': 'link', 'top': 'top'})

    # store only html body
    body = writer.generate_body()

Installation
------------

.. code-block:: sh

    $ pip install docutils-tinyhtmlwriter
