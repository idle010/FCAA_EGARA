#!/usr/bin/env python
# -*- coding: utf-8 -*-
import genroot
import sys

mpk = {}


def init():
    global mpk
    for li in open("result_rr.txt"):
        tmp = li.strip("\n").split(",")
        if genroot.getsup(tmp[1])[1] < 0.3:
            continue
        keys = tmp[0]
        if keys in mpk.keys():
            mpk[tmp[0]].append(tmp[1])
        else:
            mpk[tmp[0]] = [tmp[1]]


def trantos(li):
    tmppos = []
    for i in range(0, len(li)):
        if li[i] == '1':
            tmppos.append(i + 1)
    tmppos = [str(c) for c in tmppos]
    return "{%s}" % (",".join(tmppos))


def trans():
    for k in mpk.keys():
        mpk[k].sort()
        lista = mpk[k]
        for pos_i in range(0, len(lista)):
            lista[pos_i] = trantos(lista[pos_i])

if __name__ == '__main__':
    if (len(sys.argv)) != 2:
        print "usage:python gencrm.py filename"
        sys.exit(0)

    filename = sys.argv[1]
    genroot.init(filename)
    outfi = open("outcrm.txt", "w")
    init()
    trans()
    for c in mpk.keys():
        li = "%s->%s" % (c, ",".join(mpk[c]))
        outfi.write(li + "\n")
    print "crm generated:%d" % len(mpk)
