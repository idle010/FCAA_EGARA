#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bisect
import copy
import genroot
import gmpy2
import sys
import time

MAXLEN = 0
MAXVALUE = 0
A = set()
result = []


fiout = open("result.txt", "w")
rettt = []
sup_f = 0.0


def printset(s):
    for c in s:
        fiout.write(gmpy2.digits(c, 2).zfill(MAXLEN) + "\n")
        supcal = gmpy2.digits(c, 2).zfill(MAXLEN)
        tmp = genroot.getsup(supcal)
        retstr = "%s,%s,%.2f" % (tmp[0], supcal, tmp[1])
        rettt.append(retstr)

def init():
    for line in open("root.txt"):
        global MAXLEN
        MAXLEN = len(line.strip("\n"))
        global MAXVALUE
        MAXVALUE = gmpy2.mpz("1" * MAXLEN, 2)
        A.add(gmpy2.mpz(line.strip("\n"), 2))


def getnum():
    for c in A:
        bisect.insort_left(result, c)

    while len(A) > 0:
        minvalue = min(A)
        A.remove(minvalue)

        tm_ti = time.clock()
        keypos = bisect.bisect_right(result, minvalue)
        cp_result = copy.copy(result[keypos:])
        tm_ti = time.clock()
        for c in cp_result:
            tmp = c | minvalue
            use_tmp = gmpy2.digits(tmp, 2)
            use_tmp = "0" * (genroot.prp_num - len(use_tmp)) + use_tmp

            if (genroot.getsup(use_tmp))[1] < sup_f:
                continue

            if tmp == c:
                continue
            if tmp >= MAXVALUE:
                break
            pos = bisect.bisect_right(result, tmp)
            if result[pos - 1] != tmp:
                bisect.insort_left(result, tmp)
        print("Topology numbers:", len(result),  'used time for sort:%.3f seconds' % (time.clock() - tm_ti))


def main():
    tm_bg = time.time()
    init()
    getnum()
    printset(result)
    print("total result:", len(result))
    print("Finished,total used time:", time.time() - tm_bg)
    

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "usage  :python fcaa.py filename sup"
        print "example:python fcaa.py mushroom.txt 0.7"
        sys.exit(0)

    filename = sys.argv[1]
    sup_f = float(sys.argv[2])

    genroot.init(filename)
    main()
    rettt.sort()
    testopen = open("result_rr.txt", "w")
    for c in rettt:
        testopen.write(c + "\n")
