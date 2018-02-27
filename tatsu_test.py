"""
Test application using Tatsu.

This application uses Tatsu to compile an input grammer into a model and then
parse a file that (hopefully) obeys that grammar.

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
# None

##############################################################################
# Standard Python imports
##############################################################################
import sys
import tatsu

##############################################################################
# Local imports
##############################################################################
# None

##############################################################################
# Global data
##############################################################################
# None

##############################################################################
# Code and classes
##############################################################################

def main():
    """
    Main script function.
    """
    with open(sys.argv[1], 'r') as grammar_file:
        grammar = grammar_file.read()

    with open(sys.argv[2], 'r') as stm_file:
        stm_desc = stm_file.read()

    model = tatsu.compile(grammar, trace=False)
    ast = model.parse(stm_desc, trace=False, colorize=True)
    print(tatsu.util.asjsons(ast))

if __name__ == "__main__":
    main()

##############################################################################
# End of file
##############################################################################
