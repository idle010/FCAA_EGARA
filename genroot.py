#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gmpy2

sup_F = 0.5
sup_F = 0.6
sup_F = 0.7
sup_F = 0.9
sup_F = 0.4

maxlen = 0
prp_num = 0
obj_num = 0

filename = "src_web.txt"
filename = "src_connect4.txt"
filename = "cpsrc1.txt"
filename = "src1.txt"
filename = "src_chess.txt"
filename = "src_zoo.txt"
filename = "src_mushroom.txt"

object_ss = []

fac_lines = open(filename).readlines()
fac_lines = [c.strip("\n").strip() for c in fac_lines]
while "" in fac_lines:
    fac_lines.remove("")
prp_num = len(fac_lines[0])
obj_num = len(fac_lines)

fac_ver = [''] * prp_num

for i in range(0, prp_num):
    for j in range(0, obj_num):
        fac_ver[i] += fac_lines[j][i]


def getroot():
    lines = []
    for li in open(filename):
        li = li.strip("\n")
        if len(li) == 0:
            continue
        lines.append(li)

    global maxlen
    maxlen = len(lines[0])
    roots = [gmpy2.mpz("1" * maxlen, 2)] * maxlen
    for i in range(0, len(lines[0])):
        for li in lines:
            if li[i] == '1':
                roots[i] &= gmpy2.mpz(li, 2)
    while gmpy2.mpz("1" * maxlen, 2) in roots:
        roots.remove(gmpy2.mpz("1" * maxlen, 2))
    ss = set(roots)
    roots = list(ss)
    roots.sort()
    return roots


def getsup(obj):
    sups = "1" * obj_num
    sups_gmp = gmpy2.mpz(sups, 2)
    for i in range(0, len(obj)):
        if obj[i] == '1':
            sups_gmp &= gmpy2.mpz(fac_ver[i], 2)
    sups_gmp = gmpy2.digits(sups_gmp, 2)
    tmp_lie = "0" * (obj_num - len(sups_gmp)) + sups_gmp
    object_ss.append(tmp_lie)

    total_one = 0
    for i in range(0, len(sups_gmp)):
        if sups_gmp[i] == '1':
            total_one += 1

    return tmp_lie, round(total_one * 1.0 / obj_num, 6)

if __name__ == '__main__':
    files = open("root.txt", "w")
    for i in getroot():
        tmp = gmpy2.digits(i, 2)
        tmp = "0" * (maxlen - len(tmp)) + tmp

        root_sups = getsup(tmp)[1]
        print tmp, "sup:", root_sups
        if root_sups < sup_F:
            continue
        files.write(tmp + "\n")
