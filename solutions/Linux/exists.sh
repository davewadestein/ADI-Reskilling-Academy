#!/bin/bash
# this script takes a command line argument
# and determines if that file exists

if test $# = 1; then # check to be sure we have ONE argument
    if test ! -f $1; then # check if file does not exist
        echo $1 does not exist!
    fi
else
    echo usage: $0 filename
fi
