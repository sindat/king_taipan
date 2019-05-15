# compatibility between python 2 and python 3 with the print method
from __future__ import print_function

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

# PYTHONPATH setup
http_server = 'HTTPserver'
if sys.version_info[0] > 2:
    http_server = 'http.server'
    # add serverModules and clientModules directories to PYTHONPATH
    sys.path.append('serverModules')
    sys.path.append('clientModules')

# Import the server modules - they are not written yet!
import serverModules.util as util
import serverModules.database as database
import serverModules.security as security

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

