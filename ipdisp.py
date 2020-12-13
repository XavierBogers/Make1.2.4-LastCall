#script for the display of IP addresses

import socket
import json
import logging
import re
import uuid

def getIPAddress():
    logging.basicConfig(filename='ipaddress.log', filemode='a', level=logging.INFO)
    try:
        ipinfo={}
        ipinfo['Local IP address']=socket.gethostbyname(socket.gethostname())
        ipinfo['Machine mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        return json.dumps(ipinfo)
    except Exception as n:
        logging.exception(n)


logging.info(getIPAddress())
print(getIPAddress())