import sys
from PyQt5.QtWidgets import *
import random
import copy

class mainform(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(600, 500)
        self.move(500, 100)
        self.setWindowTitle('kalkulator')
        self.setStyleSheet("background-color: lightslategrey")


        self.tampilan = QLineEdit()
        self.tampilan.setReadOnly(True)
        self.tampilan.setFixedSize(500, 300)

        self.tampilan.setStyleSheet("background-color: azure; color: black; font-size: 13px;")
        self.tampilan.setText('selamat datang di game tebak angka, anda silahkan untuk menebak dari angka 1-99')

        #untuk tempat masukan angka
        self.masuk = QLineEdit()
        self.masuk.setFixedSize(500, 50)
        self.masuk.textChanged.connect(self.masukan)
        self.masuk.setStyleSheet("background-color: azure; text-align: center; font-size: 13px; ")

        self.sublayout = QGridLayout()
        tombol = ['oke', 'cek', 'help']
        letak = 0
        for i in tombol:
            self.tombol = QPushButton(i)
            self.sublayout.addWidget(self.tombol, 0, letak)
            letak += 1
            self.tombol.setStyleSheet("background-color: gold; border: none; border-radius: 8px;")
            self.tombol.setFixedSize(150, 50)
            self.tombol.clicked.connect(lambda checked, btn=i: self.klik_tombol(btn))

        #untuk sub layout 1
        self.layout = QGridLayout()
        self.layout.addWidget(self.tampilan, 0, 0)

        #untuk sub layout


        #untuk sublayout 3
        self.sublayout3 = QGridLayout()
        self.sublayout3.addWidget(self.masuk, 0, 0)


        #untuk main layout
        self.mainlayout = QVBoxLayout()
        self.mainlayout.addLayout(self.layout)
        self.mainlayout.addLayout(self.sublayout3)
        self.mainlayout.addLayout(self.sublayout)

        #set layoutnya
        self.setLayout(self.mainlayout)

        self.angkaRandom = None

    def random(self):
        if self.Random is None:
            self.angkaRandom = random.randint(0, 99)
    def masukan(self, text):
        self.saved_text = text
    def klik_tombol(self, btn):
        if btn == 'cek':
            self.tampilan.clear()
            self.masukan(self.saved_text)
            self.random()
            self.copy_random = copy.deepcopy(self.Random)
            if str(self.saved_text) == str(self.copy_random):
                self.tampilan.setText('selamat jawaban anda benar')
            else:
                angka_baru = str(self.saved_text)
                angka_random_baru = str(self.copy_random)
                if angka_baru[0] != angka_random_baru[0] and angka_baru[1] != angka_random_baru[1]:
                    if angka_baru[1] > angka_random_baru[1] and angka_baru[0] > angka_random_baru[0]:
                        self.tampilan.clear()
                        self.tampilan.setText('angka puluhan terlalu besar dan angka satuan terlalu besar')
                    elif angka_baru[1] < angka_random_baru[1] and angka_baru[0] < angka_random_baru[0]:
                        self.tampilan.clear()
                        self.tampilan.setText('angka puluhan terlalu kecil dan angka satuan terlalu kecil')
                    elif angka_baru[0] > angka_random_baru[0] and angka_baru[1] < angka_random_baru[1]:
                        self.tampilan.clear()
                        self.tampilan.setText('angka puluhan terlalu besar dan angka satuan terlalu kecil')
                    elif angka_baru[0] < angka_random_baru[0] and angka_baru[1] > angka_random_baru[1]:
                        self.tampilan.clear()
                        self.tampilan.setText('angka puluhan terlalu kecil dan angka satuan terlalu besar')

                elif angka_baru[0] == angka_random_baru[0] and angka_baru[1] != angka_random_baru[1]:
                    if angka_baru[1] > angka_random_baru[1]:
                        self.tampilan.clear()
                        self.tampilan.setText('angka puluhan sudah benar dan angka satuan terlalu besar')

                    elif angka_baru[1] < angka_random_baru[1]:
                        self.tampilan.clear()
                        self.tampilan.setText('angka puluhan sudah benar dan angka satuan terlalu kecil')

                elif angka_baru[1] == angka_random_baru[1] and angka_baru[0] != angka_random_baru[0]:
                    if angka_baru[0] > angka_random_baru[0]:
                        self.tampilan.clear()
                        self.tampilan.setText('angka puluhan terlalu besar dan angka satuan sudah benar')
                    elif angka_baru[0] < angka_random_baru[0]:
                        self.tampilan.clear()
                        self.tampilan.setText('angka puluhan terlalu kecil dan angka satuan sudah benar')
        elif btn == 'help':
            self.random()
            self.petunjuk = self.Random % 2
            if self.petunjuk == 0:
                self.tampilan.setText('angkanya adalah genap')
            else:
                self.tampilan.setText('angkanya adalah ganjil')
        elif btn == 'oke':
            self.tampilan.clear()
            self.angkaRandom = None
            self.random()


if __name__=='__main__':

    a = QApplication(sys.argv)
    b = mainform()
    b.show()

    a.exec_()