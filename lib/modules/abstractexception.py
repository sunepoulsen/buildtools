# ==============================================================================
#                      Classes
# ==============================================================================

##
# \brief Declares an exception to be throwed then calling abstract functions or 
# classes.
#
# 
class AbstractException( Exception ):
    ## \name Constructors
    ##@{

    ##
    # \brief Constructs a Scope instance.
    # 

    def __init__( self, message ):
        self._message = message

    def __str__( self ):
        return self._message

    def getMessage( self ):
        return self._message
        
    ##@}

