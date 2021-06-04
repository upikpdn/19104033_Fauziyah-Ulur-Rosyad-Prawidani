# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:12:17 2021

@author: LENOVO
"""


from PyQt5.QtWidgets import *

app = QApplication([])
   
button = QPushButton('Click')

def on_button_clicked():

    alert = QMessageBox()

    alert.setText('You clicked the button!')

    alert.exec_()

 

button.clicked.connect(on_button_clicked)

if __name__ == '__main__':
    button.show()
    app.exec_();