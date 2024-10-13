# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 08:53:06 2024

@author: Admin
"""

# Anh/chị nhập vào một số nguyên dương n và viết các phương thức sau: 
#a) Phương thức tính căn bậc x của số n 
#b) Phương thức trả về số đảo. 
#c) Phương thức kiểm tra có phải là số chính phương. 
#d) Phương thức kiểm tra có phải là số nguyên tố 
#e) Phương thức tính tích các chữ số lẻ. 
#f) Phương thức tính tổng các số nguyên tố nhỏ hơn n 
#g) Phương thức tính tổng các số chính phương nhỏ hơn n. 
#h) Phương thức tính tổng các ước số dương của n. 
import math
#a
def canbac(n):
    return math.pow(n,x)
def sodao(n):
    return 1/n
def chinhphuong(n):
    return math.sqrt(n)%1==0
def nguyento(n):
    if n%i==0 for i in range(2,n+1):
        return True
    else:
        return False