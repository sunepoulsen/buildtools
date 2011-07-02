#====================================================================================
#			     Checks
#====================================================================================

isEmpty( PROJECT_ROOT ): error( "Variable PROJECT_ROOT must be set before include." )
isEmpty( PROJECT_NAME ): error( "Variable PROJECT_NAME must be set before include." )

#====================================================================================
#			     Paths & Variables
#====================================================================================

PYTHON_BIN = python

TOOLS_BIN = $${PWD}/tools/bin
INSTALL_TOOL = $${PYTHON_BIN} $${TOOLS_BIN}/install.py

#====================================================================================
#			     Qt Template
#====================================================================================

CONFIG += qt warn_on thread debug_and_release

win32 {
    CONFIG += windows
}

#====================================================================================
#			     Distribution Options
#====================================================================================

isEmpty( PREFIX ) {
    unix: PREFIX = $${PROJECT_ROOT}/../Installed
    win32: PREFIX = $${PROJECT_ROOT}\\..\\Installed
}

isEmpty( PREFIX_BIN ) {
    unix: PREFIX_BIN = $${PREFIX}/bin
    win32: PREFIX_BIN = $${PREFIX}\\Bin
}

isEmpty( PREFIX_INCLUDE ) {
    unix: PREFIX_INCLUDE = $${PREFIX}/include
    win32: PREFIX_INCLUDE = $${PREFIX}\\Include
}
        
isEmpty( PREFIX_LIB ) {
    unix: PREFIX_LIB = $${PREFIX}/lib
    win32: PREFIX_LIB = $${PREFIX}\\Lib
}

isEmpty( $${TARGET} ) {
    TARGET = $${PROJECT_NAME}
    CONFIG(debug, debug|release) {
        TARGET = $${TARGET}d
    }
}

#====================================================================================
#			     Compiler Options
#====================================================================================

CONFIG(debug, debug|release) {
    DEFINES += DEBUG
}

win32 {
    DEFINES += WIN32
}
