# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:21:10 2024

@author: Admin
"""
#a
dem=0
str_input=input("nhập chuỗi:")
dodai=len(str_input)
print("độ dài của chuỗi:",dodai)
#b
kydb= "!@#$%^&*()-=+./"
demb = 0
for b in str_input:
    if b in kydb:
        demb += 1
        print("kí tự đặc biệt:",b)
print("Số ký tự đặc biệt:",demb,end="\n")
#c
demc=0
for c in str_input:
    if c.islower:
        demc+=1
        print("ký tự viết thường:",c)
print("số kí tự [a-z]:",demc,end="\n")
#d
demd=0
for d in str_input:
    if d.isdigit:
        demd+=1
        print("kí tự [0-9]",d)
print("số kí tự [0-9]",demd,end="\n")
#e
deme=0
for e in str_input:
    if e.isupper:
        print("kí tự viết hoa:",e)
        deme+=1
print("số kí tự viết hoa:",deme,end="\n")

    
