#coding=utf-8
#人脸识别类 - 使用face_recognition模块
import cv2
import face_recognition
import os
from os.path import join as pjoin



def facerec():
    path = "img"  # 模型数据图片目录
    cap = cv2.VideoCapture(0)
    total_image_name = []
    total_face_encoding = []
    for fn in os.listdir(path):  #fn 表示的是文件名q
        print(path + "/" + fn)
        total_face_encoding.append(
            face_recognition.face_encodings(
                face_recognition.load_image_file(path + "/" + fn))[0])
        fn = fn[:(len(fn) - 4)]  #截取图片名（这里应该把images文件中的图片名命名为为人物名）
        total_image_name.append(fn)  #图片名字列表
    while (1):
        ret, frame = cap.read()
    # 发现在视频帧所有的脸和face_enqcodings
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
    # 在这个视频帧中循环遍历每个人脸
        for (top, right, bottom, left), face_encoding in zip(
                face_locations, face_encodings):
        # 看看面部是否与已知人脸相匹配。
            for i, v in enumerate(total_face_encoding):
                match = face_recognition.compare_faces(
                    [v], face_encoding, tolerance=0.5)
                name = "Unknown"
                if match[0]:
                    name = total_image_name[i]
                    break
        # 画出一个框，框住脸
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # 画出一个带名字的标签，放在框下
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255),
                          cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0,
                        (255, 255, 255), 1)
    # 显示结果图像
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



def facerec_pic():
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


    data_dir = 'face_capture'
    for guy in os.listdir(data_dir):
        time_dir = pjoin(data_dir, guy)
        for i in os.listdir(time_dir):
            image_dir = pjoin(time_dir, i)
            print(image_dir)
            unknown_picture = face_recognition.load_image_file(image_dir)
            unknown_face_locations = face_recognition.face_locations(unknown_picture)
            unknown_face_encoding = face_recognition.face_encodings(unknown_picture)
            name = "Unknown"
            for (top, right, bottom, left), face_encoding in zip(
                    unknown_face_locations, unknown_face_encoding):
                # 看看面部是否与已知人脸相匹配。
                for i, v in enumerate(total_face_encoding):
                    match = face_recognition.compare_faces(
                        [v], face_encoding, tolerance=0.5)

                    if match[0]:
                        name = total_image_name[i]
                        break

            print(name)
            with open("txt/record.txt", "a") as f:
                f.writelines("filename{},name{}\n".format(image_dir,name))

    add_record()

#添加txt当中的数据至数据库
def add_record():
    self.path = "txt/record.txt"
    file = open(self.path, 'r', encoding='utf8')
    for line in file.readlines():
        curline = line.strip().split(",")
        name = curline[1]
        img_path = curline[0]
        print("添加记录")
        now_time = datetime.datetime.now()
        record_time = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
        if str(name) != "":
            conn = pymysql.connect(**DB_CONFIG)
            with conn.cursor() as cur:
                sql = "INSERT INTO record(ID, name, time, path) VALUES (null, %s, %s, %s);"
                data = [str(name), str(record_time), str(img_path)]
                cur.execute(sql, data)
                conn.commit()
            conn.close()

def collect_face():
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
