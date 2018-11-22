#/usr/bin/env bash -e
#
# Auto-generate python virtual environments and install requirements.
#
# Usage
#	./setup.sh XXX
# 
# where XXX can be:
# - google
# - ibm
# - wit
# - fuetrek

NAME=$1
VENV=venv

# check that argument has been supplied
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1
fi

FULLPATH="$VENV/$1"

# if path does not exist, generate a new virtual environment
if [ ! -d "$FULLPATH" ]
then

    PYTHON=`which python2`

    if [ ! -f $PYTHON ]
    then
        echo "Could not find Python"
    fi
    virtualenv -p $PYTHON $FULLPATH

fi

# activate the virtual environment
. $FULLPATH/bin/activate

# install requirements
pip install -r requirements/$1.txt
