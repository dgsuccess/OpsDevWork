#!/usr/bin/python

import os
import sys
import os.path



l = []

for dirs,subdirs,files in os.walk(sys.argv[1]):
    for fn in files:
        if fn == 'id.py':
            continue
        print fn

        for f in open(fn).readlines():
            l.append(f.split('\t')[9])

print len(set(l))
            

