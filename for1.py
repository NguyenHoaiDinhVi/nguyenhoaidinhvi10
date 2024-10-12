# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 08:28:33 2024

@author: Admin
"""

n=int(input("nhập một số nguyên để tính giai thừa"))
GT=1
for i in range(1,n+1):
    GT=GT*i
print("Giai thừa của",n,"là:",GT,)
    