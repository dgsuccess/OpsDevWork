#!/usr/bin/env python

import os
import os.path
import sys
import subprocess

def isNum(s):
    for i in s:
        if i not in '1234567890': return False
    return True

def isJava(fn):
    pfn = os.path.join('/proc',fn,'status')
    for line in open(pfn).readlines():
        fp = line.split()
        if fp[0] == 'Name:' and fp[1] == 'java':
            return True
        else:
            continue

def getProcessNum(pn):
    d = []
    lsdir = os.listdir(pn)
    for i in lsdir:
        if isNum(i) and isJava(i):
            d.append(i)
    return d

def exitFunc():
    ec = subprocess.call("/usr/local/nagios/libexec/ssh_hadoop.py", shell=True)
    return ec

def alarm(pid):
    OK = 0
    WARNING = 1
    CRICTICAL = 2
    UNKNOWN = 3
    if len(pid) == 2:
        p1 = pid[0]
        p2 = pid[1]
        print "OK - Hadoop Process is %s and %s !!" % (p1,p2)
        sys.exit(OK)
    elif len(pid) == 1:
        for i in pid:
            if i:
                print "WARNING, Hadoop Process is %s , but one less!" % i
                sys.exit(WARNING)
            else:
                continue
    elif len(pid) == 0:
        ret = exitFunc()
        if ret == 0:
            print "WARNING, Hadoop Process is lose, Restart success!!"
            sys.exit(WARNING)
        else:
            print "CRICTICAL, Hadoop Process is lose, Restart failed!!"
            sys.exit(CRICTICAL)
        
    else:
        print "UNKNOWN, Hadoop status unknown!"
        sys.exit(UNKNOWN)


def main():
    pn = '/proc'
    pid = getProcessNum(pn)    
    alarm(pid)

if __name__ == "__main__":
    main()
