#!/usr/bin env python

#-*- coding:utf-8 -*-


import random
import time
import subprocess
import os

now = datetime.datetime.now()+datetime.timedelta(days=1)
t = now.strftime("%Y%m%d")

def makeList():
    list = range(1,10000)
    slice = random.sample(list, 390)
    return slice

def writeList(n, lcn):
    cmd = "mkdir %s" % t
    if not os.path.exists(t):
        subprocess.call(cmd, shell=True)
    else:
        output = open('%s/%s.txt' % (t,n), 'w')
        for i in lcn:
            output.write("%s\n" % str(i))
        output.close()

def makeGroup():
    mg = makeList()

    five = mg[0:200]
    writeList('5', five)

    ten = mg[200:300]
    writeList('10', ten)

    thrity = mg[300:360]
    writeList('30', thrity)

    hundred = mg[360:380]
    writeList('100', hundred)

    bicentennial = mg[380:390]
    writeList('200', bicentennial)
    

def main():
    makeGroup()

if __name__ == '__main__':
    main()
