# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chosseFile.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from TabProcessor import *


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ChooseFormat(object):
    def setupUi(self, ChooseFormat):
        ChooseFormat.setObjectName(_fromUtf8("ChooseFormat"))
        ChooseFormat.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(ChooseFormat)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.groupBox = QtGui.QGroupBox(ChooseFormat)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 351, 221))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton2000 = QtGui.QRadioButton(self.groupBox)
        self.radioButton2000.setGeometry(QtCore.QRect(10, 30, 100, 20))
        self.radioButton2000.setObjectName(_fromUtf8("radioButton2000"))
        self.radioButton_2002 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2002.setGeometry(QtCore.QRect(10, 60, 100, 20))
        self.radioButton_2002.setObjectName(_fromUtf8("radioButton_2002"))
        self.radioButton_2003 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2003.setGeometry(QtCore.QRect(10, 90, 100, 20))
        self.radioButton_2003.setObjectName(_fromUtf8("radioButton_2003"))
        self.radioButton_2004 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2004.setGeometry(QtCore.QRect(10, 120, 100, 20))
        self.radioButton_2004.setObjectName(_fromUtf8("radioButton_2004"))
        self.radioButton_2005 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2005.setGeometry(QtCore.QRect(10, 150, 100, 20))
        self.radioButton_2005.setObjectName(_fromUtf8("radioButton_2005"))
        self.radioButton_2006 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2006.setGeometry(QtCore.QRect(10, 180, 100, 20))
        self.radioButton_2006.setObjectName(_fromUtf8("radioButton_2006"))
        self.radioButton_2008 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2008.setGeometry(QtCore.QRect(140, 30, 100, 20))
        self.radioButton_2008.setObjectName(_fromUtf8("radioButton_2008"))
        self.radioButton_2009 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2009.setGeometry(QtCore.QRect(140, 60, 100, 20))
        self.radioButton_2009.setObjectName(_fromUtf8("radioButton_2009"))
        self.radioButton_MalTab = QtGui.QRadioButton(self.groupBox)
        self.radioButton_MalTab.setGeometry(QtCore.QRect(140, 90, 100, 20))
        self.radioButton_MalTab.setObjectName(_fromUtf8("radioButton_MalTab"))

        self.retranslateUi(ChooseFormat)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ChooseFormat.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ChooseFormat.reject)
        QtCore.QMetaObject.connectSlotsByName(ChooseFormat)

    def retranslateUi(self, ChooseFormat):
        ChooseFormat.setWindowTitle(_translate("ChooseFormat", "Choose format", None))
        self.groupBox.setTitle(_translate("ChooseFormat", "Choose format:", None))
        self.radioButton2000.setText(_translate("ChooseFormat", "CoNLL 2000", None))
        self.radioButton_2002.setText(_translate("ChooseFormat", "CoNLL 2002", None))
        self.radioButton_2003.setText(_translate("ChooseFormat", "CoNLL 2003", None))
        self.radioButton_2004.setText(_translate("ChooseFormat", "CoNLL 2004", None))
        self.radioButton_2005.setText(_translate("ChooseFormat", "CoNLL 2005?", None))
        self.radioButton_2006.setText(_translate("ChooseFormat", "CoNLL 2006?", None))
        self.radioButton_2008.setText(_translate("ChooseFormat", "CoNLL 2008?", None))
        self.radioButton_2009.setText(_translate("ChooseFormat", "CoNLL 2009", None))
        self.radioButton_MalTab.setText(_translate("ChooseFormat", "MalTab", None))

