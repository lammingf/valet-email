# This script uses bogofilter to classify spam.
# Credit to: https://github.com/tminor/tmail

import subprocess
import notmuch
import sys
import os

# create notmuch database stuff
db = notmuch.Database(mode=1)
# we only care about new stuff
query = db.create_query('tag:new')
# path to binary
bogofilter = '/usr/bin/bogofilter'

# define object that we'll use to store a file path
# and bogofilter spam classification
class pOutput(object):
    path = ""
    mailType = ""

# function for creating objects out of
# bogofilter output
def processOutput(path, mailType):
    processed = pOutput()
    processed.path = path
    processed.mailType = mailType
    return processed

# define classification function
def isSpam(path):
    p = subprocess.run([bogofilter, "-BT", path], stdout=subprocess.PIPE)
    output = p.stdout.decode('ascii')
    output = output.split(" ")
    processed = processOutput(output[0], output[1])
    # output has to be decoded
    if processed.mailType == 'U' or processed.mailType == 'H':
        return False
    if processed.mailType == 'S':
        return True

# return all of the filenames that match the tag:new query
for msg in query.search_messages():
    for filepath in msg.get_filenames():
        if isSpam(filepath) == True:
            msg.remove_tag('new')
            msg.add_tag('spam')
            print("tagging spam " + str(msg))
        if isSpam(filepath) == False:
            msg.remove_tag('new')
            msg.add_tag('inbox')

sys.exit()
