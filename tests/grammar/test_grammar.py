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
import os
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
class TestUMLFigures(unittest.TestCase):
    """
    TestCase for UML 2.5 Behavior State Machine example figures.
    """
    def generic_test(self, figure_num):
        """
        Generic test method.

        Compiles the UML SM grammar, uses it to parse the text file containing
        the DSL definition of the state machine in the specified figure of the
        UML 2.5 specification, and then compares the JSON representation to
        that of the expected output.

        :param figure_num: String of the form 'X_Y' where X is the major figure
            number and Y is the minor figure number.
        """
        test_path = os.path.dirname(__file__)
        grammar_file = os.path.join(test_path,
            os.pardir, os.pardir, 'src', 'grammar', 'uml_sm.ebnf')
        figure_dsl_file = os.path.join(test_path, 'figure_'+figure_num+'.txt')
        expected_json_file = \
            os.path.join(test_path, 'figure_'+figure_num+'_expected.json')
        with open(grammar_file, 'r') as grammar_fp:
            grammar = grammar_fp.read()
        with open(figure_dsl_file, 'r') as stm_file:
            stm_desc = stm_file.read()
        with open(expected_json_file, 'r') as expected_json_fp:
            expected_json = json.load(expected_json_fp)

        # Compile the model and parse the UML figure.
        model = tatsu.compile(grammar, trace=False)
        test_ast = model.parse(stm_desc, trace=False, colorize=True)
        test_json = json.loads(tatsu.util.asjsons(test_ast))

        try:
            self.assertTrue(expected_json == test_json)
        except AssertionError, e:
            # For debugging purposes, write the test AST to a file on failure.
            failure_file = \
                os.path.join(test_path, 'figure_'+figure_num+'_failed.json')
            with open(failure_file, 'w') as failed_json_fp:
                failed_json_fp.write(test_json)
            self.fail(e)

    def test_figure_14_2(self):
        """
        TestCase for UML 2.5 Figure 14.2.
        """
        self.generic_test('14_2')

    def test_figure_14_7(self):
        """
        TestCase for UML 2.5 Figure 14.7.
        """
        self.generic_test('14_7')

    def test_figure_14_9(self):
        """
        TestCase for UML 2.5 Figure 14.9.
        """
        self.generic_test('14_9')

    def test_figure_14_10(self):
        """
        TestCase for UML 2.5 Figure 14.10.
        """
        self.generic_test('14_10')

    def test_figure_14_14(self):
        """
        TestCase for UML 2.5 Figure 14.14.
        """
        self.generic_test('14_14')

    def test_figure_14_23(self):
        """
        TestCase for UML 2.5 Figure 14.23.
        """
        self.generic_test('14_23')

    def test_figure_14_24(self):
        """
        TestCase for UML 2.5 Figure 14.24.
        """
        self.generic_test('14_24')

    def test_figure_14_36(self):
        """
        TestCase for UML 2.5 Figure 14.36.
        """
        self.generic_test('14_36')

if __name__ == "__main__":
    unittest.main()

##############################################################################
# End of file
##############################################################################
