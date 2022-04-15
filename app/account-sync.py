from subprocess import Popen, PIPE, STDOUT
import glob, time

files = glob.glob("/conf/*.conf")
procs = []

for f in files:
    print('offlineimap -c '+ f)
    procs.append(Popen(['offlineimap', '-c', f], stderr=STDOUT))

#procs.append(Popen(['cd', '/maildir/frederick.lamming\@gmail/', '&&', 'gmi', 'sync'],
#    stderr=STDOUT))

for p in procs:
    print(p.communicate())

Popen(['notmuch', 'new'])
