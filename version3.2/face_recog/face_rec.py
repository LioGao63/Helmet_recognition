#coding=utf-8
#人脸识别类 - 使用face_recognition模块
import datetime

import cv2
import face_recognition
import os
from os.path import join as pjoin
from PyQt5 import QtCore

import pymysql
from PyQt5.QtCore import pyqtSignal

DB_CONFIG = {

            'host': 'localhost',

            'port': 3306,

            'user': 'root',

            'password': '123456',

            'db': 'test',

            'charset': 'utf8mb4',

            # 'cursorclass':pymysql.cursors.DictCursor

        }

class Face_reco(QtCore.QObject):
    finish_signal = pyqtSignal()

    def __init__(self, time):
        super(Face_reco, self).__init__()
        self.time = time

    def facerec_pic(self):
        # 创建记录txt
        output_dir = "txt"  # 文件路径
        try:
            # 是否有这个路径
            if not os.path.exists(output_dir):
                # 创建路径
                os.makedirs(output_dir)
        except IOError as e:
            print("IOError")
        except Exception as e:
            print("Exception")

        path = "img"  # 模型数据图片目录
        total_image_name = []
        total_face_encoding = []
        for fn in os.listdir(path):  # fn 表示的是文件名q
            print(path + "/" + fn)
            total_face_encoding.append(
                face_recognition.face_encodings(
                    face_recognition.load_image_file(path + "/" + fn))[0])
            fn = fn[:(len(fn) - 4)]  # 截取图片名（这里应该把images文件中的图片名命名为为人物名）
            total_image_name.append(fn)  # 图片名字列表
            print("采样照片获取完毕")


        data_dir = pjoin('face_capture', self.time)
        print(data_dir)
        print("开始识别")
        for i in os.listdir(data_dir):
            if i[22:26] == 'done':
                continue
            image_dir = pjoin(data_dir, i)
            abs_dir = os.path.abspath(os.path.dirname(i))+'\\'+image_dir
            print(abs_dir)
            print(image_dir)
            unknown_picture = face_recognition.load_image_file(image_dir)
            unknown_face_locations = face_recognition.face_locations(unknown_picture)
            unknown_face_encoding = face_recognition.face_encodings(unknown_picture)
            name = "Unknown"
            print("获取未知人物面部信息")
            for (top, right, bottom, left), face_encoding in zip(
                    unknown_face_locations, unknown_face_encoding):
                # 看看面部是否与已知人脸相匹配。
                print("看看面部是否与已知人脸相匹配")
                for i, v in enumerate(total_face_encoding):
                    match = face_recognition.compare_faces(
                        [v], face_encoding, tolerance=0.5)

                    if match[0]:
                        name = total_image_name[i]
                        break

            new_dir = abs_dir.split('.')[0]+'-done.'+abs_dir.split('.')[1]
            os.rename(abs_dir, new_dir)
            print(name)
            with open("txt/"+self.time+"-record.text", "a") as f:
                f.writelines("{},{}\n".format(new_dir, name))
        print("识别完毕，开始添加记录")
        self.add_record()

    #添加txt当中的数据至数据库
    def add_record(self):
        self.path = "txt/"+self.time+"-record.text"
        file = open(self.path, 'r+', encoding='GBK')
        for line in file.readlines():
            curline = line.strip().split(",")
            name = curline[1]
            print(name)
            img_path = curline[0]
            print(img_path)
            time_str = curline[0].split('\\')[-1][0:19]
            print("添加记录")
            record_time = datetime.datetime.strptime(time_str, '%Y-%m-%d-%H-%M-%S')
            if str(name) != "":
                conn = pymysql.connect(**DB_CONFIG)
                with conn.cursor() as cur:
                    sql = "INSERT INTO record(ID, name, time, path) VALUES (null, %s, %s, %s);"
                    data = [str(name), str(record_time), str(img_path)]
                    cur.execute(sql, data)
                    conn.commit()
                conn.close()
        file.seek(0)
        file.truncate()
        file.close()
        print("txt文件清空")

        self.finish_signal.emit()

    def collect_face(self):
        output_dir = 'img'
        i = 1
        cap = cv2.VideoCapture(0)
        while 1:
            ret, frame = cap.read()
            cv2.imshow('cap', frame)
            flag = cv2.waitKey(1)
            if flag == 13:
                # 按下回车键
                output_path = os.path.join(output_dir, "%04d.jpg" % i)
                cv2.imwrite(output_path, frame)
                i += 1
            if flag == 27:
                # 按下ESC键
                break
