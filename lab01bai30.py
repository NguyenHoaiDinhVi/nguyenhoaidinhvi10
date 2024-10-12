# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:53:46 2024

@author: PC
"""
nam = int(input("Nhập vào năm:"))
thang = int(input("Nhập vào tháng:"))
if thang in [1, 3, 5, 7, 8, 10, 12]:
    ngay  = 31

elif thang in [4, 6, 9, 11]:
    ngay = 30
else:
    if (nam%4 == 0 and nam %100 !=0) or (nam%400==0):
        ngay = 29 
    else:
        ngay = 28
print(f"tháng {thang} năm {nam} có {ngay} ngày")


    
    