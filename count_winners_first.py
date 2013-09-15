
#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import datetime
import sys 

zjsl = [5, 10, 30, 100, 200]

now = datetime.datetime.now()-datetime.timedelta(days=1)
t = now.strftime("%Y%m%d")

def readJzTxt():
    zjmap = {}
    zjlc = []
    for n in zjsl:
        fn = open('/root/%s/%s.txt' % (t, n))
        fd = fn.read()
        for i in fd.split('\n'):
            try:
                zjmap[int(i)] = str(n)
                zjlc.append(int(i))
            except:
                pass
    return zjmap, zjlc

def readWbbTxt():
    lc_nd, zjlc = readJzTxt()
    nd_uid = {}
    zj_uid = []
    fn = open('/root/%s/glt%s.txt' % (t, t))
    fd = fn.read()
    for lc in lc_nd:
        for i in fd.split('\n'):
            try:
                k, v = i.split()
                zj_uid.append(int(k))
            except:
                pass
            if int(v) == int(lc):
                nd_uid.setdefault(lc_nd[lc], []).append(int(k))
                
    return nd_uid, zj_uid     

def uniqUid():
    nd_uid, zj_uid = readWbbTxt()
    new_nd_uid = {}
    for nd in nd_uid:
        v = list(set(nd_uid[nd]))
        new_nd_uid[nd] = v
    return new_nd_uid, zj_uid

def checkUid():
    new_nd_uid, zj_uid = uniqUid()
    for a in new_nd_uid['200']:
        if a in new_nd_uid['100']:
            new_nd_uid['100'].remove(a)
        if a in new_nd_uid['30']:
            new_nd_uid['30'].remove(a)
        if a in new_nd_uid['10']:
            new_nd_uid['10'].remove(a)
        if a in new_nd_uid['5']:
            new_nd_uid['5'].remove(a)

    for b in new_nd_uid['100']:
        if b in new_nd_uid['30']:
            new_nd_uid['30'].remove(b)
        if b in new_nd_uid['10']:
            new_nd_uid['10'].remove(b)
        if b in new_nd_uid['5']:
            new_nd_uid['5'].remove(b)

    for c in new_nd_uid['30']:
        if c in new_nd_uid['10']:
            new_nd_uid['10'].remove(c)
        if c in new_nd_uid['5']:
            new_nd_uid['5'].remove(c)

    for d in new_nd_uid['10']:
        if d in new_nd_uid['5']:
            new_nd_uid['5'].remove(d)

    return new_nd_uid, zj_uid

def saveFile(new_nd_uid):
    uid = new_nd_uid['200'] + new_nd_uid['100'] + new_nd_uid['30'] + new_nd_uid['10'] + new_nd_uid['5']
    output = open('ZJ%s.txt' % t, 'w')
    for i in uid:
        output.write("%s\n" % str(i))
    output.close()

def main():
    p = sys.argv[0]
    new_nd_uid, uid = checkUid()
    zj_uid = list(set(uid))
   
    print "\n奶豆和踩楼中奖UID = %s\n" % new_nd_uid
    print "踩楼中奖人数 = %s\n" % len(new_nd_uid['200'] + new_nd_uid['100'] + new_nd_uid['30'] + new_nd_uid['10'] + new_nd_uid['5'])
    print "盖楼中奖UID = %s\n" % zj_uid
    print "盖楼中奖人数 = %s\n" % len(zj_uid)
 
    if p == '-save':
       saveFile(new_nd_uid) 
    else:
       print "\n注:如果使用'-save' 参数,可以将踩楼中奖人UID存到文件内!\n" 
    
if __name__ == '__main__':
    main()    
