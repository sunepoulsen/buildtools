# ==============================================================================
#                      Imports
# ==============================================================================

import os

from unittest import TestCase

from abstractaction import AbstractAction
from abstractexception import AbstractException

# ==============================================================================
#                      Classes
# ==============================================================================

##
# \brief Unittest class of AbstractAction
# 
class AbstractActionTest( TestCase ):
    def test_action( self ):
        act = AbstractAction()
        self.assertRaises( AbstractException, act.action, None )
