#!/bin/bash
# let's get in the habit of adding the above shebang

# Loop through all arguments, which are filenames.
# for each file
#   if it exists and is non-empty, append an "inspected by" line
#   if it exists and is empty, remove it
#   if it does not exist, print an error message
# if no args, print a usage/error line

if test $# = 0; then # no args passed
    echo "usage: $0 filename [filename...]"
    exit 1
fi

for file in $*; do # loop through all files
    if test -s $file; then # file exists and is non-empty
       echo 'Inspected by DWS' >> $file
    # if we get to the elif below, then it means either
    # 1) the file does not exist, or 2) it exsits and is empty
    elif test -e $file; then # file exists and is empty
	echo "Removing empty file: $file"
	rm -f "$file" # avoid $file having wildcards that are interpreted
    else
	echo $file does not exist
    fi
done
