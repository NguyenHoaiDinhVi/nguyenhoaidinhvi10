# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:46:18 2024

@author: Admin
"""

#Viết chương trình tính tiền cước TAXI. Biết rằng: 1 km đầu tiên là 15000đ, 
#từ km thứ 2 đến thứ 5 giá là 13500đ, từ km thứ 6 giá là 11000đ, nếu đi 
#hơn 120km thì sẽ được giảm 10% trên tổng tiền.
money=0
n=int(input("nhập số km mà bạn đi taxi:"))
if n==1:
    print("tiền taxi là 15000đ")
if 1<n<6:
    for i in range(2,n+1):
       money+= i*13500
    print("tiền taxi là:",money)
if 120>=n>=6:
    for i in range(6,n+1):
        money+= i*11000
    print("tiền taxi là:",money)
if n>120:
    for i in range(121,n+1):
        money+= i*11000*0.1
    print("tiền taxi là:",money)