# ==============================================================================
#                      Imports
# ==============================================================================

import os
import io

from unittest import TestCase
from fileaction import FileAction
from actionoptions import ActionOptions

# ==============================================================================
#                      Classes
# ==============================================================================

##
# \brief Unittest class of FileAction
# 
class FileActionTest( TestCase ):
    def test_init( self ):
        act = FileAction()

    def test_params( self ):
        act = FileAction()
        self.assertEqual( len( act.getParams() ), 0 )

        act.setParams( dict( {"k1": "v1", "k2": "v2" } ) )
        self.assertEqual( len( act.getParams() ), 2 )
        self.assertTrue( "k1" in act.getParams() )
        self.assertTrue( "k2" in act.getParams() )
        self.assertTrue( "forkert" not in act.getParams() )

    def test_exchangeParams( self ):
        act = FileAction()
        self.assertEqual( act.exchangeParams( "" ), "" )
        self.assertEqual( act.exchangeParams( "mit navn" ), "mit navn" )
        self.assertEqual( act.exchangeParams( "PREFIX = @PREFIX@" ), "PREFIX = @PREFIX@" )

        act.setParams( dict( { "PREFIX": "/usr" } ) )
        self.assertEqual( len( act.getParams() ), 1 )
        self.assertTrue( "PREFIX" in act.getParams() )
        self.assertEqual( act.getParams()[ "PREFIX" ], "/usr" )

        self.assertEqual( act.exchangeParams( "" ), "" )
        self.assertEqual( act.exchangeParams( "mit navn" ), "mit navn" )
        self.assertEqual( act.exchangeParams( "PREFIX = @PREFIX@" ), "PREFIX = /usr" )
        self.assertEqual( act.exchangeParams( "PREFIX = @PREFIX@@@" ), "PREFIX = /usr@" )
        self.assertEqual( act.exchangeParams( "PREFIX = @PREFIX" ), "PREFIX = @PREFIX" )
        self.assertEqual( act.exchangeParams( "PREFIX = PREFIX@" ), "PREFIX = PREFIX@" )
        self.assertEqual( act.exchangeParams( "PREFIX = @PREFIX PREFIX = @PREFIX@ PREFIX = PREFIX@" ), 
                          "PREFIX = @PREFIX PREFIX = /usr PREFIX = PREFIX@" )

    def test_stringDevices( self ):
        options = ActionOptions()

        inText = ""
        outText = inText

        outDev = io.StringIO()
        act = FileAction( inputDevice = io.StringIO( inText ), outputDevice = outDev )
        act.action( options )
        self.assertEqual( outDev.getvalue(), outText )

        inText = "mit navn"
        outText = inText

        outDev = io.StringIO()
        act = FileAction( inputDevice = io.StringIO( inText ), outputDevice = outDev )
        act.action( options )
        self.assertEqual( outDev.getvalue(), outText )

        inText = "@PREFIX@"
        outText = inText.replace( "@PREFIX@", options.getPrefix() )

        outDev = io.StringIO()
        act = FileAction( inputDevice = io.StringIO( inText ), outputDevice = outDev )
        act.action( options )
        self.assertEqual( outDev.getvalue(), outText )

    def test_fileDevices( self ):
        options = ActionOptions()

        inText = "@PREFIX@"
        outText = inText.replace( "@PREFIX@", options.getPrefix() )

        act = FileAction( inputDevice = io.StringIO( inText ), outputFile = "test_fileDevices.txt" )
        act.action( options )
        
        outFile = io.FileIO( "test_fileDevices.txt" )
        self.assertEqual( outFile.read(), outText )
        outFile.close()
