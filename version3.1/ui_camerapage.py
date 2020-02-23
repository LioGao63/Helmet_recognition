# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camerapage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMenu, QAction, QToolButton


class Ui_CameraPage(object):
    def setupUi(self, CameraPage):
        CameraPage.setObjectName("CameraPage")
        CameraPage.resize(1080, 800)
        # font_1 = QtGui.QFont()
        font_2 = QtGui.QFont()
        # font_1.setPointSize(14)
        # font_1.setBold(True)
        font_2.setPointSize(10)
        font_2.setBold(True)
        self.toolButton = QtWidgets.QToolButton(CameraPage)
        # self.toolButton.setFont(font_1)
        self.toolButton.setGeometry(QtCore.QRect(20, 10, 71, 31))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(CameraPage)
        # self.toolButton_2.setFont(font_1)
        self.toolButton_2.setGeometry(QtCore.QRect(120, 10, 71, 31))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(CameraPage)
        self.toolButton_3.setGeometry(QtCore.QRect(220, 10, 71, 31))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(CameraPage)
        self.toolButton_4.setGeometry(QtCore.QRect(320, 10, 71, 31))
        self.toolButton_4.setObjectName("toolButton_4")

        # self.label = QtWidgets.QLabel(CameraPage)
        # self.label.setGeometry(QtCore.QRect(21, 74, 640, 480))
        # self.label.setText("")
        # self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(CameraPage)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 60, 757, 348))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(20, 120, 20, 8)
        self.gridLayout.setObjectName("gridLayout")

        self.menu = QMenu(self.toolButton)
        # 向"检测"这个一级菜单添加"检测图像"子菜单
        self.openImageAction = QAction("检测图像", self.menu)
        self.openImageAction.setFont(font_2)
        self.openImageAction.setIcon(QIcon("images/icon1.jpg"))
        self.openImageAction.triggered.connect(CameraPage.openImage)

        # 向"检测"这个一级菜单添加"打开本地视频"子菜单
        self.openVideoAction = QAction("检测视频", self.menu)
        self.openVideoAction.setFont(font_2)
        self.openVideoAction.setIcon(QIcon("images/icon2.jpg"))
        self.openVideoAction.triggered.connect(CameraPage.openVideo)

        # 向"检测"这个一级菜单添加"打开摄像头"子菜单
        self.openCameraAction = QAction("实时检测", self.menu)
        self.openCameraAction.setFont(font_2)
        self.openCameraAction.setIcon(QIcon("images/icon3.jpg"))
        self.openCameraAction.triggered.connect(CameraPage.openCamera2)

        # 将二级菜单加入到一级菜单
        self.menu.addAction(self.openImageAction)
        self.menu.addSeparator()
        self.menu.addAction(self.openVideoAction)
        self.menu.addSeparator()
        self.menu.addAction(self.openCameraAction)

        self.toolButton.setMenu(self.menu)
        self.toolButton.setPopupMode(QToolButton.InstantPopup) # 更换菜单的点击方式



        self.returnButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.returnButton.setFont(font)
        self.returnButton.setMinimumHeight(80)
        self.returnButton.setObjectName("returnButton")
        self.gridLayout.addWidget(self.returnButton, 1, 2, 1, 2)

        self.cameraButton = QtWidgets.QPushButton(QIcon("images/icon2.jpg"), "打开", self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cameraButton.setFont(font)
        self.cameraButton.setObjectName("cameraButton")
        self.cameraButton.setMinimumHeight(80)
        self.cameraButton.setIcon(QIcon(QPixmap()))
        self.gridLayout.addWidget(self.cameraButton, 1, 5, 1, 2)
        self.cameraLabel = QtWidgets.QLabel(self.layoutWidget)
        # self.cameraLabel.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cameraLabel.setFont(font)
        self.cameraLabel.setObjectName("cameraLabel")
        self.cameraLabel.setStyleSheet("background-color: yellow")
        self.gridLayout.addWidget(self.cameraLabel, 5, 0, 2, 9)

        # 设置最小行列长度


        self.retranslateUi(CameraPage)
        # self.toolButton_3.clicked.connect(CameraPage.collect)
        self.toolButton_4.clicked.connect(CameraPage.face)
        QtCore.QMetaObject.connectSlotsByName(CameraPage)

    def retranslateUi(self, CameraPage):
        _translate = QtCore.QCoreApplication.translate
        CameraPage.setWindowTitle(_translate("CameraPage", "摄像头界面"))

        # self.returnButton.setText(_translate("CameraPage", "返回"))
        # self.cameraButton.setText(_translate("CameraPage", "打开摄像头"))
        self.cameraLabel.setText(_translate("CameraPage", ""))

        self.toolButton.setText(_translate("CameraPage", "检测"))
        self.toolButton_2.setText(_translate("CameraPage", "历史记录"))
        self.toolButton_3.setText(_translate("CameraPage", "人脸采集"))
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_CameraPage() # 这是原py中的类,因人而异哦
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
