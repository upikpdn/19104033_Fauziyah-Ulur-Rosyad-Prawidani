# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:54:29 2021

@author: LENOVO
"""

class Titik (object) : 
    def __init__(self, x = 0, y = 0) : 
        # Self adalah this
        self.x = x
        self.y = y
        
    def pindah(self, x, y) : 
        self.x = x
        self.y = y
    
    def cetak(self) : 
        print(f'{self.x}, {self.y}')
 
#Buat Object
titik = Titik()
titik.cetak()
titik.pindah(5, 18)
titik.cetak()