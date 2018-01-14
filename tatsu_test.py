"""Test of Tatsu.
$URL$
"""
##############################################################################
# __future__ Python imports (must be at start of file)
##############################################################################
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

##############################################################################
# Module information
##############################################################################
__copyright__   = "Ryan Chaves"
__version__     = "$Rev$"
__author__      = "$Author$"
__date__        = "$Date$"

##############################################################################
# Standard Python imports
##############################################################################
import sys
import pprint
import json

##############################################################################
# Local imports
##############################################################################
import tatsu
from tatsu.util import asjson

##############################################################################
# Global data
##############################################################################

##############################################################################
# Code and classes
##############################################################################

def main():
    """Main script function.
    """
    with open(sys.argv[1], 'r') as grammar_file:
        grammar = grammar_file.read()

    with open(sys.argv[2], 'r') as stm_file:
        stm_desc = stm_file.read()

    model = tatsu.compile(grammar, trace=False)
    ast = model.parse(stm_desc, trace=True, colorize=True)
    print('PPRINT')
    pprint.pprint(ast, indent=2, width=20)
    print()

    print('JSON')
    print(json.dumps(asjson(ast), indent=2))
    print()

if __name__ == "__main__":
    main()

##############################################################################
# End of file
##############################################################################
