import threading
import socket
import sys
import time
from tkinter import filedialog
import requests
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QThread, pyqtSignal as Signal, pyqtSlot as Slot
from PyQt5.QtGui import QImage,QPixmap

from listener import *

    

class Connection(QtWidgets.QMainWindow):
    startCatching = Signal(bool)
    rmvConn = Signal(str)

    def __init__(self, arr, conn, client):
        super().__init__()
        self.sendingData = False
        self.cilentSocket = conn
        self.arr = arr
        self.client = client

        #tạo thread p2p cho tin nhắn
        self.catcher = Catcher(self.cilentSocket)
        self.catchThread = QThread()
        self.catcher.moveToThread(self.catchThread)

        self.catcher.shutdown.connect(self.close)
        self.catcher.catchMessage.connect(self.displayMsg)
        self.startCatching.connect(self.catcher.catchMsgWrapper)
        self.catcher.dataDone.connect(self.completeData)
        self.catcher.dataReceived.connect(self.dataRes)

        self.catchThread.start()
        self.startCatching.emit(True) #luôn mở lại catchMsg sau mỗi lệnh

    def dataRes(self, name):
        print("Relistening...")
        self.displayMsg((f"Received file {name}", 2))
        self.startCatching.emit(True)    

    #############################################################################
    ##################################   UI   ###################################
    #############################################################################
    
    def render(self):
        self.setupUi(self.arr)
        self.show()
        if (self.client == 1):
            self.cilentSocket.send("#CHAT#".encode())
    def setupUi(self, arr):
        self.chat=[]
        self.setObjectName("MainChat")
        self.resize(730, 700)
        self.setStyleSheet("background-color: rgb(240,248,255);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.avatar = QtWidgets.QLabel(self.centralwidget)
        self.avatar.setGeometry(QtCore.QRect(570, 30, 150, 150))
        image = QImage()
        image.loadFromData(requests.get(arr[3]).content)
        self.avatar.setPixmap(QPixmap(image))
        self.avatar.setScaledContents(True)
        self.avatar.setObjectName("avatar")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 30, 530, 531))
        self.textBrowser.setStyleSheet("background-color: white;")
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 570, 530, 71))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 590, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: blue;\n"
"color: white;")
        self.pushButton.setObjectName("pushButton")
        self.IP = QtWidgets.QLabel(self.centralwidget)
        self.IP.setGeometry(QtCore.QRect(570, 190, 151, 31))
        self.IP.setObjectName("IP")
        self.IP_2 = QtWidgets.QLabel(self.centralwidget)
        self.IP_2.setGeometry(QtCore.QRect(570, 240, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.IP_2.setFont(font)
        self.IP_2.setObjectName("IP_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(40, 40, 511, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("#scrollArea{\n"
                                      "    background-color:rgba(0,0,0,100);\n"
                                      "}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 509, 509))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.File_Send = QtWidgets.QPushButton(self.centralwidget)
        self.File_Send.setGeometry(QtCore.QRect(490, 660, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.File_Send.setFont(font)
        self.File_Send.setStyleSheet("background-color: blue;\n"
                                     "color: white;")
        self.File_Send.setObjectName("File_Send")
        self.File_Send.clicked.connect(self.sendFile)
        self.Path = QtWidgets.QLineEdit(self.centralwidget)
        self.Path.setGeometry(QtCore.QRect(40, 660, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Path.setFont(font)
        self.Path.setText("")
        self.Path.setMaxLength(60)
        self.Path.setObjectName("Path")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(arr)
        QtCore.QMetaObject.connectSlotsByName(self)

        #############
        #Setup send button
        #############
        self.pushButton.clicked.connect(self.sendLine)
    def retranslateUi(self, arr):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainChat", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainChat", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainChat", "SEND"))
        self.IP.setText(_translate("MainChat", arr[2]))
        self.IP_2.setText(_translate("MainChat", arr[1]))
        self.File_Send.setText("File")

    ##########################################
    #############  Sending Text   ############
    ##########################################
    
    def sendLine(self):
        if (self.lineEdit.text() != ""):
            sentence = "#CONTENT#" + self.lineEdit.text().strip()
            self.cilentSocket.send(sentence.encode()) #bắn qua bên kia qua socket
            self.displayMsg((self.lineEdit.text(), 1))
            self.lineEdit.setText("")


    ##########################################
    #############  Sending Data   ############
    ##########################################
    startDataSending = Signal(bool)
    startSendingDataBody = Signal(bool)
    def sendFile(self):
        self.sendingData = True
        self.pushButton.setEnabled(False)
        self.File_Send.setEnabled(False)

        filetypes = (
            ('All files', '*.*'),
            ('text files', '*.txt')
        )
        filename = filedialog.askopenfilename(title='Open a file', initialdir='/', filetypes = filetypes)
        self.Path.setText(filename.replace("/", chr(92)))
        print(self.Path.text())

        #tạo thread cho file
        self.dataLink = DataLink(self.cilentSocket, self.Path.text())
        self.dataThread = QThread()
        self.dataLink.moveToThread(self.dataThread)

        self.startDataSending.connect(self.dataLink.send)
        self.startSendingDataBody.connect(self.dataLink.sendBody)
        self.catcher.fileOK.connect(self.sendContentFile)
        
        self.displayMsg(("Sending file from " + self.Path.text(), 2))
        self.dataThread.start()
        print("Sending...")
        self.startDataSending.emit(True)
        

    def sendContentFile(self):
        print("Commence file transfering...")
        self.startSendingDataBody.emit(True)
        self.startCatching.emit(True)

    def completeData(self):
        self.sendingData = False
        self.pushButton.setEnabled(True)
        self.File_Send.setEnabled(True)

        self.dataThread.exit()

        self.Path.setText("")
        self.startCatching.emit(True)
        print("File transfering Completed!")

    def displayMsg(self, group):
        sentence = group[0]
        user = group[1]
        newLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(newLabel.sizePolicy().hasHeightForWidth())
        newLabel.setSizePolicy(sizePolicy)
        newLabel.setMinimumSize(QtCore.QSize(0, 25))
        if(user == 1):
            newLabel.setStyleSheet("background-color: turquoise")
        elif (user == 0):
            newLabel.setStyleSheet("background-color: pink")
        elif (user == 2):
            newLabel.setStyleSheet("background-color: gray")
        newLabel.setObjectName("label")
        self.verticalLayout.addWidget(newLabel)
        _translate = QtCore.QCoreApplication.translate
        newLabel.setText(_translate("MainChat", sentence))
        self.chat.append(newLabel)

        if(user == 0):
            self.startCatching.emit(True)


    ##########################################
    #############  Clean Closing  ############
    ##########################################
    @Slot(str)    
    def signalRmvConn(self):
        self.rmvConn.emit(self.arr[2])

    def closeEvent(self, event):
        try:
            self.cilentSocket.send("#QUIT#".encode())
        except:
            self.signalRmvConn()
            time.sleep(1)
            self.catchThread.exit()
            time.sleep(1)
        else:
            event.ignore()

