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
import json
import unittest

##############################################################################
# Local imports
##############################################################################
import tatsu

##############################################################################
# Global data
##############################################################################
# None

##############################################################################
# Code and classes
##############################################################################

# pylint: disable=C0103
class TestUMLFigure14_24(unittest.TestCase):
    """
    TestCase for UML Figure 14.24.
    """
    def test_figure_14_24(self):
        """
        Test script for UML 2.5 Figure 14.24.

        Compiles the UML SM grammar, uses it to parse the text file containing
        the DSL definition of the state machine in Figure 14.24 of the UML 2.5
        specification, and then compares the JSON representation to that of
        the expected output.
        """
        with open('uml_sm.ebnf', 'r') as grammar_file:
            grammar = grammar_file.read()
        with open('figure_14_24.txt', 'r') as stm_file:
            stm_desc = stm_file.read()
        with open('figure_14_24_expected.json', 'r') as expected_json_fp:
            expected_json = json.load(expected_json_fp)

        # Compile the model and parse the UML figure.
        model = tatsu.compile(grammar, trace=False)
        test_ast = model.parse(stm_desc, trace=False, colorize=True)
        test_json = json.loads(tatsu.util.asjsons(test_ast))

        # See if we got the expected result.
        try:
            self.assertTrue(expected_json == test_json)
        except AssertionError, e:
            # For debugging purposes, write the test AST to a file on failure.
            with open('figure_14_24_failed.json', 'w') as failed_json_fp:
                failed_json_fp.write(test_json)
            self.fail(e)

if __name__ == "__main__":
    unittest.main()

##############################################################################
# End of file
##############################################################################
