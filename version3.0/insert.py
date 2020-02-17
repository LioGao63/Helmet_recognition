# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtCore import (QFile, QVariant, Qt)
from PyQt5.QtWidgets import (QApplication, QDialog, QDialogButtonBox, QMenu,
    QMessageBox, QTableView, QVBoxLayout)
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery, QSqlTableModel)
# import psycopg2
import pymysql
import datetime,sys,os

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
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(739, 681)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(230, 130, 21, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 130, 21, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(130, 190, 391, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        TabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        TabWidget.addTab(self.tab1, "")

        conn = pymysql.connect(**DB_CONFIG)
        title = ['ID', '姓名', '时间']
        self.tableWidget.setColumnCount(3)
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
        conn.close()


        self.retranslateUi(TabWidget)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)
        self.pushButton.clicked.connect(TabWidget.add_record)
        self.pushButton_2.clicked.connect(TabWidget.delete_record)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        self.pushButton.setText(_translate("TabWidget", "+"))
        self.pushButton_2.setText(_translate("TabWidget", "-"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Tab 1"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Tab 2"))

class mywindow(QTabWidget,Ui_TabWidget):

    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

    def add_record(self):
        print("添加记录")
        value, ok = QInputDialog.getText(self, "添加", "请输入要添加的姓名:", QLineEdit.Normal, "曾梓晟")
        now_time = datetime.datetime.now()
        record_time = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cur:
            sql = "INSERT INTO record(ID, name, time) VALUES (null, %s, %s);"
            data = [str(value), str(record_time)]
            cur.execute(sql, data)
            conn.commit()
        conn.close()

        conn = pymysql.connect(**DB_CONFIG)
        title = ['ID', '姓名', '时间']
        self.tableWidget.setColumnCount(3)
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
                    # print(item)
                    self.tableWidget.setItem(row, col, item)
        conn.close()



    def delete_record(self):
        print("删除记录")
        value, ok = QInputDialog.getText(self, "删除", "请输入要删除的编号", QLineEdit.Normal, "")
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cur:
            sql = "delete from record where ID = %s"
            data = [str(value)]
            cur.execute(sql, data)
            conn.commit()
        conn.close()

        conn = pymysql.connect(**DB_CONFIG)
        title = ['ID', '姓名', '时间']
        self.tableWidget.setColumnCount(3)
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
                    # print(item)
                    self.tableWidget.setItem(row, col, item)
        conn.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())


