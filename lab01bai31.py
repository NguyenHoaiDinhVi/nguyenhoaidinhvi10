# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:32:19 2024

@author: Admin
"""

#b31: Nhập vào ba số nguyên dương. Kiểm tra xem 3 số đó có lập thành tam giác không?
# Nếu có hãy cho biết tam giác đó thuộc loại nào? (Cân, vuông, đều...). 
a=int(input("nhập số a:"))
b=int(input("nhập số b:"))
c=int(input("nhập số c:"))
while a<=0 or b<=0 or c<=0 or ((a+b+c)%1)!=0:
    print("cạnh không thể <=0")
    a=int(input("nhập lại số a:"))
    b=int(input("nhập lại số b:"))
    c=int(input("nhập lại số c:"))
if a+b>c or b+c>a or c+a>b:
        if a==b==c:
            print("3 số tạo thành tam giác đều")
        elif a**2==b*2*+c**2 or b**2==a*2*+c**2 or c**2==a**2+b**2:
            print("ba số tạo thành tam giác vuông")
        elif a==b or b==c or c==a or c==b:
            print("3 số tạo thành một tam giác cân")
        else:
            print("3 số tạo thành một tam giác thường")
            
else:
    print ("không xác định")    
    