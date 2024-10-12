# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:24:34 2024

@author: Admin
"""
N=int(input("nhập số nguyên dương:"))
total = 0
while N<=0 or N%1!=0:
    N=int(input("nhập lại số nguyên dương:"))
while N > 0 and N%1==0:
    total += N % 10  
    N //= 10         
print("tổng các chữ số:",total)