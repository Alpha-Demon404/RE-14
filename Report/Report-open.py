# Decompile by Xn0r3 with Decompyle++
# File: temp.pyc (Python 2.7)

import os
import sys
import time
if os.path.exists('.Akun/.Bahan'):
    print '[>] Install Bahan \n\n'
    time.sleep(2)
    os.system('bash .Akun/.Bahan')
    os.system('pip2 install --upgrade pip')
    os.system('rm .Akun/.Bahan')

try:
    os.system('python2 .Akun/.Rt')
except ImportError:
    sys.exit()

