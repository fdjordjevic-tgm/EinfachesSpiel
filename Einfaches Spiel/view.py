# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created: Mon Dec  5 15:36:34 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(587, 305)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        Dialog.setFont(font)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 50, 46, 13))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 46, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 46, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 170, 46, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 210, 46, 13))
        self.label_5.setObjectName("label_5")
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 40, 61, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 40, 51, 191))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(210, 50, 331, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 230, 75, 23))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 230, 75, 23))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 80, 311, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "offen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "korrekt", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "falsch", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "gesamt", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Spiele", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Drücken Sie die Buttons in aufsteigender Richtung", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Neu", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "Ende", None, QtGui.QApplication.UnicodeUTF8))

