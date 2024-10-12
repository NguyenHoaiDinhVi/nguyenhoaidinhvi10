# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:09:25 2024

@author: Admin
"""
n = int(input("Nhập một giá trị nguyên n: "))
dict = {i:i**2 for i in range(1, n+1)}
print(dict)