import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QApplication


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self): 
        self.setWindowTitle("KALKULATOR")
        self.setFixedSize(350, 400)
        self.setStyleSheet("background-color: #1e1e1e;")

        #untuk tampilan
        self.tampilan = QTextEdit()
        self.tampilan.setStyleSheet("background-color: white;")
        self.tampilan.setReadOnly(True)
        self.tampilan.setFixedSize(300, 100)

        self.mainlayout = QGridLayout()


        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        for button in buttons:
            self.button = QPushButton(button)
            self.mainlayout.addWidget(self.button)

        
        self.layout_1 = QHBoxLayout()
        self.layout_1.addWidget(self.tampilan)


        #untuk tombol
        self.btn_1 = QPushButton("1")
        self.btn_2 = QPushButton("2")
        self.btn_3 = QPushButton("3")
        self.btn_4 = QPushButton("4")
        self.btn_5 = QPushButton("5")
        self.btn_6 = QPushButton("6")
        self.btn_7 = QPushButton("7")
        self.btn_8 = QPushButton("8")
        self.btn_9 = QPushButton("9")
        self.btn_0 = QPushButton("0")
        self.btn_plus = QPushButton("+")
        self.btn_minus = QPushButton("-")
        self.btn_mul = QPushButton("*")
        self.btn_div = QPushButton("/")
        self.btn_equal = QPushButton("=")
        self.btn_clear = QPushButton("del")
        self.btn_pangkat = QPushButton("^")
        self.btn_koma = QPushButton(".")
        self.btn_akar = QPushButton("akar")
        self.btn_sisa = QPushButton("sisa") 

        self.btn_1.setFixedSize(70, 35)
        self.btn_2.setFixedSize(70, 35)
        self.btn_3.setFixedSize(70, 35)
        self.btn_4.setFixedSize(70, 35)
        self.btn_5.setFixedSize(70, 35)
        self.btn_6.setFixedSize(70, 35)
        self.btn_7.setFixedSize(70, 35)
        self.btn_8.setFixedSize(70, 35)
        self.btn_9.setFixedSize(70, 35)
        self.btn_0.setFixedSize(70, 35)
        self.btn_plus.setFixedSize(70, 35)
        self.btn_minus.setFixedSize(70, 35)
        self.btn_mul.setFixedSize(70, 35)
        self.btn_div.setFixedSize(70, 35)
        self.btn_equal.setFixedSize(70, 35)
        self.btn_clear.setFixedSize(70, 35)
        self.btn_pangkat.setFixedSize(70, 35)
        self.btn_koma.setFixedSize(70, 35)
        self.btn_akar.setFixedSize(70, 35)
        self.btn_sisa.setFixedSize(70, 35)



        self.layout_2 = QGridLayout()
        self.layout_2.addWidget(self.btn_clear, 0, 0)
        self.layout_2.addWidget(self.btn_pangkat, 0, 1)
        self.layout_2.addWidget(self.btn_akar, 0, 2)
        self.layout_2.addWidget(self.btn_sisa, 0, 3)
        self.layout_2.addWidget(self.btn_7, 1, 0)
        self.layout_2.addWidget(self.btn_8, 1, 1)
        self.layout_2.addWidget(self.btn_9, 1, 2)
        self.layout_2.addWidget(self.btn_div, 1, 3)
        self.layout_2.addWidget(self.btn_4, 2, 0)
        self.layout_2.addWidget(self.btn_5, 2, 1)
        self.layout_2.addWidget(self.btn_6, 2, 2)
        self.layout_2.addWidget(self.btn_mul, 2, 3)
        self.layout_2.addWidget(self.btn_1, 3, 0)
        self.layout_2.addWidget(self.btn_2, 3, 1)
        self.layout_2.addWidget(self.btn_3, 3, 2)
        self.layout_2.addWidget(self.btn_minus, 3, 3)
        self.layout_2.addWidget(self.btn_0, 4, 0)
        self.layout_2.addWidget(self.btn_koma, 4, 1)
        self.layout_2.addWidget(self.btn_plus, 4, 2)
        self.layout_2.addWidget(self.btn_equal, 4, 3)


        
        #untuk umum
        self.layout_main = QGridLayout()
        self.layout_main.addLayout(self.layout_1, 0, 0)
        self.layout_main.addLayout(self.layout_2, 1, 0)

        self.setLayout(self.mainlayout)

        #untuk algoritma perhitungan



if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())

        