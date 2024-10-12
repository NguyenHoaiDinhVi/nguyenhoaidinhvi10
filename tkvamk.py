# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:39:20 2024

@author: Admin
"""
v="!@#$%^&*()-=+ "
id=(input("id user:"))
length= len(id)
if 6<=length<=24:
    for i in id:
        if i in v:
            print("id user không bao gồm",i)


pw=input("password:")
w="@#$"
length= len(pw)
if 6<= length<= 24:
    for b in pw:
         if b.islower or b.isdigit or b.isupper or b in w:
             print("ok")
             if q in pw:
                 print("hợp lệ")
else:
    print("khong hop le") 
