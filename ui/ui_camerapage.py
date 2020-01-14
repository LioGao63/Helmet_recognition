# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camerapage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CameraPage(object):
    def setupUi(self, CameraPage):
        CameraPage.setObjectName("CameraPage")
        CameraPage.resize(855, 443)
        self.layoutWidget = QtWidgets.QWidget(CameraPage)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 757, 348))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.gridLayout.setObjectName("gridLayout")
        self.rightButton = QtWidgets.QPushButton(self.layoutWidget)
        self.rightButton.setMinimumSize(QtCore.QSize(80, 80))
        self.rightButton.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rightButton.setFont(font)
        self.rightButton.setObjectName("rightButton")
        self.gridLayout.addWidget(self.rightButton, 1, 2, 1, 1)
        self.leftButton = QtWidgets.QPushButton(self.layoutWidget)
        self.leftButton.setMinimumSize(QtCore.QSize(80, 80))
        self.leftButton.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.leftButton.setFont(font)
        self.leftButton.setObjectName("leftButton")
        self.gridLayout.addWidget(self.leftButton, 1, 0, 1, 1)
        self.returnButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.returnButton.setFont(font)
        self.returnButton.setObjectName("returnButton")
        self.gridLayout.addWidget(self.returnButton, 4, 0, 1, 3)
        self.cameraButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cameraButton.setFont(font)
        self.cameraButton.setObjectName("cameraButton")
        self.gridLayout.addWidget(self.cameraButton, 3, 0, 1, 3)
        self.cameraLabel = QtWidgets.QLabel(self.layoutWidget)
        self.cameraLabel.setMinimumSize(QtCore.QSize(480, 320))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cameraLabel.setFont(font)
        self.cameraLabel.setObjectName("cameraLabel")
        self.gridLayout.addWidget(self.cameraLabel, 0, 3, 5, 1)
        self.upButton = QtWidgets.QPushButton(self.layoutWidget)
        self.upButton.setMinimumSize(QtCore.QSize(80, 80))
        self.upButton.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.upButton.setFont(font)
        self.upButton.setObjectName("upButton")
        self.gridLayout.addWidget(self.upButton, 0, 1, 1, 1)
        self.downButton = QtWidgets.QPushButton(self.layoutWidget)
        self.downButton.setMinimumSize(QtCore.QSize(80, 80))
        self.downButton.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.downButton.setFont(font)
        self.downButton.setObjectName("downButton")
        self.gridLayout.addWidget(self.downButton, 2, 1, 1, 1)

        self.retranslateUi(CameraPage)
        QtCore.QMetaObject.connectSlotsByName(CameraPage)

    def retranslateUi(self, CameraPage):
        _translate = QtCore.QCoreApplication.translate
        CameraPage.setWindowTitle(_translate("CameraPage", "摄像头界面"))
        self.rightButton.setText(_translate("CameraPage", "右"))
        self.leftButton.setText(_translate("CameraPage", "左"))
        self.returnButton.setText(_translate("CameraPage", "返回"))
        self.cameraButton.setText(_translate("CameraPage", "打开摄像头"))
        self.cameraLabel.setText(_translate("CameraPage", "摄像头画面"))
        self.upButton.setText(_translate("CameraPage", "上"))
        self.downButton.setText(_translate("CameraPage", "下"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_CameraPage() # 这是原py中的类,因人而异哦
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
