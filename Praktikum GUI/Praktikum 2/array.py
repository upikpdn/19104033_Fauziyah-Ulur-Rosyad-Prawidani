# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 15:44:18 2021

@author: LENOVO
"""

#Menggunakan variabel 
angka = 10

#Param 1 : Maksimal
for i in range(angka) : 
    print("Angka ke : ")
    print(i)
    
#Param 2 : Minim, Maks (sifat increment)
for i in range (angka, 20) : 
    print("Angka ke : ")
    print(i)

#Param 3 : Max, Min, Lompatan + (increment)
#Param 3 : Max, Min, Lompatan - (decrement)
for i in range(angka, 1, -1) : 
    print("Angka ke : ")
    print(i)

#array
array = [1,2,3,4]

for i in array : 
    print(i, end = '')
    