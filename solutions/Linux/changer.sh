#!/bin/bash

# Change all instances of Foo to Bar (or perhaps let caller specify)
# ...for each .txt file in the directory
# (Maybe let the user specify the directory to do this in)
#
# algorithm:
# for each file we want to modify
#   use sed to edit in place and create a backup
#   (that really does all the work for us, once we get the editing command right)
#   (it will make a backup by adding .bak to the entire filename)
#
# command-line args:
# we could specify the directory to do the work in on the command line
# or the old pattern and new pattern
# at this point we don't want to get too complex with command line options

dir=. # work in current directory unless told otherwise

if test $# -gt 1; then # are there any command line args?
    if test $1 = -d; then # -d = set directory to work in
        dir=$2
        shift 2 # discard (or "shift off") two command line args
    fi
fi

# change old_pattern to new_pattern; user may specify these
old_pattern=Foo
new_pattern=Bar

# at this point there may be no args left, if they were consumed above
if test $# -gt 1; then
    old_pattern=$1
    new_pattern=$2
fi

# move to the specific directory

cd $dir

for file in *.txt; do # or for file in *; if we want all files
    # use -i to edit file in place and created backup
    #sed -i.bak "s/$old_pattern/$new_pattern/g" $file 
    # if we want to limit the substitution to whole words, there are various
    # solutions outlined in StackOverflow and elsewhere. Unforunately, on a
    # Mac, it's much uglier than it is elsewhere...
    sed -i.bak "s/[[:<:]]$old_pattern[[:>:]]/$new_pattern/g" $file
    echo Processed $file and put backup into $file.bak
done
