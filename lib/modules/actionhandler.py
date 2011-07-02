# ==============================================================================
#                      Classes
# ==============================================================================

##
# \brief Implements a container of actions, to be executed.
#
class ActionHandler:
    ## \name Constructors
    ##@{

    ##
    # \brief Constructs a Scope instance.
    # 
    def __init__( self, actions = None ):
        self._actions = actions
    ##@}

    ## \name Properties
    ##@{

    ##
    # \brief Returns the list of actions.
    #
    def getActions( self ):
        return self._actions

    ##
    # \brief Sets the list of actions.
    #
    # \param actions A list of AbstractAction objects.
    #
    def setActions( self, actions ):
        self._actions = actions    
    ##@}

    ## \name Helpers
    ##@{
    
    ##
    # \brief Finds and returns the action with a given \e name.
    #
    # \param name The of the action to look for.
    #
    # \return
    #     Returns \e None if no action exists with the name \e name.
    #
    def find( self, name ):
        for act in self.getActions():
            if act.getName() == name:
                return act

        return None


    ##
    # \brief Executes each action with a set of options.
    #
    # \param options An instance of ActionOptions.
    #
    def execute( self, options = None ):
        for act in self.getActions():
            act.action( options )
    ##@}
