# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:26:01 2024

@author: Admin
"""

n=int(input("Nhập một số lẻ dương bất kỳ:"))
tich=1
while n<=0 or n%2==0:
    n=int(input("Nhập lại một số lẻ dương bất kỳ:"))
if n>0 and n%2==1:
    for i in range(1,n+2,1):
        tich*=i
    print("tích của dãy số:",tich)