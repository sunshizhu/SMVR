SMVR(Software defined Multi-Vendor service Rack)
========================

This is a command line application to help users to control and deploy software products of multiple vendors in a single sever. 

Ready to be realeased and distributed via setuptools/PyPI/pip for Python 2 and 3


Usage
-----


Behavior
--------


Installation sets up bootstrap command
**************************************

Situation before installation::

    $ smvr
    bash:smvr command not found

Installation right from the source tree (or via pip from PyPI)::

    $ python setup.py install

Now, the ``smvr`` command is available::

    $ smvr arg1 arg2
    Executing bootstrap version 0.2.0.
    List of argument strings: ['arg1', 'arg2']
    Stuff and Boo():
    <class 'bootstrap.stuff.Stuff'>
    <bootstrap.bootstrap.Boo object at 0x7f366749a190>


On Unix-like systems, the installation places a ``smvr`` script into a
centralized ``bin`` directory, which should be in your ``PATH``. On Windows,
``smvr.exe`` is placed into a centralized ``Scripts`` directory which
should also be in your ``PATH``.
