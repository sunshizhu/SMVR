# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('smvr/smvr.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "smvr",
    packages = ["smvr"],
    entry_points = {
        "console_scripts": ['smvr = smvr.smvr:main']
        },
    version = version,
    description = "Python command line application help users control software products from multiple vendors.",
    long_description = long_descr,
    author = "Michael Shone",
    author_email = "shonemike1212@googlemail.com",
    url = "",
    )
