# ==============================================================================
#                      Imports
# ==============================================================================

import os

from unittest import TestCase

from actionoptions import ActionOptions

# ==============================================================================
#                      Classes
# ==============================================================================

##
# \brief Unittest class of AbstractAction
# 
class ActionOptionsTest( TestCase ):
    def test_init( self ):
        act = ActionOptions()
        self.assertEqual( act.getPrefix(), os.path.abspath( ActionOptions.PREFIX_PATH ) )
        self.assertEqual( act.getVersion(), "" )

        act = ActionOptions( "/tmp" )
        self.assertEqual( act.getPrefix(), "/tmp" )
        self.assertEqual( act.getVersion(), "" )
