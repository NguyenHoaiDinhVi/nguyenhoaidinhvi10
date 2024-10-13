# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 07:05:35 2024

@author: Admin
"""

#Viết phương thức kiểm tra giá trị nhập vào phải thuộc đoạn [-89, 90], nếu 
#sai bắt nhập lại (Chú ý: không dùng đệ quy). 
def sone(n):
    n=float(input("nhập vào giá trị thuộc đoạn -89 đến 99:"))
    while n<-89 or n>90:
        n=float(input("nhập lại giá trị thuộc đoạn -89 đến 99:"))
    return -89<= n<=90
print(sone(7))

        
