# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:04:58 2024

@author: Admin
"""

tong=0
nhan=1
vi=0
n=int(input("nhập số n nguyên dương:"))
x=float(input("nhập số x:"))
while n<=0:
    n=int(input("nhập lại số n nguyên dương:"))
if n>0:
    for i in range(1,n+1,1):
       nhan*=x
       tong+=i
       vi+= nhan/tong
    print("tổng của dãy số là:",round( vi,2))