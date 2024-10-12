# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 16:10:48 2024

@author: Admin
"""

n=int(input("nhập số nguyên"))
if n<=1:
    print("không là số nguyên tố")
else:
    for i in range(2,n+1):
        if n%i==0:
            print("là số nguyên tố")
            break
    else:
        print("không là số nguyên tố")