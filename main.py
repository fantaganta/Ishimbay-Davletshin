import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5 import uic

from random import randint


class Example(QMainWindow, QWidget):
    def __init__(self):
        print(1)
        super().__init__()
        self.n = 0
        self.paint = False
        uic.loadUi('elipse.ui', self)
        self.show()
        print(2)
        self.pushButton.clicked.connect(self.paint_elipse)

    def paintEvent(self, event):
        if self.paint:
            x = randint(0, 600)
            y = randint(0, 600)
            random_numb_x = randint(0, x)
            random_numb_y = randint(0, y)
            if random_numb_x > random_numb_y:
                self.r = random_numb_y
            else:
                self.r = random_numb_x
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(x, y, self.r * 2, self.r * 2)
            qp.end()

    def paint_elipse(self):
        self.paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())