import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox

from subprocess import call
import requests
import socket
import pickle
import sys
import time

HEADER_LENGTH = 10


class UI_AddFriend(QtWidgets.QMainWindow):
    def __init__(self, id, serverIP):
        #kết nối với server để gọi ds fr
        super().__init__()
        self.id = id
        self.serverIP = serverIP
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.serverIP, 8082))

        self.list = []

        message = {}
        message["method"] = "showall"
        message["id"] = self.id
        message["ip"] = socket.gethostbyname(socket.gethostname())

        msg = pickle.dumps(message)
        msg = bytes(f"{len(msg):<{HEADER_LENGTH}}", "utf-8") + msg

        client_socket.send(msg)

        data = client_socket.recv(2048)
        mes = data.decode()
        print(mes)
        print(type(mes))
        
        if (mes != "[]"):
            arr = mes.split("], [")
            arr[0] = arr[0][2:]
            arr[-1] = arr[-1][:-2]
            
            for i in range(len(arr)):
                arr[i] = arr[i].split(', ')
                for ii in range(4):
                    arr[i][ii] = arr[i][ii].strip("\"")
                arr[i][0] = i
                
            for user in arr:
                self.list.append(user)

        # data_res = pickle.loads(data)
        # print(data_res)
        # print(type(data_res))

        client_socket.close()

        self.render()

    def render(self):
        self.setupUi(self, self.list)
        self.show()

    def setupUi(self, Addfriend, List):
        Addfriend.setObjectName("Addfriend")
        Addfriend.resize(532, 331)
        self.Scroll_Area = QtWidgets.QScrollArea(Addfriend)
        self.Scroll_Area.setGeometry(QtCore.QRect(0, 0, 531, 331))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Scroll_Area.sizePolicy().hasHeightForWidth())
        self.Scroll_Area.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Scroll_Area.setPalette(palette)
        self.Scroll_Area.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Scroll_Area.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Scroll_Area.setStyleSheet("#Scroll_Area{\n"
                                       "    border: 1px solid black;\n"
                                       "    background-color: rgb(240,248,255);\n"
                                       "}")
        self.Scroll_Area.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.Scroll_Area.setWidgetResizable(True)
        self.Scroll_Area.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignJustify)
        self.Scroll_Area.setObjectName("Scroll_Area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(
            QtCore.QRect(0, 0, 529, 329))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.scrollAreaWidgetContents_2.setPalette(palette)
        self.scrollAreaWidgetContents_2.setObjectName(
            "scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.outer_frameList=[]
        self.addList = []
        self.name = []
        self.OnOffList = []
        self.displayUI()

        self.Scroll_Area.setWidget(self.scrollAreaWidgetContents_2)
        self.Scroll_Area.raise_()
        self.retranslateUi(Addfriend)
        QtCore.QMetaObject.connectSlotsByName(Addfriend)

    def retranslateBt(self, arr):
        _translate_ = QtCore.QCoreApplication.translate
        self.addList[arr[0]].setText(_translate_("Addfriend", "Add"))
        if (arr[1] == ''):
            self.name[arr[0]].setText(_translate_(
                "Addfriend", "Chưa có user nào đăng ký"))
        else:
            self.name[arr[0]].setText(_translate_("Addfriend", arr[1]))

        self.OnOffList[arr[0]].setText(_translate_("Addfriend", "Online"))

    def retranslateUi(self, Addfriend):
        _translate = QtCore.QCoreApplication.translate
        Addfriend.setWindowTitle(_translate("Addfriend", "Add some chads!"))
        self.Add.setText(_translate("Addfriend", "Add"))

    def addfriend(self, arr):
        #kết nối với server để add bạn theo friend_name
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.serverIP, 8082))

        message = {}
        message["method"] = "addfriend"
        message["id"] = self.id
        message["friend_name"] = arr[1]

        msg = pickle.dumps(message)
        msg = bytes(f"{len(msg):<{HEADER_LENGTH}}", "utf-8") + msg

        client_socket.send(msg)
        
        data = client_socket.recv(2048)
        mes = data.decode()
        
        print(mes)
        print(type(mes))
        client_socket.close()
        self.refresh()

    def refresh(self):
        #kết nối với server để gọi lại ds fr (y chang __init__)
        for outer_frame in self.outer_frameList:
            outer_frame.setParent(None)
        self.outer_frameList.clear()
        self.addList.clear()
        self.name.clear()
        self.OnOffList.clear()

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.serverIP, 8082))

        self.list=[]

        message = {}
        message["method"] = "showall"
        message["id"] = self.id
        message["ip"] = socket.gethostbyname(socket.gethostname())

        msg = pickle.dumps(message)
        msg = bytes(f"{len(msg):<{HEADER_LENGTH}}", "utf-8") + msg

        client_socket.send(msg)

        data = client_socket.recv(2048)
        mes = data.decode()
        print(mes)
        print(type(mes))
        
        if (mes != "[]"):
            arr = mes.split("], [")
            arr[0] = arr[0][2:]
            arr[-1] = arr[-1][:-2]
            
            for i in range(len(arr)):
                arr[i] = arr[i].split(', ')
                for ii in range(4):
                    arr[i][ii] = arr[i][ii].strip("\"")
                arr[i][0] = i
                
            for user in arr:
                self.list.append(user)

        # data_res = pickle.loads(data)
        # print(data_res)
        # print(type(data_res))

        client_socket.close()

        self.displayUI()

    def displayUI(self):
        List = self.list
        for i in range(len(List)):
            arr = List[i]
            Outer_frame = QtWidgets.QFrame(
                self.scrollAreaWidgetContents_2)
            sizePolicy = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                Outer_frame.sizePolicy().hasHeightForWidth())
            Outer_frame.setSizePolicy(sizePolicy)
            Outer_frame.setMinimumSize(QtCore.QSize(343, 100))
            palette = QtGui.QPalette()
            Outer_frame.setPalette(palette)
            Outer_frame.setAutoFillBackground(True)
            Outer_frame.setStyleSheet("background-color: rgb(#aaaaff);\n"
                                           "")
            Outer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            Outer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            Outer_frame.setObjectName("Outer_frame" + str(arr[0]))

            # Background
            self.Layer = QtWidgets.QLabel(Outer_frame)
            self.Layer.setEnabled(True)
            self.Layer.setGeometry(QtCore.QRect(0, 0, 511, 100))
            self.Layer.setMinimumSize(QtCore.QSize(0, 100))
            palette = QtGui.QPalette()
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Active,
                             QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive,
                             QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Inactive,
                             QtGui.QPalette.Window, brush)
            brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled,
                             QtGui.QPalette.Base, brush)
            brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            palette.setBrush(QtGui.QPalette.Disabled,
                             QtGui.QPalette.Window, brush)
            self.Layer.setPalette(palette)
            self.Layer.setAutoFillBackground(True)
            self.Layer.setStyleSheet("#Layer{\n"
                                     "    background-color: rgb(#aaaaff);\n"
                                     "}")
            self.Layer.setText("")
            self.Layer.setObjectName("Layer" + str(arr[0]))

            # Button frame
            self.Button_frame = QtWidgets.QFrame(Outer_frame)
            self.Button_frame.setGeometry(QtCore.QRect(330, 30, 141, 51))
            self.Button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Button_frame.setObjectName("Button_frame" + str(arr[0]))
            self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.Button_frame)
            self.horizontalLayout_31.setObjectName(
                "horizontalLayout_31" + str(arr[0]))

            self.Add = QtWidgets.QPushButton(self.Button_frame)
            self.Add.setObjectName(str(arr[0]))
            self.Add.clicked.connect(lambda x,ip=arr:self.addfriend(ip))
            self.horizontalLayout_31.addWidget(self.Add)

            # Information
            self.Info = QtWidgets.QFrame(Outer_frame)
            self.Info.setGeometry(QtCore.QRect(10, 10, 200, 81))
            self.Info.setMinimumSize(QtCore.QSize(200, 0))
            self.Info.setStyleSheet("#Info{\n"
                                    "    opacity: 0;\n"
                                    "}")
            self.Info.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Info.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Info.setObjectName("Info" + str(arr[0]))

            self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.Info)
            self.horizontalLayout_32.setSpacing(5)
            self.horizontalLayout_32.setObjectName(
                "horizontalLayout_32" + str(arr[0]))

            # Avatar
            self.ImageReal = QtWidgets.QLabel(self.Info)
            self.ImageReal.setMinimumSize(QtCore.QSize(50, 40))
            self.ImageReal.setText("")
            if (arr[3] != ''):
                image = QImage()
                image.loadFromData(requests.get(arr[3]).content)
                self.ImageReal.setPixmap(QPixmap(image))
                self.ImageReal.setScaledContents(True)
            else:
                self.ImageReal.setStyleSheet(
                    "border-image: url(./image/addfriend.png)"
                )
            self.ImageReal.setObjectName("ImageReal" + str(arr[0]))
            self.ImageReal.raise_()
            self.horizontalLayout_32.addWidget(self.ImageReal)

            # Info Box
            self.InfoBox = QtWidgets.QFrame(self.Info)
            sizePolicy = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                self.InfoBox.sizePolicy().hasHeightForWidth())
            self.InfoBox.setSizePolicy(sizePolicy)
            self.InfoBox.setMinimumSize(QtCore.QSize(100, 40))
            self.InfoBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.InfoBox.setFrameShadow(QtWidgets.QFrame.Raised)
            self.InfoBox.setObjectName("InfoBox" + str(arr[0]))

            ## Name and Status
            self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.InfoBox)
            self.verticalLayout_12.setContentsMargins(-1, 2, -1, 2)
            self.verticalLayout_12.setObjectName(
                "verticalLayout_12" + str(arr[0]))
            Name = QtWidgets.QLabel(self.InfoBox)
            Name.setObjectName("Name" + str(arr[0]))
            self.verticalLayout_12.addWidget(Name)

            self.Status = QtWidgets.QFrame(self.InfoBox)
            self.Status.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.Status.setFrameShadow(QtWidgets.QFrame.Raised)
            self.Status.setObjectName("Status" + str(arr[0]))

            self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.Status)
            self.horizontalLayout_33.setContentsMargins(9, 9, 9, -1)
            self.horizontalLayout_33.setSpacing(5)
            self.horizontalLayout_33.setObjectName(
                "horizontalLayout_33" + str(arr[0]))

            self.IMG = QtWidgets.QLabel(self.Status)
            self.IMG.setAlignment(QtCore.Qt.AlignCenter)
            self.IMG.setObjectName("IMG" + str(arr[0]))
            self.horizontalLayout_33.addWidget(self.IMG)

            self.OnOff = QtWidgets.QLabel(self.Status)
            self.OnOff.setObjectName("OnOff" + str(arr[0]))

            self.horizontalLayout_33.addWidget(self.OnOff)
            self.verticalLayout_12.addWidget(self.Status)
            self.horizontalLayout_32.addWidget(self.InfoBox)
            self.verticalLayout_2.addWidget(Outer_frame)
            self.outer_frameList.append(Outer_frame)
            self.addList.append(self.Add)
            self.name.append(Name)
            self.OnOffList.append(self.OnOff)
            self.retranslateBt(arr)
    
    def closeEvent(self,event):
        print("exit")



