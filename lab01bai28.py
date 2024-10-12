# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:33:14 2024

@author: Admin
"""
v=[]
n=int(input("nhập số n nguyên dương:"))
while n<=0:
    n=int(input("nhập lại số nguyên dương:"))
for i in range(1, n + 1):
        if n % i == 0:
            v.append(i)
print(f"tất cả ước số của {n} là:",v)