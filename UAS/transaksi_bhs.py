# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transaksi_bhs.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import pymysql.cursors

class transaksi_bhs(object):
    def setupUi(self, BAHASA):
        self.BHS = BAHASA
        BAHASA.setObjectName("MainWindow")
        BAHASA.resize(800, 589)
        self.centralwidget = QtWidgets.QWidget(BAHASA)
        self.centralwidget.setObjectName("centralwidget")
        

        # Membuat label untuk menampilkan kalimat perintah/intruksi
        self.kalPerintah = QtWidgets.QLabel(self.centralwidget)
        self.kalPerintah.setGeometry(QtCore.QRect(20, 50, 551, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.kalPerintah.setFont(font)
        self.kalPerintah.setObjectName("kalPerintah")

        # Membuat label untuk menampilkan kalimat yang akan diterjemahkan
        self.KalTerjemah = QtWidgets.QLabel(self.centralwidget)
        self.KalTerjemah.setGeometry(QtCore.QRect(20, 90, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.KalTerjemah.setFont(font)
        self.KalTerjemah.setObjectName("KalTerjemah")

        # Membuat label bahasa sunda sebagai judul untuk lineEdit yang digunakan untuk menginputkan jawaban
        self.sunda = QtWidgets.QLabel(self.centralwidget)
        self.sunda.setGeometry(QtCore.QRect(30, 140, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.sunda.setFont(font)
        self.sunda.setObjectName("sunda")

        # Membuat label bahasa bugis sebagai judul untuk lineEdit yang digunakan untuk menginputkan jawaban
        self.bugis = QtWidgets.QLabel(self.centralwidget)
        self.bugis.setGeometry(QtCore.QRect(30, 240, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.bugis.setFont(font)
        self.bugis.setObjectName("bugis")

        # Membuat label bahasa banjar sebagai judul untuk lineEdit yang digunakan untuk menginputkan jawaban
        self.banjar = QtWidgets.QLabel(self.centralwidget)
        self.banjar.setGeometry(QtCore.QRect(30, 340, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.banjar.setFont(font)
        self.banjar.setObjectName("banjar")

        # Membuat lineEdit untuk menginputkan jawaban bahasa sunda
        self.txt_sunda = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sunda.setGeometry(QtCore.QRect(30, 190, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_sunda.setFont(font)
        self.txt_sunda.setText("")
        self.txt_sunda.setObjectName("txt_sunda")

        # Membuat lineEdit untuk menginputkan jawaban bahasa bugis
        self.txt_bugis = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_bugis.setGeometry(QtCore.QRect(30, 290, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_bugis.setFont(font)
        self.txt_bugis.setText("")
        self.txt_bugis.setObjectName("txt_bugis")

        # Membuat lineEdit untuk menginputkan jawaban bahasa banjar
        self.txt_banjar = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_banjar.setGeometry(QtCore.QRect(30, 390, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_banjar.setFont(font)
        self.txt_banjar.setText("")
        self.txt_banjar.setObjectName("txt_banjar")

        # Membuat pushbutton
        self.oke_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.oke_pushButton.setGeometry(QtCore.QRect(350, 470, 131, 41))
        self.oke_pushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.oke_pushButton.setObjectName("oke_pushButton")
        
        # Menghoneksikan pushbutton dengan fungsi oke
        self.oke_pushButton.clicked.connect(self.oke)

        BAHASA.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BAHASA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        BAHASA.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BAHASA)
        self.statusbar.setObjectName("statusbar")
        BAHASA.setStatusBar(self.statusbar)
        
        # memanggil fungsi retranslate
        self.retranslateUi(BAHASA)
        QtCore.QMetaObject.connectSlotsByName(BAHASA)

    # Fungsi untuk memberi nama/text pada objek
    def retranslateUi(self, BAHASA):
        _translate = QtCore.QCoreApplication.translate
        BAHASA.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.kalPerintah.setText(_translate("MainWindow", "SILAHKAN TERJEMAH KALIMAT BERIKUT INI"))
        self.KalTerjemah.setText(_translate("MainWindow", "\" AKU MAU MINUM \""))
        self.sunda.setText(_translate("MainWindow", "BAHASA SUNDA"))
        self.bugis.setText(_translate("MainWindow", "BAHASA BUGIS"))
        self.banjar.setText(_translate("MainWindow", "BAHASA BANJAR"))
        self.oke_pushButton.setText(_translate("MainWindow", "OKE"))
      

    # Fungsi ini untuk mengkoneksikan ke database dengan naa database vending
    def koneksi(self):
        con = pymysql.connect(db='vending', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()

    # Fungsi ini untuk menampilkan message box
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
        
    # Fungsi ini untuk menjalankan button "oke" pada halaman detail produk
    def oke(self):
        sunda = self.txt_sunda.text()
        bugis = self.txt_bugis.text()
        banjar = self.txt_banjar.text()
        con = pymysql.connect(db='vending', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()

        # query sql untuk mengambil data bahasa
        sql = "SELECT * from bahasa where sunda=%s and bugis=%s and banjar=%s"
        data = cur.execute(sql, (sunda, bugis, banjar))

        # Percabangan untuk verifikasi bahasa oleh sistem
        if(len(cur.fetchall())>0):
            # jika kalimat yang diinputkan sama dengan database (bernilai true), maka akan menampilkan message box berhasil
            self.messagebox("Berhasil", "Silahkan Ambil Minuman Anda")
        else:
            # jika kalimat yang diinputkan tidak sama (bernilai false), maka akan menampilkan message box gagal
            self.messagebox("GAGAL", "Bahasa yang Anda Masukkan Salah ! ")

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BAHASA = QtWidgets.QMainWindow()
    ui = transaksi_bhs()
    ui.setupUi(BAHASA)
    BAHASA.show()
    sys.exit(app.exec_())
