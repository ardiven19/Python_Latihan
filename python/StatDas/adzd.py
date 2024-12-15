import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPainter, QColor, QBrush

class Switch(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCheckable(True)
        self.setFixedSize(60, 30)
        self.update_style()

        self.clicked.connect(self.update_style)

    def update_style(self):
        if self.isChecked():
            self.setStyleSheet("""
                QPushButton {
                    background-color: #4caf50;
                    border-radius: 15px;
                    text-align: left;
                    padding-left: 5px;
                }
            """)
        else:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #cccccc;
                    border-radius: 15px;
                    text-align: right;
                    padding-right: 5px;
                }
            """)

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        knob_color = QColor('#ffffff')

        if self.isChecked():
            knob_rect = self.rect().adjusted(self.width() // 2, 2, -2, -2)
        else:
            knob_rect = self.rect().adjusted(2, 2, -self.width() // 2, -2)

        painter.setBrush(QBrush(knob_color))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(knob_rect)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Switch Example")

        layout = QVBoxLayout()
        self.switch = Switch()
        layout.addWidget(self.switch)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
