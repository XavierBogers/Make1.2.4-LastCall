# script for network and port scanning

import socket

p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'pythonprogramming.net'

def scan(port):
    try:
        p.connect((server,port))
        return True
    except:
        return False


for i in range(1,512):
    if scan(i):
        print('Port',i,'is active')
    else:
        print('Port',i,'is inactive')