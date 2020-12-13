# script for system update

import os

passw = input('Please enter your password')
update = 'apt-get-update'
upgrade = 'apt-get-upgrade'
os.system('echo %s|sudo -S %s' % (passw, update))
os.system('echo %s|sudo -S %s' % (passw, upgrade))