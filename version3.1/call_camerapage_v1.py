import datetime


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from face_recog import face_rec
from ui_camerapage import Ui_CameraPage
from ui_faceCollection import Ui_faceCollection
from PyQt5 import QtWidgets, QtCore
import sys
from sys import platform


from models import *  # set ONNX_EXPORT in models.py
from utils.datasets import *
from utils.utils import *


class CameraPageWindow(QWidget, Ui_CameraPage):

    returnSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(CameraPageWindow, self).__init__(parent)

        self.timer_camera = QTimer()  # 初始化定时器
        self.cap = cv2.VideoCapture()  # 初始化摄像头
        self.CAM_NUM = 0
        self.setupUi(self)
        self.initUI()
        self.slot_init()
        self.setWindowTitle("安全帽检测")

    def initUI(self):
        self.setLayout(self.gridLayout)

    def slot_init(self):
        self.timer_camera.timeout.connect(self.show_camera)

    # 信号和槽连接

        # self.cameraButton.clicked.connect(self.slotCameraButton)

    def openImage(self):
        try:
            fname, _ = QFileDialog.getOpenFileName(self, '打开图片', '/', 'Image files (*.jpg *.gif *.png)')
            print(fname)
            # self.cameraLabel.setPixmap(QPixmap(self.show_camera(fname)))
            self.show_camera(fname)
        except:
            self.cameraLabel.setText("打开文件失败，可能是文件类型错误")

    def openVideo(self):
        try:
            fname, _ = QFileDialog.getOpenFileName(self, '打开视频', '/', 'Video files(*.mp4 *.avi *.mov *.rmvb)')
            print(fname)

            #self.cameraLabel.setPixmap(QPixmap(self.show_camera(fname)))
            self.show_camera(fname)
        except:
            self.cameraLabel.setText("打开视频失败，可能是文件类型错误")



    def openCamera(self):
        self.show_camera()



    def show_camera(self, imageSource='0', save_txt=False, save_img=False):
        cfg = 'cfg/yolov3_5.cfg'
        conf_thres = 0.4
        nms_thres = 0.35
        img_size = 416
        name_data = 'data/hat.names'
        out, source, weights, half, view_img = 'output', imageSource, 'weights/backup80.pt', False, True
        webcam = source == '0' or source.startswith('rtsp') or source.startswith('http') or source.endswith('.txt')
        face_capture_path = 'face_capture/'
        face_num = 0
        # 初始化
        device = torch_utils.select_device(device='cpu')
        if os.path.exists(out):
            shutil.rmtree(out)   # 删除输出文件夹
        os.makedirs(out)  # 建立新的输出文件夹

        # 初始化模型
        model = Darknet(cfg, img_size)

        # 加载权重
        if weights.endswith('.pt'):  # pytorch格式
            model.load_state_dict(torch.load(weights, map_location=device)['model'])
        else:  # darknet格式
            _ = load_darknet_weights(model, weights)

        classify = False
        if classify:
            modelc = torch_utils.load_classifier(name='resnet101', n=2)  # initialize
            modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=device)['model'])  # load weights
            modelc.to(device).eval()


        # eval模式
        model.to(device).eval()

        # 数据装载
        vid_path, vid_writer = None, None
        if webcam:
            view_img = True
            torch.backends.cudnn.benchmark = True  # set True to speed up constant image size inference
            dataset = LoadStreams(source, img_size=img_size, half=half)  # 如果--source=0，则调用摄像头
        else:
            save_img = True
            dataset = LoadImages(source, img_size=img_size, half=half)

        # 获取名字和画框颜色
        names = load_classes(name_data)
        colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(names))]

        t0 = time.time()
        t_start = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')

        for path, img, im0s, vid_cap in dataset:
            t = time.time()

            # 获取预测结果
            img = torch.from_numpy(img).to(device)
            if img.ndimension() == 3:
                img = img.unsqueeze(0)
            pred = model(img)[0]

            if half:
                pred = pred.float()

            # 应用NMS(非极大值抑制)
            pred = non_max_suppression(pred, conf_thres, nms_thres)

            if classify:
                pred = apply_classifier(pred, modelc, img, im0s)

            # Process detections
            for i, det in enumerate(pred):  # detections per image
                t1 = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d-%H-%M-%S')
                if webcam:  # batch_size >= 1
                    p, s, im0 = path[i], '%g: ' % i, im0s[i]
                else:
                    p, s, im0 = path, '', im0s

                save_path = str(Path(out) / Path(p).name)
                s += '%gx%g ' % img.shape[2:]
                if det is not None and len(det):
                    # 将box从img_size缩放至im0(图片原始大小)
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                    # 打印结果
                    for c in det[:, -1].unique():
                        n = (det[:, -1] == c).sum()
                        s += '%g %ss, ' % (n, names[int(c)])

                    # 写入结果
                    for *xyxy, conf, _, cls in det:
                        if save_txt:  # Write to file
                            with open(save_path + '.txt', 'a') as file:
                                file.write(('%g ' * 6 + '\n') % (*xyxy, cls, conf))

                        if save_img or view_img:  # 把bbox添加至图像
                            label = '%s %.2f' % (names[int(cls)], conf)
                            plot_one_box(xyxy, im0, label=label, color=colors[int(cls)])


                        # 截取识别出的人脸
                        cls_name = names[int(cls)]
                        if cls_name == 'person':
                            if not os.path.exists(face_capture_path + t_start):
                                os.makedirs(face_capture_path + t_start)
                            cropim0 = im0[int(xyxy[1]):int(xyxy[3]), int(xyxy[0]):int(xyxy[2])]
                            cv2.imwrite(face_capture_path + t_start + '/' + t1 + '-' + str(face_num) + '.jpg', cropim0)
                            print("人脸图片区域已记录")
                            face_num += 1


                # 打印时间(检测时间+NMS)
                print('%sDone. (%.3fs)' % (s, time.time() - t))

                # 结果
                if view_img:
                    show = cv2.resize(im0, (800, 640))
                    show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
                    showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                    self.cameraLabel.setPixmap(QPixmap.fromImage(showImage))


                # 保存结果（图片）
                if save_img:
                    if dataset.mode == 'images':
                        cv2.imwrite(save_path, im0)
                    else:  # 视频处理
                        if vid_path != save_path:  # new video
                            vid_path = save_path
                            if isinstance(vid_writer, cv2.VideoWriter):
                                vid_writer.release()  # release previous video writer

                            fps = vid_cap.get(cv2.CAP_PROP_FPS)
                            w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                            h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                            # 向视频写入帧（cv2.VideoWriter_fourcc）
                            vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mpv4'), fps, (w, h))

                        vid_writer.write(im0)

        if save_txt or save_img:
            print('Results saved to %s' % os.getcwd() + os.sep + out)
            if platform == 'darwin':  # MacOS
                os.system('open ' + out + ' ' + save_path)


        self.face.moveToThread(self.facethread)
        self.face.finish_signal.connect(self.facethread.quit)
        self.facethread.started.connect(self.face.facerec_pic)
        self.facethread.start()
        print("识别线程开启")
        print('Done. (%.3fs)' % (time.time() - t0))


    # 打开关闭摄像头控制
    def slotCameraButton(self):
        if self.timer_camera.isActive() == False:

    #打开摄像头并显示图像信息
            self.openCamera1()
        else:
    # 关闭摄像头并清空显示信息
            self.closeCamera()

    # 打开摄像头
    def openCamera1(self):
        flag = self.cap.open(self.CAM_NUM)

        if flag == False:
            msg = QMessageBox.Warning(self, u'Warning', u'请检测相机与电脑是否连接正确',
                                  buttons=QMessageBox.Ok,
                                  defaultButton=QMessageBox.Ok)
        else:
            self.timer_camera.start(30)
            self.cameraButton.setText('关闭摄像头')

    # 关闭摄像头
    def closeCamera(self):
        self.timer_camera.stop()

        self.cap.release()
        self.cameraLabel.clear()
        self.cameraButton.setText('打开摄像头')

    # #人脸识别模块
    # def face(self):
    #     face_rec.facerec()
    #
    # def collect(self):
    #     face_rec.collect_face()


