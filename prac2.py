#! /usr/bin/env python
"""
#hw1
print("sean")

#hw2
mybase = input("base: ")

def BASE(base):
    if base == 'A':
        return 'Adenine'
    elif base == 'C':
        return 'Cytosine'
    elif base == 'G':
        return 'Guanine'
    elif base == 'T':
        return 'Thymine'
    elif base == 'U':
        return 'Uracil'
          
b=BASE(mybase)
print(b)

#hw3

N=int(input("10/n, n: "))

def SN(n):
    try :
        result= 10//n
    except ZeroDivisionError:
        result= "Re" 
    return result
a=SN(N)
print(a)    
"""
a=5

def FAC(n):
    for i in range(1,int(n)):
        n = n*i
    return n
        
b=FAC(a)
print(b)


