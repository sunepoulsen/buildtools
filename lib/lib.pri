#====================================================================================
#			     Includes
#====================================================================================

include( default.pri )

#====================================================================================
#			     Qt Template
#====================================================================================

TEMPLATE = lib

win32 {
    CONFIG += dll
}

DESTDIR = $${PREFIX_LIB}

#====================================================================================
#			     Extra Rules
#====================================================================================

inst_headers.target = install_headers
unix: inst_headers.commands = $${INSTALL_TOOL} *.h $${PREFIX_INCLUDE}/
win32: inst_headers.commands = $${INSTALL_TOOL} *.h $${PREFIX_INCLUDE}\\
inst_headers.depends = $(DESTDIR)\$(TARGET)

inst_pro.target = install_pro
unix: inst_pro.commands = $${INSTALL_TOOL} $${PROJECT_ROOT}/$${PROJECT_NAME}.pri $${PREFIX_LIB}/
win32: inst_pro.commands = $${INSTALL_TOOL} $${PROJECT_ROOT}\\$${PROJECT_NAME}.pri $${PREFIX_LIB}\\
inst_pro.depends = $(DESTDIR)\$(TARGET)

ALL_DEPS += install_headers install_pro
QMAKE_EXTRA_TARGETS += inst_headers inst_pro

