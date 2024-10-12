# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:52:57 2024

@author: Admin
"""

tong=0
n=int(input("nhập số n nguyên dương:"))
while n<=0:
    n=int(input("nhập lại số n nguyên dương:"))
if n>0:
    for i in range(1,n+1,1):
        tong+= 1/(2*i)
    print("tổng của dãy số là:",round( tong,2))