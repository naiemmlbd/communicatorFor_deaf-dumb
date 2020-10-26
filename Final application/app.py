# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
import sys
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 601, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(35, 80, 721, 381))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 470, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.speechtoText)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 470, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.signtoText)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Communicator for Deaf and Dumb"))
        self.pushButton.setText(_translate("MainWindow", "Speech to Text"))
        self.pushButton_2.setText(_translate("MainWindow", "Sign to Text"))

    def speechtoText(self):

        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            print("Please say something")

            audio = r.listen(source)

            print("Please wait .... ")

            try:
                self.textBrowser.setText(r.recognize_google(audio, language = 'en-US'))


            except Exception as e:
                print("Error :  " + str(e))

    def signtoText(self):
        model = load_model('trained_model.h5')

        img_dim = 128

        class_labels = [
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z',
        ]

        cap = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX

        text = ""
        word = ""
        count_same_frame = 0

        #####
        temp=0
        previouslabel=None
        previousText=" "
        label = None

        while True:

            ret, frame = cap.read()

            # cv2.rectangle(frame, (900, 100), (1300, 500), (255, 0, 0),
            #               3)  # bounding box which captures ASL sign to be detected by the system
            # img1 = frame[100:500, 900:1300]
            # img_ycrcb = cv2.cvtColor(img1, cv2.COLOR_BGR2YCR_CB)
            # blur = cv2.GaussianBlur(img_ycrcb, (11, 11), 0)
            # skin_ycrcb_min = np.array((0, 138, 67))
            # skin_ycrcb_max = np.array((255, 173, 133))
            # mask = cv2.inRange(blur, skin_ycrcb_min,
            #                    skin_ycrcb_max)  # detecting the hand in the bounding box using skin detection

            cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)
            roi = frame[100:500, 100:500]
            img = cv2.resize(roi, (img_dim, img_dim))
            img_ycrcb = cv2.cvtColor(roi, cv2.COLOR_BGR2YCR_CB)
            blur = cv2.GaussianBlur(img_ycrcb, (11, 11), 0)
            skin_ycrcb_min = np.array((0, 138, 67))
            skin_ycrcb_max = np.array((255, 173, 133))
            mask = cv2.inRange(blur, skin_ycrcb_min,
                            skin_ycrcb_max)  # detecting the hand in the bounding box using skin detection

            img = image.img_to_array(img)
            img = np.expand_dims(img, axis=0)
            img = img.astype('float32')/255
            label = np.argmax(model.predict(img))
            color = (0, 0, 255)

            if (label != None):
                if (temp == 0):
                    previouslabel = class_labels[label]
                if previouslabel == class_labels[label]:
                    previouslabel = class_labels[label]
                    temp += 1
                else:
                    temp = 0
                if (temp == 40):
                    if (class_labels[label] == 'P'):
                        label = " "
                    text = text + class_labels[label]
                    if (class_labels[label] == 'Q'):
                        words = re.split(" +", text)
                        words.pop()
                        text = " ".join(words)
                # text=previousText
                    print (text)

                cv2.putText(frame, class_labels[label], (50, 150), font, 8, (0, 125, 155),
                            2)  # displaying the predicted letter on the main screen
                cv2.putText(frame, text, (50, 450), font, 3, (0, 0, 255), 2)

            cv2.imshow('Video', frame)
            cv2.imshow('Mask', mask)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

