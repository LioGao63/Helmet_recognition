# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'faceCollection.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QPixmap ,QPalette


class Ui_faceCollection(object):
    def setupUi(self, faceCollection):
        faceCollection.setObjectName("faceCollection")
        faceCollection.setEnabled(True)
        faceCollection.resize(575, 475)
        self.label = QtWidgets.QLabel(faceCollection)
        self.label.setGeometry(QtCore.QRect(140, 30, 281, 181))
        self.label.setStyleSheet(
            "font:20pt '楷体';border-width: 1px;border-style: solid;border-color: rgb(255, 0, 0);")
        self.label.setObjectName("label")

        self.toolButton = QtWidgets.QToolButton(faceCollection)
        self.toolButton.setGeometry(QtCore.QRect(160, 240, 90, 31))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(faceCollection.openImage1)

        self.toolButton_1 = QtWidgets.QToolButton(faceCollection)
        self.toolButton_1.setGeometry(QtCore.QRect(290, 240, 90, 31))
        self.toolButton_1.setObjectName("toolButton")
        self.toolButton_1.clicked.connect(faceCollection.collect)

        self.lineEdit = QtWidgets.QLineEdit(faceCollection)
        self.lineEdit.setGeometry(QtCore.QRect(180, 300, 181, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.toolButton_2 = QtWidgets.QToolButton(faceCollection)
        self.toolButton_2.setGeometry(QtCore.QRect(180, 380, 91, 31))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.clicked.connect(faceCollection.submit)

        self.toolButton_3 = QtWidgets.QToolButton(faceCollection)
        self.toolButton_3.setGeometry(QtCore.QRect(320, 380, 91, 31))
        self.toolButton_3.setObjectName("toolButton_3")

        self.retranslateUi(faceCollection)
        QtCore.QMetaObject.connectSlotsByName(faceCollection)

    def retranslateUi(self, faceCollection):
        _translate = QtCore.QCoreApplication.translate
        faceCollection.setWindowTitle(_translate("faceCollection", "人脸采集"))
        self.label.setText(_translate("faceCollection", ""))
        self.toolButton.setText(_translate("faceCollection", "选择本地图片"))
        self.toolButton_1.setText(_translate("faceCollection", "打开摄像头"))
        self.lineEdit.setText(_translate("faceCollection", "输入姓名"))
        self.toolButton_2.setText(_translate("faceCollection", "确定"))
        self.toolButton_3.setText(_translate("faceCollection", "取消"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_faceCollection() # 这是原py中的类,因人而异哦
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
