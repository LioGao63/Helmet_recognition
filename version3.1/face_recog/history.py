# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import pymysql
import datetime,sys,os
# 数据库说明：
# 表名：record
# ID：主键，整数，自增
# name: 字符串
# time: datetime
# path: 字符串
#以下是mysql定义，包括用户名及密码
DB_CONFIG = {

            'host': 'localhost',

            'port': 3306,

            'user': 'root',

            'password': '123456',

            'db': 'test',

            'charset': 'utf8mb4',

            # 'cursorclass':pymysql.cursors.DictCursor

        }
class Ui_TabWidget(object):

    #操作按键部分，有查看和删除两个按键
    def viewButton(self,id):
        widget = QWidget()
        button = QtWidgets.QPushButton("查看")
        button.clicked.connect(lambda :self.viewImg(id))
        deleteButton = QtWidgets.QPushButton("删除")
        deleteButton.clicked.connect(lambda :self.delete_record(id))
        hLayout = QHBoxLayout()
        hLayout.addWidget(button)
        hLayout.addWidget(deleteButton)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    #查看图片模块
    def viewImg(self,id):
        print("查看图片")
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cur:
            sql = "select path from record where ID = %s;"
            data = [str(id)]
            cur.execute(sql, data)
            ndata = cur.fetchall()
            for img in ndata:
                jpg = QtGui.QPixmap(img[0]).scaled(300, 200)
                self.label.setPixmap(jpg)

    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(1080, 800)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(50, 150, 600, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        TabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        TabWidget.addTab(self.tab1, "")
        self.label = QLabel(self)
        self.label.setText("显示图片")
        self.label.setFixedSize(300, 200)
        self.label.move(720, 250)
        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )

        conn = pymysql.connect(**DB_CONFIG)
        title = ['ID', '姓名', '时间','操作']
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(title)
        with conn.cursor() as cur:
            sql = "select ID, name, time from record;"
            cur.execute(sql)
            ndata = cur.fetchall()
            for row,line in enumerate(ndata):
                self.tableWidget.setRowCount(row+1)
                for col,itemdata in enumerate(line):
                    item = QTableWidgetItem()
                    item.setText(str(line[col]))
                    # print(item)
                    self.tableWidget.setItem(row, col, item)
                    if col==2:
                        self.tableWidget.setCellWidget(row, col+1, self.viewButton(line[0]))
        conn.close()


        self.retranslateUi(TabWidget)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Tab 1"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Tab 2"))

    #删除记录模块
    def delete_record(self,id):
        print("删除记录")
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cur:
            sql = "delete from record where ID = %s"
            data = [str(id)]
            cur.execute(sql, data)
            conn.commit()
        conn.close()

        conn = pymysql.connect(**DB_CONFIG)
        title = ['ID', '姓名', '时间', '操作']
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(title)
        with conn.cursor() as cur:
            sql = "select ID, name, time from record;"
            cur.execute(sql)
            ndata = cur.fetchall()
            for row, line in enumerate(ndata):
                self.tableWidget.setRowCount(row + 1)
                for col, itemdata in enumerate(line):
                    item = QTableWidgetItem()
                    item.setText(str(line[col]))
                    self.tableWidget.setItem(row, col, item)
                    if col == 2:
                        self.tableWidget.setCellWidget(row, col + 1, self.viewButton(line[0]))
        conn.close()

class mywindow(QTabWidget,Ui_TabWidget):

    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())

