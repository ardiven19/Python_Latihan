import sys
from PyQt5.QtWidgets import *
class mainform(QWidget):
    def __init__(form):
        super().__init__()
        form.setupUi()

    def setupUi(form):
        form.resize(300, 250)
        form.move(100, 100)
        form.setWindowTitle('kalkulator')
        form.setStyleSheet("background-color: indigo; font-size: 20px; font-family: 'Times New Roman', Times, serif;")

        form.tampilan = QLineEdit()
        form.tampilan.setFixedSize(270, 100)
        form.tampilan.setReadOnly(True)
        form.tampilan.setStyleSheet("background-color: darkseagreen; color: black; font-size: 19px; border: none; border-radius: 8px;")

        form.button1 = QPushButton('1')
        form.button2 = QPushButton('2')
        form.button3 = QPushButton('3')
        form.button4 = QPushButton('4')
        form.button5 = QPushButton('5')
        form.button6 = QPushButton('6')
        form.button7 = QPushButton('7')
        form.button8 = QPushButton('8')
        form.button9 = QPushButton('9')
        form.button0 = QPushButton('0')
        form.button_koma = QPushButton('.')
        form.button_tambah = QPushButton('+')
        form.button_kurang = QPushButton('-')
        form.button_kali = QPushButton('x')
        form.button_bagi = QPushButton('/')
        form.button_sama = QPushButton('=')
        form.button_hapus = QPushButton('del')
        form.button_buka = QPushButton('(')
        form.button_tutup = QPushButton(')')
        form.button_pangkat = QPushButton('^')

        form.button1.setStyleSheet("background-color: gold; border: none; border-radius: 8px;")
        form.button2.setStyleSheet("background-color: gold; border: none; border-radius: 8px;")
        form.button3.setStyleSheet("background-color: gold; border: none; border-radius: 8px;")
        form.button4.setStyleSheet("background-color: gold; border: none; border-radius: 8px;")
        form.button5.setStyleSheet("background-color: gold; border: none; border-radius: 8px;")
        form.button6.setStyleSheet("background-color: gold; border: none; border-radius: 8px;")
        form.button7.setStyleSheet("background-color: gold; border: none; border-radius: 8px;")
        form.button8.setStyleSheet("background-color: gold; border: none; border-radius: 8px;")
        form.button9.setStyleSheet("background-color: gold; border: none; border-radius: 8px;")
        form.button0.setStyleSheet("background-color: gold; border: none; border-radius: 8px;")
        form.button_koma.setStyleSheet("background-color: cyan; border: none; border-radius: 8px;")
        form.button_tambah.setStyleSheet("background-color: cyan; border: none; border-radius: 8px;")
        form.button_kurang.setStyleSheet("background-color: cyan; border: none; border-radius: 8px;")
        form.button_kali.setStyleSheet("background-color: cyan; border: none; border-radius: 8px;")
        form.button_bagi.setStyleSheet("background-color: cyan; border: none; border-radius: 8px;")
        form.button_sama.setStyleSheet("background-color: cyan; border: none; border-radius: 8px;")
        form.button_hapus.setStyleSheet("background-color: cyan; border: none; border-radius: 8px;")
        form.button_buka.setStyleSheet("background-color: cyan; border: none; border-radius: 8px;")
        form.button_tutup.setStyleSheet("background-color: cyan; border: none; border-radius: 8px;")
        form.button_pangkat.setStyleSheet("background-color: cyan; border: none; border-radius: 8px;")


        form.button1.setFixedSize(60, 40)
        form.button2.setFixedSize(60, 40)
        form.button3.setFixedSize(60, 40)
        form.button4.setFixedSize(60, 40)
        form.button5.setFixedSize(60, 40)
        form.button6.setFixedSize(60, 40)
        form.button7.setFixedSize(60, 40)
        form.button8.setFixedSize(60, 40)
        form.button9.setFixedSize(60, 40)
        form.button0.setFixedSize(60, 40)
        form.button_koma.setFixedSize(60, 40)
        form.button_tambah.setFixedSize(60, 40)
        form.button_kurang.setFixedSize(60, 40)
        form.button_kali.setFixedSize(60, 40)
        form.button_bagi.setFixedSize(60, 40)
        form.button_sama.setFixedSize(60, 40)
        form.button_hapus.setFixedSize(60, 40)
        form.button_buka.setFixedSize(60, 40)
        form.button_tutup.setFixedSize(60, 40)
        form.button_pangkat.setFixedSize(60, 40)

        layout1 = QGridLayout()
        layout1.addWidget(form.tampilan, 0, 0)
    


        layout = QGridLayout()
        layout.addWidget(form.button_hapus, 0, 0)
        layout.addWidget(form.button_buka, 0, 1)
        layout.addWidget(form.button_tutup, 0, 2)
        layout.addWidget(form.button_pangkat, 0, 3)
        layout.addWidget(form.button9, 1, 2)
        layout.addWidget(form.button8, 1, 1)
        layout.addWidget(form.button7, 1, 0)
        layout.addWidget(form.button6, 2, 2)
        layout.addWidget(form.button5, 2, 1)
        layout.addWidget(form.button4, 2, 0)
        layout.addWidget(form.button3, 3, 2)
        layout.addWidget(form.button2, 3, 1)
        layout.addWidget(form.button1, 3, 0)
        layout.addWidget(form.button0, 4, 0)
        layout.addWidget(form.button_koma, 4, 1)
        layout.addWidget(form.button_tambah, 4, 2)
        layout.addWidget(form.button_kurang, 3, 3)
        layout.addWidget(form.button_kali, 1, 3)
        layout.addWidget(form.button_bagi, 2, 3)
        layout.addWidget(form.button_sama, 4, 3)

        layout_asli = QVBoxLayout()
        layout_asli.addLayout(layout1)
        layout_asli.addLayout(layout)
        
        form.setLayout(layout_asli)

        form.button1.clicked.connect(form.satu)
        form.button2.clicked.connect(form.dua)
        form.button3.clicked.connect(form.tiga)
        form.button4.clicked.connect(form.empat)
        form.button5.clicked.connect(form.lima)
        form.button6.clicked.connect(form.enam)
        form.button7.clicked.connect(form.tujuh)
        form.button8.clicked.connect(form.delapan)
        form.button9.clicked.connect(form.sembilan)
        form.button0.clicked.connect(form.nol)
        form.button_koma.clicked.connect(form.koma)
        form.button_tambah.clicked.connect(form.tambah)
        form.button_kurang.clicked.connect(form.kurang)
        form.button_kali.clicked.connect(form.kali)
        form.button_bagi.clicked.connect(form.bagi)
        form.button_sama.clicked.connect(form.sama)
        form.button_hapus.clicked.connect(form.delete)
        form.button_buka.clicked.connect(form.open)
        form.button_tutup.clicked.connect(form.close)
        form.button_pangkat.clicked.connect(form.pangkat)
        
        form.text = []
    def delete(form):
        form.text.clear()
        form.tampilan.clear()
    def hasil(form, hasil3):
        form.hasil2 = hasil3
        form.tampilan.setText(form.hasil2)
    def variable(form, text):
        form.text.append(text)
        result = ''.join(form.text)
        form.hasil(result)
    def satu(form):
        form.variable('1')
    def dua(form):
        form.variable('2')
    def tiga(form):
        form.variable('3')
    def empat(form):
        form.variable('4')
    def lima(form):
        form.variable('5')
    def enam(form):
        form.variable('6')
    def tujuh(form):
        form.variable('7')
    def delapan(form):
        form.variable('8')
    def sembilan(form):
        form.variable('9')
    def nol(form):
        form.variable('0')
    def koma(form):
        form.variable('.')
    def tambah(form):
        form.variable('+')
    def kurang(form):
        form.variable("-")
    def kali(form):
        form.variable("*")
    def bagi(form):
        form.variable("/")
    def open(form):
        form.variable("(")
    def close(form):
        form.variable(")")
    def pangkat(form):
        form.variable("**")    
    def sama(form):
        form.akhir = ''.join(form.text)
        form.awal = str(eval(form.akhir))
        form.tampilan.setText(form.awal)



if __name__=='__main__':

    a = QApplication(sys.argv)
    b = mainform()
    b.show()

    a.exec_()