import sys
import os
from PyQt4 import QtCore, QtGui

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

        d = draw()
        d.drawGraph(instance.edges, instance.tokens)

        label = QtGui.QLabel()
        path = os.path.abspath('test-output/round-table.gv.pdf')
        pixmap = QtGui.QPixmap(path)
        label.setPixmap(pixmap)

        self.ui.scrollArea.setWidget(label)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()

    sys.exit(app.exec_())