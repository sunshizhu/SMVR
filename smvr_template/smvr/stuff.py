# -*- coding: utf-8 -*-


"""bootstrap.stuff: stuff module within the bootstrap package."""

import logging
import argparse


class Stuff(object):
    pass



class OptParser(object):

    def __init__(self):
        desc = "Deploys a smvr environment"
        self._parser = argparse.ArgumentParser(description=desc)
        self._args = None
    
    def __getattr__(self, attr):
        if attr not in self.__dict__:
            if hasattr(self.args, attr):
                return getattr(self.args, attr)

        raise AttributeError("%r object has no attribute %r" %
                             (self.__class__, attr))
    def parse_args(self):
        self._args = self._parser.parse_args()


    @property
    def args(self):
        return self._args


    @property
    def parser(self):
        return self._parser





CONF = OptParser()
