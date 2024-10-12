# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:28:51 2024

@author: Admin
"""

# Viết chương trình liệt kê tất cả bộ nghiệm nguyên của phương trình sau: 
#2x + 7y + 9z = 979 với x, y, z > 0 và x + y + z lớn nhất
max=0
DS=[]
tong=979

for x in range(1,tong//2+1):
    for y in range(1,tong//7+1):
        for z in range(1,tong//9+1):
            if 2*x+7*y+9*z==tong:
                   sum = x+y+z
                   if sum> max:
                       max= sum
                       DS=[(x,y,z)]
print(f"{DS} là bộ nghiệm lớn nhất (x+y+z)={max}")
                   