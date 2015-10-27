#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup

__version__ = "1.1.0rc1"
__url__ = "https://github.com/ondratu/docutils-tinyhtmlwriter"


def doc():
    with open('README.rst', 'r') as readme:
        return readme.read().strip()

setup(
    name="distutils-tinyhtmlwriter",
    version=__version__,
    description="Docutils Writer producing Tiny HTML",
    author="Ondrej Tuma",
    author_email="mcbig@zeropage.cz",
    url=__url__,
    py_modules=['docutils_tinyhtml'],
    scripts=['rst2html-tiny'],
    license="BSD",
    long_description=doc(),
    classifiers=[
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
        "Topic :: Utilities"],
    requires=['docutils (>= 0.12)'],
    install_requires=['docutils >= 0.12']
)
