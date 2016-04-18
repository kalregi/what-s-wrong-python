from PyQt4 import QtGui, QtCore


class Drawing(QtGui.QWidget):
    def __init__(self):
        super(Drawing, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,350,100)
        self.setWindowTitle("Drawing")
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRect(qp, 10,10,10,10)
        qp.end()

    def drawRect(self, qp, x, y, w, h):
        #pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        #qp.setPen(pen)
        qp.setBrush(QtGui.QColor(200, 0, 0))
        qp.drawRect(x, y, w, h)