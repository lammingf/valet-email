#!/bin/bash

# Move a message file while removing its UID-part
function safeMove { s=${1##*/}; s=${s%%,*}; mv -f $1 $2/$s; }

# Copy a message file while removing its UID-part
function safeCopy { s=${1##*/}; s=${s%%,*}; cp -f $1 $2/$s; }

# Move all spam messages to the Spam folder
echo Moving $(notmuch count --output=files tag:spam AND NOT folder:Spam) \
     spam-marked messages to the Spam folder
for i in $(notmuch search --output=files tag:spam AND NOT folder:Spam); do
    safeMove $i ${MAILDIR}/Spam/cur
done

#echo Moving $(notmuch count --output=files tag:Family AND tag:to-me NOT tag:spam) \
#     ham-marked messages to the Ham folder
#for i in $(notmuch search --output=files tag:Family AND tag:to-me NOT tag:spam); do
#    safeCopy $i ${MAILDIR}/Ham/cur
#done
