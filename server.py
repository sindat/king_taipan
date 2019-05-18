# compatibility between python 2 and python 3 with the print method
from __future__ import print_function

"""
##### IMPORTS #####
# os dependant functionality
import os
# python runtime related methods
import sys
import time
import json
# conversion from bytes to strings with base64 encoding
import base64
# saving stuff to disk, being able to then reference it in other python scripts
import pickle
import socket
# C structs support 
import struct
import random
# retrieve source code of a method, examine contents of a class, display detailed traceback
import inspect
# parser for command line options and arguments
import argparse
import datetime
# construct higher level threading interfaces
import threading
# spawn processes with run()
import subprocess
# specialized container datatypes
import collections
"""
# WEB SERVER MODULES
import http.server 
import socketserver

PORT = 6969
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer('127.0.0.1',PORT), Handler) as httpd:
    print("SERVER RUNNING AT PORT ", PORT)
    httpd.serve_forever()

# WEB SERVER SETUP
# FOR PYTHON 2.XX VERSIONS THEY USE THE SimpleHTTPServer MODULE
http_server = 'SimpleHTTPServer'
# IN PYTHON 3, WEB SERVER MODULE IS IMMPORTED AS THE http.server
if sys.version_info[0] > 2:
    http_server = 'http.server'
    # add serverModules and clientModules directories to PYTHONPATH
    sys.path.append('serverModules')
    sys.path.append('clientModules')

# SERVER MODULES IMPORT 
import serverModules.util as util
import serverModules.database as database
#import serverModules.security as security


# importing video processing package - cv2 (OpenCV)
try: 
    import cv2
except ImportError:
    util.log("MISSING PACKAGE: 'cv2' - REQUIRED BY 'webcam' MODULE")

# colored terminal text 
try: 
    import colorama
except ImportError:
    sys.exit("CRITICAL ERROR: PACKAGE 'colorama' IS REQUIRED")



###### MAIN FUNCTION ######
def main():
    parser = argparse.ArgumentParser(
        prog = 'server.py'
        description = "CC command line server"
    )
    # FILL ARGUMENT PARSER WITH INFORMATION
    parser.add_argument(
        '--host',
        action='store',
        type='str',
        default='127.0.0.1',
        help='Please enter your server hostname or IP address where server will run'
    )

    parser.add_argument(
        '--port',
        action='store',
        type='int',
        default=6969,
        help="Specify server listening port"
    )

    # SPECIFY DATABASE - LINKED TO THE DATABASE MODULE
    # I CAN LINK DIRECTLHY TO THE DATABASE BECAUSE IT'S REFERENCED IN THE PYTHONPATH AND MODULE IMPORT, IMPORTED AS "database"
    parser.add_argument(
        '--database',
        action='store',
        type='str',
        default='database.mainDB',
        help='the linked SQLite database'
    )

###### THE KEY CLASS ######
class CC():
    def __init__(self, host='127.0.0.1', port=6969):
        # server database attribute
        self._database = db
        # listening server socket bound to port 
        self.socket = self._socket(port)

