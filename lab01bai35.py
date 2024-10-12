# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:39:08 2024

@author: Admin
"""

 #Tính S = 1 + 2 + 3 + ... + n (n nguyên và lớn hơn 0)
n=int(input("nhập số n nguyên dương:"))
tong=0
while n<=0:
     n=int(input("nhập lại số n nguyên dương:"))
if n>0:
    for i in range(n):
        tong+=i
    print("tổng của dãy số là:",tong)
     