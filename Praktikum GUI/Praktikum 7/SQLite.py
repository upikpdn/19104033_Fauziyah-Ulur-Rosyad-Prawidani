# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:16:13 2021

@author: LENOVO
"""

from PyQt5.QtSql import *

def connectdb():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('testdb')
    if db.open():
        print('koneksi telah dibuat')
    else:
        print('ERROR: ' + db.lastError().text())


connectdb()
