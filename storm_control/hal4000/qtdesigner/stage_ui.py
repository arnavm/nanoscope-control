# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stage.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(438, 328)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(438, 328))
        Dialog.setMaximumSize(QtCore.QSize(438, 328))
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(360, 290, 75, 24))
        self.okButton.setObjectName("okButton")
        self.leftSButton = QtWidgets.QPushButton(Dialog)
        self.leftSButton.setGeometry(QtCore.QRect(136, 131, 52, 66))
        self.leftSButton.setText("")
        self.leftSButton.setObjectName("leftSButton")
        self.leftLButton = QtWidgets.QPushButton(Dialog)
        self.leftLButton.setGeometry(QtCore.QRect(64, 131, 68, 66))
        self.leftLButton.setText("")
        self.leftLButton.setObjectName("leftLButton")
        self.rightSButton = QtWidgets.QPushButton(Dialog)
        self.rightSButton.setGeometry(QtCore.QRect(255, 132, 52, 66))
        self.rightSButton.setText("")
        self.rightSButton.setObjectName("rightSButton")
        self.rightLButton = QtWidgets.QPushButton(Dialog)
        self.rightLButton.setGeometry(QtCore.QRect(310, 132, 68, 66))
        self.rightLButton.setText("")
        self.rightLButton.setObjectName("rightLButton")
        self.upSButton = QtWidgets.QPushButton(Dialog)
        self.upSButton.setGeometry(QtCore.QRect(188, 79, 66, 52))
        self.upSButton.setText("")
        self.upSButton.setObjectName("upSButton")
        self.upLButton = QtWidgets.QPushButton(Dialog)
        self.upLButton.setGeometry(QtCore.QRect(188, 8, 66, 68))
        self.upLButton.setText("")
        self.upLButton.setObjectName("upLButton")
        self.downLButton = QtWidgets.QPushButton(Dialog)
        self.downLButton.setGeometry(QtCore.QRect(189, 252, 66, 68))
        self.downLButton.setText("")
        self.downLButton.setObjectName("downLButton")
        self.downSButton = QtWidgets.QPushButton(Dialog)
        self.downSButton.setGeometry(QtCore.QRect(189, 198, 66, 52))
        self.downSButton.setText("")
        self.downSButton.setObjectName("downSButton")
        self.posGroupBox = QtWidgets.QGroupBox(Dialog)
        self.posGroupBox.setGeometry(QtCore.QRect(260, 10, 171, 91))
        self.posGroupBox.setObjectName("posGroupBox")
        self.yposText = QtWidgets.QLabel(self.posGroupBox)
        self.yposText.setGeometry(QtCore.QRect(55, 37, 111, 16))
        self.yposText.setText("")
        self.yposText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yposText.setObjectName("yposText")
        self.yposLabel = QtWidgets.QLabel(self.posGroupBox)
        self.yposLabel.setGeometry(QtCore.QRect(10, 36, 41, 20))
        self.yposLabel.setObjectName("yposLabel")
        self.xposLabel = QtWidgets.QLabel(self.posGroupBox)
        self.xposLabel.setGeometry(QtCore.QRect(9, 17, 41, 20))
        self.xposLabel.setObjectName("xposLabel")
        self.xposText = QtWidgets.QLabel(self.posGroupBox)
        self.xposText.setGeometry(QtCore.QRect(54, 17, 111, 16))
        self.xposText.setText("")
        self.xposText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.xposText.setObjectName("xposText")
        self.zeroButton = QtWidgets.QPushButton(self.posGroupBox)
        self.zeroButton.setGeometry(QtCore.QRect(90, 60, 71, 24))
        self.zeroButton.setObjectName("zeroButton")
        self.homeButton = QtWidgets.QPushButton(Dialog)
        self.homeButton.setGeometry(QtCore.QRect(197, 140, 51, 51))
        self.homeButton.setObjectName("homeButton")
        self.moveGroupBox = QtWidgets.QGroupBox(Dialog)
        self.moveGroupBox.setGeometry(QtCore.QRect(10, 200, 171, 111))
        self.moveGroupBox.setObjectName("moveGroupBox")
        self.ymoveLabel = QtWidgets.QLabel(self.moveGroupBox)
        self.ymoveLabel.setGeometry(QtCore.QRect(10, 50, 41, 20))
        self.ymoveLabel.setObjectName("ymoveLabel")
        self.xmoveLabel = QtWidgets.QLabel(self.moveGroupBox)
        self.xmoveLabel.setGeometry(QtCore.QRect(9, 21, 41, 20))
        self.xmoveLabel.setObjectName("xmoveLabel")
        self.goButton = QtWidgets.QPushButton(self.moveGroupBox)
        self.goButton.setGeometry(QtCore.QRect(90, 80, 71, 24))
        self.goButton.setObjectName("goButton")
        self.xmoveDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.moveGroupBox)
        self.xmoveDoubleSpinBox.setGeometry(QtCore.QRect(50, 20, 111, 22))
        self.xmoveDoubleSpinBox.setDecimals(1)
        self.xmoveDoubleSpinBox.setMinimum(-100000.0)
        self.xmoveDoubleSpinBox.setMaximum(100000.0)
        self.xmoveDoubleSpinBox.setObjectName("xmoveDoubleSpinBox")
        self.ymoveDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.moveGroupBox)
        self.ymoveDoubleSpinBox.setGeometry(QtCore.QRect(50, 50, 111, 22))
        self.ymoveDoubleSpinBox.setDecimals(1)
        self.ymoveDoubleSpinBox.setMinimum(-100000.0)
        self.ymoveDoubleSpinBox.setMaximum(100000.0)
        self.ymoveDoubleSpinBox.setObjectName("ymoveDoubleSpinBox")
        self.saveGroupBox = QtWidgets.QGroupBox(Dialog)
        self.saveGroupBox.setGeometry(QtCore.QRect(10, 10, 171, 111))
        self.saveGroupBox.setObjectName("saveGroupBox")
        self.saveComboBox = QtWidgets.QComboBox(self.saveGroupBox)
        self.saveComboBox.setGeometry(QtCore.QRect(10, 20, 151, 22))
        self.saveComboBox.setObjectName("saveComboBox")
        self.addButton = QtWidgets.QPushButton(self.saveGroupBox)
        self.addButton.setGeometry(QtCore.QRect(10, 50, 61, 23))
        self.addButton.setObjectName("addButton")
        self.clearButton = QtWidgets.QPushButton(self.saveGroupBox)
        self.clearButton.setGeometry(QtCore.QRect(100, 50, 61, 23))
        self.clearButton.setObjectName("clearButton")
        self.saveButton = QtWidgets.QPushButton(self.saveGroupBox)
        self.saveButton.setGeometry(QtCore.QRect(10, 80, 61, 23))
        self.saveButton.setObjectName("saveButton")
        self.loadButton = QtWidgets.QPushButton(self.saveGroupBox)
        self.loadButton.setGeometry(QtCore.QRect(100, 80, 61, 23))
        self.loadButton.setObjectName("loadButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HAL-4000 Stage Control"))
        self.okButton.setText(_translate("Dialog", "Ok"))
        self.posGroupBox.setTitle(_translate("Dialog", "Current Position"))
        self.yposLabel.setText(_translate("Dialog", "Y (um):"))
        self.xposLabel.setText(_translate("Dialog", "X (um):"))
        self.zeroButton.setText(_translate("Dialog", "Zero"))
        self.homeButton.setText(_translate("Dialog", "Home"))
        self.moveGroupBox.setTitle(_translate("Dialog", "Move To"))
        self.ymoveLabel.setText(_translate("Dialog", "Y (um):"))
        self.xmoveLabel.setText(_translate("Dialog", "X (um):"))
        self.goButton.setText(_translate("Dialog", "Go"))
        self.saveGroupBox.setTitle(_translate("Dialog", "Saved Positions"))
        self.addButton.setText(_translate("Dialog", "Add"))
        self.clearButton.setText(_translate("Dialog", "Clear"))
        self.saveButton.setText(_translate("Dialog", "Save"))
        self.loadButton.setText(_translate("Dialog", "Load"))

