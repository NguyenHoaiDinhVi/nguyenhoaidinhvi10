# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:18:18 2024

@author: Admin
"""

n=int(input("Nhập một số chẵn dương bất kỳ:"))
tong=0
while n<=0 or n%2!=0:
    n=int(input("Nhập lại một số chẵn dương bất kỳ:"))
if n>0 and n%2==0:
    for i in range(2,n+1,2):
        tong+=i
    print("tống của dãy số:",tong)


    