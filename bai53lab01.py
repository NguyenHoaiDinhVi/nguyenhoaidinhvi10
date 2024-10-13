# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 07:47:31 2024

@author: Admin
"""

#BÀI 53. Nhập vào một số nguyên dương n và viết các phương thức sau 
#a) S = 1 + 2 + 3 +......+ n 
#b) S = 12 +22 +32 +......+n2 
#c) S = 1 + 1/2 + 1/3 +......+ 1/n 
#d) S = 1! + 2! + 3! +......+ n! 
#e) S = 1 * 2 * 3 *......* n
import math
def sone(n):
    return sum(( range(1,n+1)))
#b
def sone1(n):
    return sum(range(12,(2*n)+1,5))
#c
def sone2(n):
    return sum(1/i for i in range(1,n+1))
#d
def sone3(n):
    return sum(math.factorial(i) for i in range(1,n+1))
#e
def sone4(n):
    tich=1
    for i in range(1,n+1):
        tich*= i
    return tich
    

n = int(input("Nhập một số nguyên dương n: "))
print(f"Tổng S = 1 + 2 + ... + {n} = {sone(n)}")
print(f"Tổng S = 1^2 + 2^2 + ... + {n}^2 = {sone1(n)}")
print(f"Tổng S = 1 + 1/2 + ... + 1/{n} = {sone2(n)}")
print(f"Tổng S = 1! + 2! + ... + {n}! = {sone3(n)}")
print(f"Tích S = 1 * 2 * ... * {n} = {sone4(n)}")
    