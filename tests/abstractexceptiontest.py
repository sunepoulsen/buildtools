# ==============================================================================
#                      Imports
# ==============================================================================

import os

from unittest import TestCase

from abstractexception import AbstractException

# ==============================================================================
#                      Classes
# ==============================================================================

##
# \brief Unittest class of AbstractException
# 
class AbstractExceptionTest( TestCase ):
    def test_init( self ):
        self.assertRaises( TypeError, AbstractException )
        self.assertRaises( TypeError, AbstractException, "message", 2 )

        exp = AbstractException( "" )
        self.assertEqual( exp.getMessage(), "" )

        exp = AbstractException( "message" )
        self.assertEqual( exp.getMessage(), "message" )

    def test_raise( self ):
        try:
            raise AbstractException( "Message" )
        except AbstractException as exp:
            self.assertEqual( exp.getMessage(), "Message" )
