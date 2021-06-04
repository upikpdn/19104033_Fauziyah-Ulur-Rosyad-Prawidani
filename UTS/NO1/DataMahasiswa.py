# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataMahasiswa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from EntryForm import *

class Ui_MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("MainWindow")
        Form.resize(436, 484)
        self.DataMahasiswa = QtWidgets.QLabel(Form)
        self.DataMahasiswa.setGeometry(QtCore.QRect(130, 20, 165, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.DataMahasiswa.setFont(font)
        self.DataMahasiswa.setObjectName("DataMahasiswa")

        #Kolom Data Mahasiswa
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(30, 50, 371, 220))
        self.listWidget.setObjectName("listWidget")

        #NIM
        self.NIM = QtWidgets.QLabel(Form)
        self.NIM.setGeometry(QtCore.QRect(20, 290, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NIM.setFont(font)
        self.NIM.setObjectName("NIM")

        #NAMA
        self.Nama = QtWidgets.QLabel(Form)
        self.Nama.setGeometry(QtCore.QRect(20, 320, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Nama.setFont(font)
        self.Nama.setObjectName("Nama")

        #JURUSAN
        self.Jurusan = QtWidgets.QLabel(Form)
        self.Jurusan.setGeometry(QtCore.QRect(20, 350, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Jurusan.setFont(font)
        self.Jurusan.setObjectName("Jurusan")

        #NO TELP
        self.NoTelp = QtWidgets.QLabel(Form)
        self.NoTelp.setGeometry(QtCore.QRect(20, 380, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NoTelp.setFont(font)
        self.NoTelp.setObjectName("NoTelp")

        #KOLOM INPUT NIM
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(85, 290, 315, 20))
        self.lineEdit.setObjectName("lineEdit")

        #KOLOM INPUT NAMA
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(85, 320, 315, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        #KOLOM INPUT JURUSAN
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(85, 350, 315, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        #KOLOM INPUT NO TELP
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(85, 380, 315, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")

        #PUSH BUTTON TAMBAH 
        self.Tambah = QtWidgets.QPushButton(Form)
        self.Tambah.setGeometry(QtCore.QRect(115, 445, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Tambah.setFont(font)
        self.Tambah.setObjectName("Tambah")
        self.Tambah.clicked.connect(self.addButtonClick)

        #PUSH BUTTON EDIT
        self.Edit = QtWidgets.QPushButton(Form)
        self.Edit.setGeometry(QtCore.QRect(195, 445, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Edit.setFont(font)
        self.Edit.setObjectName("Edit")
        self.Edit.clicked.connect(self.editButtonClick)

        #PUSH BUTTON CLEAR
        self.Clear = QtWidgets.QPushButton(Form)
        self.Clear.setGeometry(QtCore.QRect(275, 445, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Clear.setFont(font)
        self.Clear.setObjectName("Clear")
        self.Clear.clicked.connect(self.listWidget.clear)

        #PUSH BUTTON HAPUS
        self.Hapus = QtWidgets.QPushButton(Form)
        self.Hapus.setGeometry(QtCore.QRect(355, 445, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Hapus.setFont(font)
        self.Hapus.setObjectName("Hapus")
        self.Hapus.clicked.connect(self.deleteButtonClick)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.DataMahasiswa.setText(_translate("Form", "DATA MAHASISWA"))
        self.NIM.setText(_translate("Form", "NIM"))
        self.Nama.setText(_translate("Form", "NAMA"))
        self.Jurusan.setText(_translate("Form", "JURUSAN"))
        self.NoTelp.setText(_translate("Form", "NO. TELP"))
        self.Tambah.setText(_translate("Form", "TAMBAH"))
        self.Edit.setText(_translate("Form", "EDIT"))
        self.Clear.setText(_translate("Form", "CLEAR"))
        self.Hapus.setText(_translate("Form", "HAPUS"))

    def addButtonClick(self):
        self.listWidget.addItem(
            self.lineEdit.text() + ' ' +
            self.lineEdit_2.text() + ' ' +
            self.lineEdit_3.text() + ' ' +
            self.lineEdit_4.text())

    def editButtonClick(self):
        if self.listWidget.currentRow() < 0: return
        self.entryForm = EntryForm()
        s = str(self.listWidget.currentItem().text())
        idx = s.index('-')
        self.entryForm.nim.setText(s[:(idx - 1)])
        self.entryForm.nama.setText(s[(idx - 2):])
        self.entryForm.jurusan.setText(s[(idx - 3):])
        self.entryForm.telp.setText(s[(idx - 4):])

        if self.entryForm.exec_() == QDialog.Accepted:
            self.listWidget.currentItem().setText(
                self.entryForm.nim.text() + ' ' +
                self.entryForm.nama.text() + ' ' +
                self.entryForm.jurusan.text() + ' ' +
                self.entryForm.telp.text())

    def deleteButtonClick(self):
        row = self.listWidget.currentRow()
        if row >= 0:
            self.listWidget.takeItem(row)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

