# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 07:30:28 2024

@author: Admin
"""

#54.Viết phương thức in ra n phần tử của dãy Fibonacy. 
def fibonacci(n):
    a=0
    b=1
    day=[]
    for i in range(n):
        day.append(a)
        a,b= b,a+b
    return day
n = int(input("Nhập số phần tử của dãy Fibonacci: "))
result = fibonacci(n)
print(f"Dãy Fibonacci gồm {n} phần tử: {result}")