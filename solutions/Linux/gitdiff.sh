title=

if test $# = 1; then
   title="for file $1"
fi

echo Working vs. Staging area $title
echo '(Changes that have not yet been staged.)'
git diff $1
echo
echo Staging vs. Repo $title
echo '(Changes than have been staged but not committed.)'
git diff --staged $1
