#!/usr/bin/env python
# -*- coding: utf-8 -*-

tmpkk = {"0":"100000",
         "2":"010000",
         "4":"001000",
         "5":"000100",
         "6":"000010",
         "8":"000001" }
tmpkk2 = {
        "1":"1000000",
        "2":"0100000",
        "3":"0010000",
        "4":"0001000",
        "5":"0000100",
        "6":"0000010",
        "7":"0000001"
        }

fo = open("src_zoo.txt", "w")
for li in open("zoo.data"):
    tmpli = li.strip("\n").strip()
    print tmpli
    elist = tmpli.split(",")[1:]
    print elist[-1], elist[-5]
    elist[-1] = ""#tmpkk2[elist[-1]]
    elist[-5] = ""#tmpkk[elist[-5]]
    li_result = "".join(elist)
    fo.write(li_result + "\n")
    
    
        

