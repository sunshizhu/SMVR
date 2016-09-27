SMVR(Software defined Multi-Vendor service Rack)
========================

This is a command line application to help users to control and deploy software products of multiple vendors in a single sever. 

Ready to be realeased and distributed via setuptools/PyPI/pip for Python 2 and 3


Usage
-----


Behavior
--------


Installation sets up smvr command
**************************************

Situation before installation::

    $ smvr
    bash:smvr command not found

Installation right from the source tree (or via pip from PyPI)::

    $ python setup.py install

Now, the ``smvr`` command is available::

    $ smvr -w user_name
    Hello user_name !!


On Unix-like systems, the installation places a ``smvr`` script into a
centralized ``bin`` directory, which should be in your ``PATH``. On Windows,
``smvr.exe`` is placed into a centralized ``Scripts`` directory which
should also be in your ``PATH``.
