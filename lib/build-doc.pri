#====================================================================================
#			        Documentation Rules
#====================================================================================

build_api.target = build-api
unix: build_api.commands = $(MAKE) -C dist/doc/doxygen all
win32: build_api.commands = $(MAKE) -C dist\\doc\\doxygen all

QMAKE_EXTRA_TARGETS += build_api

