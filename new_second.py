#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime
import sys 
import os

zjsl = [5, 10, 30, 100, 200]

now = datetime.datetime.now()-datetime.timedelta(days=4)
t = now.strftime("%Y%m%d")
tt = now.strftime("%Y/%m/%d")

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
    gl_uid = {}
    fn = open('/root/%s/glt%s.txt' % (t, t))
    fd = fn.read()
    for i in fd.split('\n'):
        try:
            k, v = i.split()
            zj_uid.append(int(k))
        except:
            pass
        if k in gl_uid:
            gl_uid[k] += 1
        else:
            gl_uid[k] = 1
        for lc in lc_nd:
            if int(v) == int(lc):
                nd_uid.setdefault(lc_nd[lc], []).append(int(k))
    
    return gl_uid, nd_uid, zj_uid     


def parserUid():
    gl_uid, nd_uid, zj_uid = readWbbTxt()
    lc_ten_uid = []
    for i in gl_uid:
        if gl_uid[i] > 10:
            lc_ten_uid.append(i)
    for i in lc_ten_uid:
        for n in nd_uid:
            for k in nd_uid[n]:
                if int(i) == int(k):
                    nd_uid[n].remove(k)

    return nd_uid, zj_uid, lc_ten_uid

def uniqUid():
    nd_uid, zj_uid, lc_ten_uid = parserUid()
    new_nd_uid = {}
    for nd in nd_uid:
        v = list(set(nd_uid[nd]))
        new_nd_uid[nd] = v
    return new_nd_uid, zj_uid, lc_ten_uid

def checkUid():
    new_nd_uid, zj_uid, lc_ten_uid = uniqUid()
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

    return new_nd_uid, zj_uid, lc_ten_uid

def saveFile(new_nd_uid):
    uid = new_nd_uid['200'] + new_nd_uid['100'] + new_nd_uid['30'] + new_nd_uid['10'] + new_nd_uid['5']
    output = open('ZJ%s.txt' % t, 'w')
    for i in uid:
        output.write("%s\n" % str(i))
    output.close()

def main():
    new_nd_uid, uid, lc_ten_uid = checkUid()
    zj_uid = list(set(uid))
    zj_rlt = new_nd_uid['200'] + new_nd_uid['100'] + new_nd_uid['30'] + new_nd_uid['10'] + new_nd_uid['5']
    wj = int(len(zj_uid))-int(len(lc_ten_uid))-int(len(zj_rlt))
    zj = round(float(len(zj_rlt)) / float(len(zj_uid)) * 100, 2)
    print "\n---------------------%s 巢妈团活动@微宝贝盖踩楼分析---------------\n" % tt
    print "\n盖过楼的去重后的UID(共计%s人) = %s\n" % (len(zj_uid),zj_uid)
    print "\n盖楼超过10层的被开除的UID(共计%s人) = %s\n" % (len(lc_ten_uid), lc_ten_uid)
    print "\n奶豆对应的踩中楼的UID(共计%s人) = %s\n" % (len(zj_rlt), new_nd_uid)
    print "\n未踩中楼的共计%d人,总中奖率 = %.2f%%\n" % (wj, zj)
    print "\n--------------------------------------------------------------------\n"
    try:
        if sys.argv[1] == '-save':
            saveFile(new_nd_uid) 
            if os.path.exists('ZJ%s.txt' % t):
                print "%s.txt中奖UID保存成功!\n" % t
            else:
               print "中奖UID保存失败!\n"
        else:
            print "加参数'-save'可将踩楼中奖人UID存到文件内!\n"
    except:
        print "加参数[-save]可将踩楼中奖人UID存到文件内!\n"
if __name__ == '__main__':
    main()    
