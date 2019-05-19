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
# PARSER FOR COMMAND LINE ARGUMENTS 
import argparse

"""
PORT = 6969
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("127.0.0.1",PORT), Handler) as httpd:
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

"""

# SERVER MODULES IMPORT 

"""
import serverModules.util as util
import serverModules.database as database
"""
#import serverModules.security as security


# importing video processing package - cv2 (OpenCV)

"""
try: 
    import cv2
except ImportError:
    util.log("MISSING PACKAGE: 'cv2' - REQUIRED BY 'webcam' MODULE")

# colored terminal text 
try: 
    import colorama
except ImportError:
    sys.exit("CRITICAL ERROR: PACKAGE 'colorama' IS REQUIRED")
"""



###### MAIN FUNCTION ######
def main():
    
    # DEFINE THE PARSER VARIABLE 
    parser = argparse.ArgumentParser(
        prog = 'server.py',
        description = "CC command line server"
    )
    # HOST INFO ARGUMENT
    parser.add_argument(
        '--host',
        action='store',
        type=str,
        default='127.0.0.1',
        help='Please enter your server IP address where server will run'
    )
    # PORT INFO ARGUMENT 
    parser.add_argument(
        '--port',
        action='store',
        type=int,
        default=6969,
        help="Specify server listening port"
    )

    # SPECIFY DATABASE - LINKED TO THE DATABASE MODULE
    # I CAN LINK DIRECTLHY TO THE DATABASE BECAUSE IT'S REFERENCED IN THE PYTHONPATH AND MODULE IMPORT, IMPORTED AS "database"
    
    """
    parser.add_argument(
        '--database',
        action='store',
        type=str,
        default='database.db',
        help='the linked SQLite database'
    )  
    """

   
    options = parser.parse_args()
    globals()['cc'] = CC(host=options.host, port=options.port)




# COMMAND & CONTROL (CC) 
# RETURNS AN INSTANCE OF THE CC SERVER
# WILL BE INSTANTIATED IN THE main() FUNCTION - WRITE THE run() FUNCTION FOR IT TO LAUNCH THE TERMINAL
class CC():
    def __init__(self, host='127.0.0.1', port=6969, db=":memory:"):
        """
        CREATES A NEW COMMAND & CONTROL SERVER, FIRE IT UP WITH SPECIFIED PARAMETERS
        INSTANTIATED WITH THE main() FUNCTION

        DB IS TAKEN FROM :memory:, AS IN THE CURRENT SESSION
        """
        

    def run(self):
        """
        RUN THE COMMAND & CONTROL SERVER TERMINAL
        ALSO IT FIRES UP THE PYTHON HTTP WEB SERVER serve_forever 
        OPENS UP A TERMINAL READY TO RECEIVE COMMANDS, ALSO REACTS TO KEYBOARD INTERRUPTS
        """

# RUN MAIN FUNCTION ONLY WHEN THIS PROGRAM IS BEING EXECUTED, NOT IMPORTED 
if __name__ == '__main__':
    main()