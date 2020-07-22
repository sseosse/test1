#! /usr/bin/env python

import sys
import json

def read_csv(b):
    ret=[]
    cnt=1
    header=""
    splitted=""
    with open(b,'r') as handle:
        for i in handle:
            if cnt %2 ==1:
                header = i.strip().split(',')
            else :
                splitted = i.strip().split(',')
            cnt+=1
            d=dict(zip(header, splitted))
            ret.append(d)
    return ret

def tojson(l,k):
    with open(k,"w") as handle:
        json.dump(l, handle)








file_name = sys.argv[1]
ret = read_csv(file_name)
tojson(ret, "sample.json")
