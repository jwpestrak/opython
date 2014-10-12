"""
wiretimes.py: read the wireshark.bin data file.
"""

import os
import struct

stem = '/home/jwpestrak/Documents/programming/python/Python3/Lesson08/'
fnme = 'wireshark.bin'

os.chdir(stem)
tmstmp_lst = []
f = open(fname, 'rb')
    while True:
        x = unpack(f.readline())
        tmstmp_lst.append(x) 
f.close()

for ts in tmstmp_lst:
    print(ts)
