# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spotcounter.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(561, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(561, 640))
        Dialog.setMaximumSize(QtCore.QSize(561, 640))
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(480, 610, 75, 24))
        self.okButton.setObjectName("okButton")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 541, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.countsTab = QtWidgets.QWidget()
        self.countsTab.setObjectName("countsTab")
        self.graphFrame = QtWidgets.QFrame(self.countsTab)
        self.graphFrame.setGeometry(QtCore.QRect(60, 40, 471, 371))
        self.graphFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.graphFrame.setObjectName("graphFrame")
        self.countsText1 = QtWidgets.QLabel(self.countsTab)
        self.countsText1.setGeometry(QtCore.QRect(20, 10, 101, 16))
        self.countsText1.setObjectName("countsText1")
        self.countsLabel1 = QtWidgets.QLabel(self.countsTab)
        self.countsLabel1.setGeometry(QtCore.QRect(130, 10, 61, 16))
        self.countsLabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.countsLabel1.setObjectName("countsLabel1")
        self.label = QtWidgets.QLabel(self.countsTab)
        self.label.setGeometry(QtCore.QRect(100, 480, 341, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.minSpinBox = QtWidgets.QSpinBox(self.countsTab)
        self.minSpinBox.setGeometry(QtCore.QRect(5, 400, 51, 22))
        self.minSpinBox.setMaximum(1000)
        self.minSpinBox.setSingleStep(10)
        self.minSpinBox.setObjectName("minSpinBox")
        self.maxSpinBox = QtWidgets.QSpinBox(self.countsTab)
        self.maxSpinBox.setGeometry(QtCore.QRect(5, 30, 51, 22))
        self.maxSpinBox.setMinimum(10)
        self.maxSpinBox.setMaximum(1000)
        self.maxSpinBox.setSingleStep(10)
        self.maxSpinBox.setProperty("value", 1000)
        self.maxSpinBox.setObjectName("maxSpinBox")
        self.tabWidget.addTab(self.countsTab, "")
        self.imageTab = QtWidgets.QWidget()
        self.imageTab.setObjectName("imageTab")
        self.imageFrame = QtWidgets.QFrame(self.imageTab)
        self.imageFrame.setGeometry(QtCore.QRect(10, 40, 516, 516))
        self.imageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.imageFrame.setObjectName("imageFrame")
        self.countsText2 = QtWidgets.QLabel(self.imageTab)
        self.countsText2.setGeometry(QtCore.QRect(20, 10, 101, 16))
        self.countsText2.setObjectName("countsText2")
        self.countsLabel2 = QtWidgets.QLabel(self.imageTab)
        self.countsLabel2.setGeometry(QtCore.QRect(130, 10, 61, 16))
        self.countsLabel2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.countsLabel2.setObjectName("countsLabel2")
        self.tabWidget.addTab(self.imageTab, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HAL-4000 Spot Counter"))
        self.okButton.setText(_translate("Dialog", "Ok"))
        self.countsText1.setText(_translate("Dialog", "Total Localizations:"))
        self.countsLabel1.setText(_translate("Dialog", "TextLabel"))
        self.label.setText(_translate("Dialog", "This Space Intentionally Left Blank"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.countsTab), _translate("Dialog", "Counts"))
        self.countsText2.setText(_translate("Dialog", "Total Localizations:"))
        self.countsLabel2.setText(_translate("Dialog", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imageTab), _translate("Dialog", "STORM Image"))

