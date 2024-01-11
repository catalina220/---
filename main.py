import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from random import randint


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.circles = []

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Random Circles')
        self.button = QPushButton('Add Circle', self)
        self.button.clicked.connect(self.addCircle)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircles(qp)
        qp.end()

    def addCircle(self):
        diameter = randint(10, 100)

        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        
        x = randint(0, self.width() - diameter)
        y = randint(0, self.height() - diameter)

        self.circles.append((x, y, diameter, r, g, b))
        self.update()

    def drawCircles(self, qp):
        for circle in self.circles:
            x, y, diameter, r, g, b = circle

            qp.setBrush(QColor(r, g, b))
            qp.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    circleWidget = CircleWidget()
    circleWidget.show()
    sys.exit(app.exec_())
