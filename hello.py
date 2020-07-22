#! /usr/bin/env python
"""
print("hello bioinfo")


from math import * 
r=3
area=int(r)**2*pi
print(area)



num1=3
num2=5

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 ** num2)



num1=3
if num1%2==1:
    print("odd")
else:
    print("even")


num1=21
if num1%3==0 and num1%7==0:
    print(num1,"is 3,7's multi")
elif num1%7==0:
    print(num1,"is 7's multi")
elif num1%3==0:
    print(num1,"is 3's multi")
else:
    print(num1,"not 3,7's multi")



sum=0
for i in range(1,11):
    sum+=i
print(sum)


for i in range(2,10,2):
    for k in range(1,10,1):
        print(f"{i}x{k}={i*k}")



n=5
f=1
while n > 0:
    f*=n
    n-=1
print(f)

def Greet():
    print("hello, bio")
Greet()


def mySum(a:int,b:int):
    return a + b
r1=mySum(2,3)
r2=mySum(5,7)
r3=mySum(10,15)

print(r1)
print(r2)
print(r3)


name=input("ur name: ")
print(f"hello {name}")
print(type(name))



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


"""

#30

l1=['A','T','G','C']
l2=['A','T','G','C']
ltmp=()
def MER(l1,l2,n):
    if n == 1:
        return l2


    
