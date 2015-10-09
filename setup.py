"""
Docutils Tiny HTML Writer is another docutils html writer, with very light html
output. It will create mainly for use in other project's like doc generators or
web publishers, which want to use their own html headers and footers.
"""

from distutils.core import setup
from distutils.command.build_scripts import build_scripts
from distutils.command.clean import clean
from distutils.dir_util import remove_tree
from distutils import log

from os import path
from shutil import copyfile

from docutils_tinyhtml import __version__, __url__

class X_build_scripts(build_scripts):
    def run(self):
        self.mkpath('build/_scripts_')
        copyfile('rst2html-tiny.py', 'build/_scripts_/rst2html-tiny')
        build_scripts.run(self)

class X_clean(clean):
    def run(self):
        for directory in ('build/_scripts_',):
            if path.exists(directory):
                remove_tree(directory, dry_run=self.dry_run)
            else:
                log.warn("'%s' does not exist -- can't clean it",
                            directory)
        clean.run(self)

setup(
    name                = "distutils-tinyhtmlwriter",
    version             = __version__,
    description         = "Docutils Writer producing Tiny HTML",
    author              = "Ondrej Tuma",
    author_email        = "mcbig@zeropage.cz",
    url                 = __url__,
    py_modules          = ['docutils_tinyhtml'],
    scripts             = ['build/_scripts_/rst2html-tiny'],
    license             = "BSD",
    long_description    = __doc__,
    classifiers         = [
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: End Users/Desktop",
            "License :: OSI Approved :: BSD License",
            "Natural Language :: English",
            "Natural Language :: Czech",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Topic :: Documentation",
            "Topic :: Software Development :: Documentation",
            "Topic :: Text Processing",
            "Topic :: Text Processing :: Markup",
            "Topic :: Utilities"
        ],
    requires            = ['docutils (>= 0.12)'],
    cmdclass            = {'build_scripts': X_build_scripts,
                           'clean': X_clean }
)
