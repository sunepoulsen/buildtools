# ==============================================================================
#                      Imports
# ==============================================================================

from abstractexception import AbstractException

import os.path

# ==============================================================================
#                      Classes
# ==============================================================================

##
# \brief Declares an option class for actions.
# 
class ActionOptions:
    ## \name Constants
    ##@{
    PREFIX_PATH = "../installed"
    DEBUG_PREFIX = None
    RELEASE_PREFIX = None
    ##@}

    ## \name Constructors
    ##@{

    ##
    # \brief Constructs an abstract action
    # 
    def __init__( self, prefix = os.path.abspath( PREFIX_PATH ), version = "" ):
        self._prefix = prefix
        self._debugPrefix = ActionOptions.DEBUG_PREFIX 
        self._releasePrefix = ActionOptions.RELEASE_PREFIX
        self._version = version
    ##@}

    ## \name Properties
    ##@{

    ##
    # \brief 
    #
    def getPrefix( self ):
        return self._prefix

    ##
    # \brief 
    #
    # \param prefix 
    #
    def setPrefix( self, prefix ):
        self._prefix = prefix

    ##
    # \brief 
    #
    def getVersion( self ):
        return self._version

    ##
    # \brief 
    #
    # \param version 
    #
    def setVersion( self, version ):
        self._version = version

    ##@}
