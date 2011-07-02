# ==============================================================================
#                      Imports
# ==============================================================================

import argparse
import os.path

from actionoptions import ActionOptions
from actionhandler import ActionHandler
from fileaction import FileAction

# ==============================================================================
#                      Classes
# ==============================================================================

##
# \brief 
#
class AutogenFactory:
    ## \name Constants
    ##@{
    ARG_PREFIX = '--prefix'
    ARG_PREFIX_HELP = 'Sets the prefix directory of bin, include and lib directories.'
    ##@}

    ## \name Constructors
    ##@{

    ##
    # \brief Constructs an abstract action
    # 
    def __init__( self, description, version, actions = [] ):
        self._description = description
        self._version = version
        self._actions = actions
    ##@}

    def getActions( self ):
        return self._actions

    def setActions( self, actions ):
        self._actions = actions

    def appendAction( self, action ):
        self._actions.append( action )

    def newFileAction( self, inFile, outFile, params = None ):
        act = FileAction( inputFile = inFile, outputFile = outFile )
        if params is not None:
            act.setParams( params )

        return act

    def newUseLibAction( self, inFile, outFile, libname, qtmodules ):
        params = dict( { "QTMODULES": qtmodules, "LIBNAME": libname } )

        return self.newFileAction( inFile, outFile, params )

    ##
    # \brief 
    #
    # \param args Arguments from the command line.
    #
    def main( self, args ):
        parser = argparse.ArgumentParser( description = self._description )
        parser.add_argument( '--prefix', default = ActionOptions.PREFIX_PATH )
        parser.add_argument( '-v', '--version', action='version', version = self._version )

        params = parser.parse_args( args[1:] )    

        options = ActionOptions( os.path.realpath( params.prefix ), self._version )

        handler = ActionHandler( self._actions )
        handler.execute( options )
        
        return 0
