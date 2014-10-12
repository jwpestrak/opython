"""
wiretimes.py: read the wireshark.bin data file.
"""

import os
import struct

stem = '/home/jwpestrak/Documents/programming/python/Python3/Lesson08/'
fnme = 'wireshark.bin'

os.chdir(stem)
tmstmp_lst = []

with open("wireshark.bin", "rb") as f:
    header = f.read(24)
    vals = struct.unpack('<IHHiIII', header)
    print(vals)
