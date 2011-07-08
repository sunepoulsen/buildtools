#!/usr/bin/env python

# =========================================================================================
#                       Imports
# =========================================================================================

import os
import sys
import argparse

## Magic to add lib/modules to search path
sys.path.append( os.path.join( os.path.split( os.path.dirname( os.path.realpath( sys.argv[0] ) ) )[0], "lib/modules" ) )

from copyaction import CopyAction

# =========================================================================================
#                       Main function
# =========================================================================================

def main( args ):    
    parser = argparse.ArgumentParser( description = 'Install tool to install files from one location to another.' )
    parser.add_argument( 'src', nargs='+' )
    parser.add_argument( 'dest' )

    params = parser.parse_args( args[1:] )    

    act = CopyAction( params.src, params.dest  )
    act.action()

    return 0

# =========================================================================================
#                       Execution
# =========================================================================================

main( sys.argv )

