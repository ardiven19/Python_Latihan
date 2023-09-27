import sys
import PyQt5
from PyQt5.QtWidgets import *

class mainform(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(600, 500)
        self.move(500, 100)
        self.setWindowTitle('kalkulator')
        self.setStyleSheet("background-color: lightslategrey")

        #tampilan harga
        self.tampilan = QTextEdit()
        self.tampilan.setReadOnly(True)

        
        


        
        #layout
        self.layout_1 = QVBoxLayout()
        self.layout_1.addWidget(self.tampilan)
        self.layout_3 = QGridLayout()
        self.layout_2 = QVBoxLayout()
        self.layout_2.addLayout(self.layout_3)
        self.layout_main = QHBoxLayout()
        self.layout_main.addLayout(self.layout_1)
        self.layout_main.addLayout(self.layout_2)
        
        self.setLayout(self.layout_main)




if __name__=='__main__':

    a = QApplication(sys.argv)
    b = mainform()
    b.show()

    a.exec_()

