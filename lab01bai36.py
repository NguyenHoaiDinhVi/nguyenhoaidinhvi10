# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:42:20 2024

@author: Admin
"""

# Tính S = 1**2 + 2**2 + 3**2 + ... + n**2 (n nguyên và lớn hơn 0) 
tong=0
n=int(input("nhập số n nguyên dương:"))
while n<=0:
    n=int(input("nhập lại số n nguyên dương:"))
if n>0:
    for i in range(1,n+1,1):
        tong+= i**2
    print("tổng của dãy số là:", tong)