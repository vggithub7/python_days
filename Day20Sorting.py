#!/bin/python

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here
total=0
for i in range (len(a)):
        numS=0
        for j in range(len(a)-i-1):
                if a[j]>a[j+1]:
            
                        btw=a[j]
                        a[j]=a[j+1]
                        a[j+1]=btw
                        numS+=1
        if numS == 0:
                break
        else :
            total=total+numS
print 'Array is sorted in',total,'swaps.'
print 'First Element:',a[0]
print 'Last Element:',a[n-1]
print 'mukul'
