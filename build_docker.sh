#!/bin/sh
export PYTHONPATH=`pwd`

# gather version information from our codebase
PACKAGE_VERSION=`python -c 'import charactergen
print (charactergen.version)
'` 
echo Building version: $PACKAGE_VERSION

# build docker image now
docker build -t charactergen:$PACKAGE_VERSION .
