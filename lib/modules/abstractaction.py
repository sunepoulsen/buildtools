# ==============================================================================
#                      Imports
# ==============================================================================

from abstractexception import AbstractException

# ==============================================================================
#                      Classes
# ==============================================================================

##
# \brief Declares an abstract action class.
#
# AbstractAction is the class of an action. An action is used to perform a given
# action doing the configuration of the source code or used in python scripts to
# be called from a makefile.
# 
class AbstractAction:
    ## \name Constructors
    ##@{

    ##
    # \brief Constructs an abstract action
    # 
    def __init__( self ):
        return
    ##@}

    ## \name Interface
    ##@{

    ##
    # \brief Executes the actions associated with this action.
    #
    # \param options An instance of ActionOptions.
    #
    def action( self, options = None ):
        raise AbstractException( "AbstractAction.action is abstract" )

    ##@}
