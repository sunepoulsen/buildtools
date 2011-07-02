# ==============================================================================
#                      Imports
# ==============================================================================

from abstractaction import AbstractAction
import os
import io

# ==============================================================================
#                      Classes
# ==============================================================================

##
# \brief 
# 
class FileAction( AbstractAction ):
    ## \name Constructors
    ##@{
    READ_MODE = 'r'
    WRITE_MODE = 'w'
    APPEND_MODE = 'a'
    ##@}

    ## \name Constructors
    ##@{

    ##
    # \brief Constructs an abstract action
    # 
    def __init__( self, inputDevice = None, outputDevice = None, inputFile = None, outputFile = None, params = None ):
        self._inputDevice = inputDevice
        self._outputDevice = outputDevice
        self._inputFile = inputFile
        self._outputFile = outputFile
        
        self._params = dict()
        if params is not None:
            self._params = dict( params )        
    ##@}

    ## \name Properties
    ##@{
    def getInputDevice( self ):
        return self._inputDevice

    def setInputDevice( self, device ):
        self._inputDevice = device
        if self._inputDevice is not None:
            self._inputFile = None

    def getOutputDevice( self ):
        return self._outputDevice

    def setOutputDevice( self, device ):
        self._outputDevice = device
        if self._outputDevice is not None:
            self._outputFile = None

    def getParams( self ):
        return self._params

    def setParams( self, params ):
        self._params = params

    def getInputFile( self ):
        return self._inputFile

    def setInputFile( self, filename ):
        self._inputFile = filename
        if self._inputFile is not None:
            self_inputDevice = None

    def getOutputFile( self ):
        return self._outputFile

    def setOutputFile( self, filename ):
        self._outputFile = filename
        if self._outputFile is not None:
            self_outputDevice = None

    ##@}

    ## \name Helpers
    ##@{
    def createFilePath( self, filename ):
        path = os.path.split( os.path.dirname( os.path.realpath( filename ) ) )[0]
        if not os.path.exists( path ):
            os.makeDirs( path )
        

    def exchangeParams( self, bytes ):
        if len( self.getParams() ) == 0:
            return bytes

        s = bytes.replace( "@@", "@" )
        for key in iter( self.getParams() ):
            s = s.replace( "@" + key + "@", self.getParams()[ key ] )

        return s
    ##@}

    ## \name Interface
    ##@{

    def action( self, options = None ):
        if options is not None:
            self._params.update( { "PREFIX": options.getPrefix(),
                                   "VERSION": options.getVersion() } )

        inDevice = self.getInputDevice()
        if self.getInputFile() is not None:
            inDevice = io.FileIO( self.getInputFile(), self.READ_MODE )

        outDevice = self.getOutputDevice()
        if self.getOutputFile() is not None:
            self.createFilePath( self.getOutputFile() )
            outDevice = io.FileIO( self.getOutputFile(), self.WRITE_MODE )

        bytes = inDevice.read()
        if self.getInputFile() is not None:
            inDevice.close()

        outDevice.write( self.exchangeParams( bytes ) )
        outDevice.flush()
        if self.getOutputFile() is not None:
            outDevice.close()

    ##@}
