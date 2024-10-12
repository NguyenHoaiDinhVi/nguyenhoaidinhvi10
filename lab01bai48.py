# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:19:27 2024

@author: Admin
"""
 #Viết chương trình liệt kê tất cả bộ nghiệm nguyên của phương trình sau: 
#2x + 7y + 9z = 979 với x, y, z > 0 và x + y + z nhỏ nhất
A=[]
min=979
for x in range(1,979//2+1):
    for y in range(1,979//7+1):
        for z in range(1,979//9+1):
            if 2*x+7*y+9*z==979:
              sum= x+y+z
              if sum<min:
                  min= sum
                  A=[(x,y,z)]
print(f"{A}với bộ nghiệm(x+y+z)={min}")