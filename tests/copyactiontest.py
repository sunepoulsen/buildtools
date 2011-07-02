# ==============================================================================
#                      Imports
# ==============================================================================

import os
import io

from unittest import TestCase
from copyaction import CopyAction

# ==============================================================================
#                      Classes
# ==============================================================================

##
# \brief Unittest class of CopyAction
# 
class CopyActionTest( TestCase ):
    def test_init( self ):
        act = CopyAction( [ '*.py' ], "/" )
        self.assertEqual( act.getSources(), [ '*.py' ] )
        self.assertEqual( act.getDest(), "/" )

    def test_action( self ):
        self.assertTrue( "data/tmp/"[-1] == os.sep )

        act = CopyAction( [ "data/*.txt" ], "data/tmp/" )
        act.action()
        self.assertFalse( act.isChanged( "data/test_fileDevices.txt", "data/tmp/test_fileDevices.txt" ) )

        act = CopyAction( [ "data/tmp/*.txt" ], "data/tmp/tmp.txt" )
        act.action()
        self.assertFalse( act.isChanged( "data/tmp/test_fileDevices.txt", "data/tmp/tmp.txt" ) )
        
