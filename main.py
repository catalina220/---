import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random


class CircleDrawer(QMainWindow):
    def __init__(self):
        super(CircleDrawer, self).__init__()
        loadUi('UI.ui', self)  # Загружаем интерфейс из файла UI.ui
        self.setWindowTitle('Circle Drawer')
        self.button_draw_circle.clicked.connect(self.draw_circle)

    def draw_circle(self):
        diameter = random.randint(10, 100)
        painter = QPainter(self)
        painter.setPen(QColor(Qt.yellow))
        painter.setBrush(QColor(Qt.yellow))
        painter.drawEllipse(100, 100, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec_())
