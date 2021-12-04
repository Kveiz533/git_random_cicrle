from PyQt5.Qt import *
import sys
from random import randint
from random_circle import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.search)
        self.do_paint = False

    def search(self):
        self.paint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(randint(1, 255), randint(1, 255), randint(1, 255)))
        r = randint(10, 200)
        x = randint(100, 600)
        y = randint(100, 400)
        qp.drawEllipse(x, y, r, r)

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
