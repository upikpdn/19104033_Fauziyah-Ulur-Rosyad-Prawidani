# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:07:32 2021

@author: LENOVO
"""

x = False
y = True

# if ... else
if x != True : 
    print('print')
else : 
    print('tidak print')
    
# if ... else if ... else
if x != False : 
    print('print')
elif y != False : 
    print('Print Y')

# if(... and ...) ... else
if x != True and y == False : 
    print('print')
else : 
    print('tidak print')