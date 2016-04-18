import sys
import os
from PyQt4 import QtCore, QtGui
import PyQt4
import pdf2png
import drawing_example


from GUI import Ui_MainWindow
from ChooseFormat import Ui_ChooseFormat
import os

from TabProcessor import *

from test import draw

class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self._parent = parent
        self.ui = Ui_ChooseFormat()
        self.ui.setupUi(self)

    def accept(self):
        instancefactory = None
        if self.ui.radioButton2000.isChecked():
            instancefactory = CoNLL2000()
        if self.ui.radioButton_2002.isChecked():
            instancefactory = CoNLL2002()
        if self.ui.radioButton_2003.isChecked():
            instancefactory = CoNLL2003()
        if self.ui.radioButton_2004.isChecked():
            instancefactory = CoNLL2004()
        if self.ui.radioButton_2005.isChecked():
            instancefactory = CoNLL2005()
        if self.ui.radioButton_2006.isChecked():
            instancefactory = CoNLL2006()
        if self.ui.radioButton_2008.isChecked():
            instancefactory = CoNLL2008()
        if self.ui.radioButton_2009.isChecked():
            instancefactory = CoNLL2009()
        if self.ui.radioButton_MalTab.isChecked():
            instancefactory = MaltTab()

        self.close()
        self._parent.choosen(instancefactory)



    def reject(self):
        self.close()


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.PushButtonAddGold.clicked.connect(self.browse_folder)

    def browse_folder(self):
        app = QtGui.QMainWindow()
        myapp = MyWindow(self)
        myapp.show()

    def choosen(self, factory):

        directory = QtGui.QFileDialog.getOpenFileName(self)
        print(directory)
        f = open(directory)
        l = list(f.readlines())

        instance = factory.create(l)
        #self.graphvizdraw(instance)
        self.qtdraw(instance)

    def graphvizdraw(self, instance):
        d = draw()
        d.drawGraph(instance.edges, instance.tokens)

        label = self.ui.label_picture

        path = os.path.abspath('test-output/round-table.gv.pdf')
        pdf2png.gs_pdf_to_png(path, 70)
        path2 = os.path.abspath('test-output/round-table.gv.png')

        #pixmap = QtGui.QPixmap(path2)
        #label.setPixmap(pixmap)
        myPixmap = QtGui.QPixmap(path2)
       # myScaledPixmap = myPixmap.scaled(label.size())
        label.setPixmap(myPixmap)

        label.show()

    def qtdraw(self, instance):

        pixmap = QtGui.QPixmap(QtCore.QSize(400,400))
        pixmap.fill(QtGui.QColor(200,0,0))
        painter = QtGui.QPainter (pixmap)
        #gradient = QtGui.QLinearGradient(QtCore.QPoint(pixmap.rect().topLeft()),
        #                             QtCore.QPoint(pixmap.rect().bottomLeft()))
        print("painter kész")
        #gradient.setColorAt(0, QtCore.Qt.blue)
        #gradient.setColorAt(0.4, QtCore.Qt.cyan)
        #gradient.setColorAt(1, QtCore.Qt.green)

        #brush = QtGui.QBrush(gradient)
        #painter.fillRect(QtCore.QRectF(0,0,400,400), brush)
        #painter.drawText(QtCore.QRectF(0,0,400,400), QtCore.Qt.AlignCenter,
        #                  "This is az image created with QPainter and QPixmap")

        painter.setBrush(QtGui.QColor(200,200,0))
        painter.setBackground(QtGui.QColor(200,0,0))
        #painter.drawRect(110,15,540,60)
        #painter.drawEllipse(QtCore.QPoint(200, 400), 150, 40)
        painter.drawArc(20,350, 150, 40, 16*0, 16*180)
        del painter
        print("rajzoltam")
        pixmap.save("output.jpg")
        #print("mentve")

        label = self.ui.label_picture
        label.setPixmap(pixmap)
        label.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    myapp.raise_()

    sys.exit(app.exec_())