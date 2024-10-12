# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:19:27 2024

@author: Admin
"""
#Viết chương trình liệt kê tất cả bộ nghiệm nguyên của phương trình sau: 
#2x + 7y + 9z = 979 với (x, y, z > 0)
DS=[]
for x in range(1,979//2+1):
    for y in range(1,979//7+1):
        for z in range(1, 979//2+1):
            DS+=[(x,y,z)]
for i in DS: 
    print("bộ nghiệm",i)
               
                
        