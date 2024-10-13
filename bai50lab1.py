# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 07:00:32 2024

@author: Admin
"""

# Viết phương thức kiểm tra một số nhập vào: nếu là số âm có giá trị lẻ thì 
#trả về -1, nếu là số dương có giá trị chẵn thì trả về 1, trường hợp khác trả 
#về 0.
def sone(n):
    if n<0 and n%2==1:
        return -1
    elif n>0 and n%2==0:
        return 1
    else:
        return 0
