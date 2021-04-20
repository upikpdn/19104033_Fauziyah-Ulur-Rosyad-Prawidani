# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:15:53 2021

@author: LENOVO
"""

try : 
    a = int(input('Masukkan nilai a : '))
    b = int(input('Masukkan nilai b : ')) 
    c = a / b
    
    print('%d / %d = %.2f' %(a,b,c))
    
except ZeroDivisionError as e : 
    print('Error : Tidak boleh dibagi 0')