class FaceCollectionWindow(QDialog, Ui_faceCollection):
    global faceImageName
    returnSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(FaceCollectionWindow, self).__init__(parent)
        QDialog.__init__(self)
        self.setupUi(self)

        # self.slot_init()

    # self.cameraButton.clicked.connect(self.slotCameraButton)
    # def slot_init(self):
    #     self.toolButton.clicked.connect(self.openImage())

    def openImage1(self):
        global faceImageName
        try:

            faceImageName, _ = QFileDialog.getOpenFileName(self, '打开文件', '/', 'Image files (*.jpg *.gif *.png)')

            self.label.setPixmap(QPixmap(faceImageName).scaled(self.label.width(), self.label.height()))
        except:
            self.label.setText("打开文件失败，可能是文件类型错误")

    def submit(self):
        print(faceImageName)
        self.save_event(faceImageName)

    def save_event(self, faceImageName):
        rename = self.lineEdit.text()
        output_dir = "img"  # 文件路径
        try:
            # 是否有这个路径
            if not os.path.exists(output_dir):
                # 创建路径
                os.makedirs(output_dir)
            # 获得图片后缀
            file_suffix = os.path.splitext(faceImageName)[-1]
            print(file_suffix)
            # 拼接图片名（包含路径）
            filename = '{}{}{}{}'.format(output_dir, os.sep, rename, file_suffix)
            print(type(filename))
            img = self.label.pixmap().toImage()
            # 保存到文件夹中
            img.save(filename)
            faceImageName = '0.jpg'
        except IOError as e:
            print("IOError")
        except Exception as e:
            print("Exception")

    def collect(self):
        global faceImageName
        faceImageName  = '0.jpg'
        self.collect_face()

    def collect_face(self):
        output_dir = 'img'
        i = 1
        cap = cv2.VideoCapture(0)
        winname = "capture"
        while 1:
            ret, frame = cap.read()
            cv2.imshow('cap', frame)
            flag = cv2.waitKey(1)
            # if cv2.getWindowProperty(winname, cv2.WND_PROP_AUTOSIZE) < 1:
            #     break
            if flag == 13:
                # 按下回车键
                # output_path = os.path.join(output_dir, "%04d.jpg" % i)
                # cv2.imwrite(output_path, frame)
                # i += 1
                show = cv2.resize(frame, (480, 320))
                show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
                showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                self.label.setPixmap(QPixmap.fromImage(showImage).scaled(self.label.width(), self.label.height()))
                break
            if flag == 27:
                # 按下ESC键
                break
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = CameraPageWindow()# 这是原py中的类,因人而异哦
    faceCollection = FaceCollectionWindow()
    btn = ui.toolButton_3
    btn.clicked.connect(faceCollection.show)

    ui.show()
    sys.exit(app.exec_())