#! /usr/bin/env python
"""
#1
print("hello bioinfo")

#2
from math import * 
r=3
area=int(r)**2*pi
print(area)


#3
num1=3
num2=5

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 ** num2)


#4
num1=3
if num1%2==1:
    print("odd")
else:
    print("even")

#5
num1=21
if num1%3==0 and num1%7==0:
    print(num1,"is 3,7's multi")
elif num1%7==0:
    print(num1,"is 7's multi")
elif num1%3==0:
    print(num1,"is 3's multi")
else:
    print(num1,"not 3,7's multi")


#6
sum=0
for i in range(1,11):
    sum+=i
print(sum)


for i in range(2,10,2):
    for k in range(1,10,1):
        print(f"{i}x{k}={i*k}")


#7
n=5
f=1
while n > 0:
    f*=n
    n-=1
print(f)

def Greet():
    print("hello, bio")
Greet()

#8
def mySum(a:int,b:int):
    return a + b
r1=mySum(2,3)
r2=mySum(5,7)
r3=mySum(10,15)

print(r1)
print(r2)
print(r3)

#9
name=input("ur name: ")
print(f"hello {name}")
print(type(name))


#10
word=input("word: ")
if word.isdigit():
    print(f"{word} is digit")
elif word.isalpha():
    print(f"{word} is string")
else :
    print("??")

import sys
#print(dir(sys)) sys
f=sys.argv[1]
d={}
with open(f,'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for s in line.strip():
            if s in d:
                d[s] += 1
            else :
                d[s] = 1
total = 0 
for k,v in d.items():
    total += v
with open("result.txt",'w') as handle:
    handle.write(f"A: {d['A']}")
    handle.write(f"T: {d['T']}")
    handle.write(f"G: {d['G']}")
    handle.write(f"C: {d['C']}")



#11
import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta]")
    sys.exit()        #error cover
#print("hi", sys.argv[1])
f = sys.argv[1]
try:
    with open(f,'r') as handle:
        read = handle.readlines()
    print(read)
except filenotfounderror:
    print(f"{f} not found.. please check..")
    sys.exit()
print(read)

#12
import sys
import gzip

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta.gz]")
    sys.exit()        #error cover
f = sys.argv[1]
with gzip.open(f,'rb') as handle:
    for line in handle:
        line = line.decode("utf-8")
        print(line.strip())
        sys.exit()

#13
import sys
#print(dir(sys)) sys
import gzip

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta.gz]")
    sys.exit()        #error cover

f=sys.argv[1]
d={}
with gzip.open(f,'rb') as handle:
    for line in handle:
        line = line.decode("utf-8")
        if line.startswith(">"):
            continue
        for s in line.strip():
            if s in d:
                d[s] += 1
            else :
                d[s] = 1
total = 0 
for k,v in d.items():
    total += v
with open("result_gzip.txt",'w') as handle:
    handle.write(f"A: {d['A']}")
    handle.write(f"T: {d['T']}")
    handle.write(f"G: {d['G']}")
    handle.write(f"C: {d['C']}")
    handle.write(f"all : {d['A']+d['T']+d['C']+d['G']}")

#14
seq1="ATGTTATAG"
for i in range(0,len(seq1),3):
    print(i,seq1[i])

#15

seq1="ATGTTATAG"
for i in range(0,len(seq1),3):
    print(i,i+3,seq1[i:i+3])

#16

seq1="ATGTTATAG"
print(seq1[::-1])


#17-1

import sys

def comp1(seq:str)->str:
    comp =""
    for s in seq:
        if s == "A":
            comp +="T"
        elif s == "C":
            comp +="G"
        elif s == "T":
            comp +="A"
        elif s == "G":
            comp +="C"
    return comp
seq = sys.argv[1]
c1=comp1(seq)
print(seq)
print(c1)

#[1] in seq

#17-2
import sys

def comp2(seq:str)->str:
    d_comp = {'A':'T','T':'A','G':'C','C':'G'}
    comp=""
    for s in seq:
        comp += d_comp[s]
    return comp
seq=sys.argv[1]
c2=comp2(seq)
print(seq)
print(c2)

#18

seq1="AGTTTATAG"
for i in range(0,len(seq1)+1):
    if seq1[i:i+2] == "TT":
        print(i)
#19
a=[3,1,1,2,0,0,2,3,3]
max=a[0]
for i in a:
    if i>max:
        max=i
        print(f"max: {max}")
    else:
        continue

#20
a=[3,1,1,2,0,0,2,3,3,]
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)

#21
import sys
def reaD_txt(file_name : str)->str)
    with open(file_name,'r') as handle:
        for line in handle:
            if line,startswith(">"):
                continue
            ret += line.strip()

    return ret
file_name = sys.argv[1]
txt=reaD_txt(file_name)
print(txt)   #not yet

#22
import sys

def reaD_csv(file_name : str)->list:
    ret=[]
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header=line.strip().split(",")
                continue
            splitted = line.strip().split(",")
            d = dict(zip(header, splitted))
            ret.append(d)           
ret += line.strip()
file_name= sys.argv[1]
csv=reaD_csv(file_name)

#23,24
import sys
import json
def reaD_csv(file_name : str)->list:
    with open(file_name,'r') as handle:
        ret=[]    
        for line in handle:
            if line.startswith("#"):
                header=line.strip().split("\t")
                continue
            splitted = line.strip().split("\t")
            d = dict(zip(header, splitted))
            ret.append(d)   
    return ret    
file_name= sys.argv[1]
print(reaD_csv(file_name))


#25
import sys
import json

def read_txt(file_name: str) -> str:
    ret = ""
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            ret += line.strip()
    return ret

 

def read_csv(file_name: str) -> list:
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split(",")
                continue
            splitted = line.strip().split(",")
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

 

def read_tsv(file_name: str) -> list:
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split("\t")
                continue
            splitted = line.strip().split("\t")
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

def to_json(l: list) -> None:
    with open("read_sample.json",'w') as handle:
        json.dump(l, handle, indent=4)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("#usage: python {sys.argv[0]} [txt]")
        sys.exit()

file_name = sys.argv[1]
#txt = read_txt(file_name)
#print(txt)
#ret = read_csv(file_name)
ret = read_tsv(file_name)
to_json(ret)

#26
import sys

class FASTA:
    def __init__(self,file_name:str):
        self.file_name=file_name
        self.count={}
        self.length=0
    def count_base(self):
        with open(self.file_name,'r') as handle:
            for line in handle:
                if line.startswith(">"):
                    continue
                line=line.strip()
                for s in line:
                    if s in self.count:
                        self.count[s]+=1
                    else:
                        self.count[s]=1

    def get_length(self):
        for k,v in self.count.items():
            self.length +=v

if __name__=="__main__":
    if len(sys.argv) !=2:
        print("#usage: python {sys.argv[0]} [txt]")
        sys.exit()
    file_name = sys.argv[1]
    t = FASTA(file_name)
    t.count_base()
    print(t.count)
    t.get_length()
    print(t.length)

#27
import sys
class FASTQ:
    def __init__(self,file_name:str):
        self.file_name=file_name
        self.length=0
        
    def count_length(self):
        with open(self.file_name,'r') as handle:
            cnt = 0
            for line in handle:
                
                if cnt % 4 == 0:
                    header = line.strip()
                    self.length +=1
                elif cnt % 4 == 1:
                    seq = line.strip()
                elif cnt % 4 == 3:
                    qual = line.strip()
                cnt+=1 
            
if __name__=="__main__":
    if len(sys.argv) !=2:
        print("#usage: python {sys.argv[0]} [txt]")
        sys.exit()
    file_name = sys.argv[1]
    t = FASTQ(file_name)
    t.count_length()
    print(t.length)

#28
#29
#30


#31 
import sys

l1=['A','T','G','C']
l2=['A','T','G','C']

def MER(l1,l2,n):
    if n==1:
        return l2
    ltmp=[]
    for s1 in l1:
        for s2 in l2:
            ltmp.append(s1+s2)
    return MER(l1,ltmp,n-1)

n = int(sys.argv[1])        
print(MER(l1,l2,n))
"""


