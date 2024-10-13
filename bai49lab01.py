# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 06:44:46 2024

@author: Admin
"""

# Viết phương thức kiểm tra một số nhập vào là số chẵn có giá trị âm. Đúng 
#trả về true. Sai trả về false. 

def ktra_so_nay(n):
    return n<0 and n%1==0
print(ktra_so_nay(8))