# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 07:37:53 2024

@author: Admin
"""

# Viết phương thức tính chu vi và diện tích hình chữ nhật khi biết độ dài 2 
#cạnh. Sau đó vẽ hình chữ nhật ra màn hình bằng các dấu *. Phương thức 
#tính chu vi, diện tích và phương thức vẽ hình chữ nhật phải độc lập nhau.
def tinh_chuvi(a,b):
    return 2*(a+b)
def tinh_dientich(a,b):
    return a*b
def ve_(a,b):
    for i in range(b):
        print("*"* a)
        
        
a= int(input("Nhập chiều dài hình chữ nhật: "))
b = int(input("Nhập chiều rộng hình chữ nhật: "))
chuvi = tinh_chuvi(a,b)
dientich = tinh_dientich(a,b)
print(f"Chu vi hình chữ nhật: {chuvi}")
print(f"Diện tích hình chữ nhật: {dientich}")
print("Hình vẽ chữ nhật:")
ve_(a,b)