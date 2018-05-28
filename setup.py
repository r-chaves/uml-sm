##############################################################################
# Module information
##############################################################################
"""Setup configuration file for JIRATimeTracker.
"""
##############################################################################
# __future__ Python imports (must be at start of file)
##############################################################################
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

##############################################################################
# Standard Python imports
##############################################################################
from setuptools import find_packages, setup

##############################################################################
# Local imports
##############################################################################
# None

##############################################################################
# Metadata
##############################################################################
# None

##############################################################################
# Global data
##############################################################################
PACKAGE_REQUIREMENTS = [
    'TatSu==4.2.6'
]

##############################################################################
# Code and classes
##############################################################################

setup(
    name='uml_sm',
    use_scm_version=True,
    description='UML State Machine something TODO',
    url='https://https://github.com/r-chaves/uml-sm',
    author='Ryan Chaves',
    author_email='ryan.chaves@gmail.com',
    license='MIT',
    # packages=find_packages('.'),
    packages=find_packages('src'),
    # package_dir={'':'src'},
    setup_requires=['setuptools_scm'],
    install_requires=PACKAGE_REQUIREMENTS,
    zip_safe=False
    )

##############################################################################
# End of file
##############################################################################
