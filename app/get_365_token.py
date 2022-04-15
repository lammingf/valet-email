import sys, os, subprocess
sys.path.append('./M365-IMAP')

import config

conf = os.path.join('./M365-IMAP', config.RefreshTokenFileName)

def get_token():
    return open(conf,'r').read()
