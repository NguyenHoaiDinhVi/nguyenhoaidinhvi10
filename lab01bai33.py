# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:38:46 2024

@author: Admin
"""

# Viết chương trình nhập vào số nguyên dương n. Kiểm tra xem n có phải là 
#số chính phương hay không? (Số chính phương là số khi lấy căn bậc 2 có 
#kết quả là nguyên). 
n=int(input("nhập số nguyên dương:"))
import math
while n<=0:
    n=int(input("nhập lại số nguyên dương"))
if n>0:
   if math.sqrt(n)%1==0:
       print(f"{n} là số chính phương")
   else:
       print(f"{n} không là số chính phương")
        