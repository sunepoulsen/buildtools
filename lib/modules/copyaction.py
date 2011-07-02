# ==============================================================================
#                      Imports
# ==============================================================================

from abstractaction import AbstractAction
import os
import filecmp
import glob
import shutil

# ==============================================================================
#                      Classes
# ==============================================================================

##
# \brief 
# 
class CopyAction( AbstractAction ):
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
    def __init__( self, sources, dest ):
        self._sources = sources
        self._dest = dest
    ##@}

    ## \name Properties
    ##@{
    def getSources( self ):
        return self._sources

    def setSources( self, sources ):
        self._sources = sources

    def getDest( self ):
        return self._dest

    def setDest( self, dest ):
        self._dest = dest
    ##@}

    ## \name Helpers
    ##@{
    def makePath( self, path ):
        fullpath = os.path.realpath( path )
        if not os.path.exists( fullpath ):
            print( "Creating directory %s" % fullpath )
            os.makedirs( fullpath )

    def isChanged( self, src, dest ):
        if not os.path.exists( os.path.dirname( os.path.realpath( dest ) ) ):
            return True

        try:
            if filecmp.cmp( src, dest ):
                return False
        except:
            return True

        return True
        
    def copyFile( self, srcFileName, destFileName ):
        if not self.isChanged( srcFileName, destFileName ):
            return
        
        self.makePath( os.path.dirname( os.path.realpath( destFileName ) ) )

	print( "Copying file %s to %s" % ( srcFileName, destFileName ) )
	shutil.copyfile( srcFileName, destFileName )

    ##@}

    ## \name Interface
    ##@{

    def action( self, options = None ):
	for wildcard in self.getSources():
	    for filename in glob.glob( wildcard ):
                src = os.path.realpath( filename )
                dest = os.path.realpath( self.getDest() )

                if self.getDest()[-1] == os.sep:
                    dest += os.sep + os.path.split( src )[1]

                self.copyFile( src, dest )

    ##@}
