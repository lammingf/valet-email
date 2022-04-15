#!/bin/bash

FILES="/conf/*.conf"

for f in $FILES
do
  echo "Processing $f file..."
  offlineimap -c $f &
done

(cd /maildir/frederick.lamming\@gmail/ && gmi sync) &

wait < <(jobs -p)

notmuch new
