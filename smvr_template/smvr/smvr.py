# -*- coding: utf-8 -*-


"""smvr.smvr: provides entry point main()."""


__version__ = "0.1.0"


import sys
import logging
from .stuff import Stuff


logging.basicConfig(
    filename='smvr.log',
    level=logging.DEBUG,
    format=('%(asctime)s %(levelname)s '
            '(%(funcName)s) %(message)s'))

log = logging.getLogger('smvr_cmd')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)


from .stuff import CONF as cfg


def main():
    
    cfg.parser.add_argument('-w', '--welcome', dest='user_name', 
                    help='welcome !!', type=str)
    
    cfg.parser.add_argument('-s', action='store', dest='simple_value',
                    help='Store a simple value')

    cfg.parser.add_argument('-c', action='store_const', dest='constant_value',
                    const='value-to-store',
                    help='Store a constant value')

    cfg.parser.add_argument('-t', action='store_true', default=False,
                    dest='boolean_switch',
                    help='Set a switch to true')

    cfg.parser.add_argument('-f', action='store_false', default=False,
                    dest='boolean_switch',
                    help='Set a switch to false')

    cfg.parser.add_argument('-a', action='append', dest='collection',
                    default=[],
                    help='Add repeated values to a list',
                    )

    cfg.parser.add_argument('-A', action='append_const', dest='const_collection',
                    const='value-1-to-append',
                    default=[],
                    help='Add different values to list')

    cfg.parser.add_argument('-B', action='append_const', dest='const_collection',
                    const='value-2-to-append',
                    help='Add different values to list')

    cfg.parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    cfg.parser.add_argument('-d', '--demo', action='store_true')

    cfg.parse_args()

    log.debug("Starting SMVR deployer")

    if cfg.demo: 
        print ('simple_value     ={}'.format(cfg.simple_value))
        print ('constant_value   ={}'.format(cfg.constant_value))
        print ('boolean_switch   ={}'.format(cfg.boolean_switch))
        print ('collection       ={}'.format(cfg.collection))
        print ('const_collection ={}'.format(cfg.const_collection))
        log.info("Show some command line functions")
    if cfg.user_name:
        print ('Hello {} !!'.format(cfg.user_name))
        log.info("say hello to end user")



