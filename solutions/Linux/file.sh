#!/bin/bash

for file in $(ls -F); do
    # let's see if the file in question has a known extension
    echo -n $file': ' # no carriage return due to the -n
    case $file in
        *.txt) echo text file;;
	 *.py) echo Python language file;;
	*.bak) echo '"Backup"' file;;
	 *.sh) echo Bash script;;
           */) echo directory;;
           *@) echo symbolic link;;
            *) echo unknown file type;;
    esac
done
