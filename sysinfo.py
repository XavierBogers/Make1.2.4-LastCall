# script to display system info

# library import to extract multiple system properties from the current host system

import platform
import socket
import re
import uuid
import json
import psutil
import logging

# function to extract all the required system data

def getMachineInfo():
    logging.basicConfig(filename='systeminfo.log', filemode='a', level=logging.INFO)
    # information will be logged to the systeminfo.log file
    try:
        info={}
        info['OS']=platform.system()
        info['OS-release']=platform.release()
        info['OS-version']=platform.version()
        info['OS-architecture']=platform.machine()
        info['Machine hostname']=socket.gethostname()
        info['Machine ip-address']=socket.gethostbyname(socket.gethostname())
        info['Machine mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['Processor']=platform.processor()
        info['RAM']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

# logging the information to the specified file

logging.info(getMachineInfo())

# print the requested data

print(getMachineInfo())
