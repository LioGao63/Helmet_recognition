# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from PyQt5.QtGui import QIcon


class Ui_CameraPage(object):
    def setupUi(self, CameraPage):
        CameraPage.setObjectName("CameraPage")
        CameraPage.setFixedSize(1300, 750)
        self.centralwidget = QtWidgets.QWidget(CameraPage)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.graphicsView = QtWidgets.QLabel(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setMinimumSize(QtCore.QSize(1000, 600))
        self.graphicsView.setStyleSheet("background-color: white")
        self.gridLayout.addWidget(self.graphicsView, 1, 1, 1, 1)




        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.retranslateUi(CameraPage)
        QtCore.QMetaObject.connectSlotsByName(CameraPage)


        #功能
        self.pushButton.clicked.connect(CameraPage.openImage)
        self.pushButton_2.clicked.connect(CameraPage.openVideo)
        self.pushButton_3.clicked.connect(CameraPage.openCamera)
        self.pushButton_6.clicked.connect(CameraPage.stopCamera)



    def retranslateUi(self, CameraPage):
        _translate = QtCore.QCoreApplication.translate
        CameraPage.setWindowTitle(_translate("CameraPage", "Anti No Helmet"))
        self.label_4.setText(_translate("CameraPage", "图像显示界面"))
        self.label.setText(_translate("CameraPage", "检测功能"))
        self.label.setStyleSheet('color:rgb(255, 120, 255)')
        self.pushButton.setText(_translate("CameraPage", "图像检测"))
        self.pushButton_2.setText(_translate("CameraPage", "视频检测"))
        self.pushButton_3.setText(_translate("CameraPage", "实时检测"))
        self.label_2.setText(_translate("CameraPage", "历史记录"))
        self.label_2.setStyleSheet('color:rgb(255, 120, 255)')
        self.pushButton_4.setText(_translate("CameraPage", "查看记录"))
        self.label_3.setText(_translate("CameraPage", "人脸采集"))
        self.label_3.setStyleSheet('color:rgb(255, 120, 255)')
        self.pushButton_5.setText(_translate("CameraPage", "采集人脸"))
        self.pushButton_6.setText(_translate("CameraPage", "关闭摄像头"))
        CameraPage.setWindowIcon(QIcon('helmet.jpg'))  # 设置图标

        CameraPage.setWindowOpacity(0.9)  # 设置窗口透明度
        CameraPage.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        #CameraPage.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        picicon=qtawesome.icon('ei.picasa', color='black')
        videoicon=qtawesome.icon('ei.video-alt', color='black')
        realtimeicon=qtawesome.icon('mdi.camera-gopro', color='black')
        hisicon=qtawesome.icon('mdi.history', color='black')
        faceicon = qtawesome.icon('mdi.face', color='black')

        self.pushButton.setIcon(picicon)
        self.pushButton_2.setIcon(videoicon)
        self.pushButton_3.setIcon(realtimeicon)
        self.pushButton_4.setIcon(hisicon)
        self.pushButton_5.setIcon(faceicon)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = Ui_CameraPage() # 这是原py中的类,因人而异哦
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
