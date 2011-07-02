#!/usr/bin/env python

# ==============================================================================
#                      Imports
# ==============================================================================

import sys, os;
sys.path.append( os.path.join( os.path.split( os.path.dirname( os.path.realpath( sys.argv[0] ) ) )[0], "modules" ) )

import glob
import unittest

from abstractexceptiontest import AbstractExceptionTest
from abstractactiontest import AbstractActionTest
from actionoptionstest import ActionOptionsTest
from fileactiontest import FileActionTest
from copyactiontest import CopyActionTest

# ==============================================================================
#                      Functions
# ==============================================================================

def printEnvironment():
    for name, value in os.environ.iteritems():
        print( "%s ==> %s" % (name, value) )

def printFiles( wildcard ):
    print( "List of wildcard: %s" % wildcard )
    for filename in glob.glob( wildcard ):
        print( "\t%s" % filename )

def main( args ):
    suite = unittest.TestSuite()
    suite.addTest( unittest.TestLoader().loadTestsFromTestCase( AbstractExceptionTest ) )
    suite.addTest( unittest.TestLoader().loadTestsFromTestCase( AbstractActionTest ) )
    suite.addTest( unittest.TestLoader().loadTestsFromTestCase( ActionOptionsTest ) )
    suite.addTest( unittest.TestLoader().loadTestsFromTestCase( FileActionTest ) )
    suite.addTest( unittest.TestLoader().loadTestsFromTestCase( CopyActionTest ) )

    unittest.TextTestRunner( verbosity = 0 ).run( suite )

# ==============================================================================
#                      Executions
# ==============================================================================

if __name__ == '__main__' :
    main( sys.argv )
