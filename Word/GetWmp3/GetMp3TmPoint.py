
import PyQt5.QtWidgets
import PyQt5.QtMultimedia
import PyQt5.QtCore
import sys
import PyQt5
from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import (QWidget, QToolTip,QPushButton,QMessageBox, QApplication,QLabel)
from PyQt5.QtGui import QFont

# app = PyQt5.QtWidgets.QApplication(sys.argv)
# url = PyQt5.QtCore.QUrl.fromLocalFile("class.mp3")
# content = PyQt5.QtMultimedia.QMediaContent(url)
# player = PyQt5.QtMultimedia.QMediaPlayer()
# player.setMedia(content)
# Sound_level=10
# player.setVolume(Sound_level)
# player.play()
# sys.exit(app.exec())



class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.FileName=''
        #========Size Parameters========
        self.TOPL=300
        self.TOPT=300
        self.LENGTH=1000
        self.HIGHT=600

        self.HDiv=5
        self.LDiv=5
        #===============================
        #=========Components============
        btn1 = QPushButton('SaveBegin', self)
        btn2 = QPushButton('SaveEnd', self)
        TE = QTextEdit()
        # self.lbl = QLabel("Path",self)
        # self.qle = QLineEdit(self)
        #===============================
        #=========Locate Components=====
        # btn1.resize(self.LSize(1.3),self.HSize(1/2))
        # btn1.move(self.LSize(1/2),self.HSize(1))
        
        #实例化垂直布局
        layout=QVBoxLayout()
        #相关控件添加到垂直布局中
        layout.addWidget(TE)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setLayout(layout)

        
        
        self.setGeometry(self.TOPL, self.TOPT, self.LENGTH, self.HIGHT)

        # self.setWindowTitle('Txt & Wav')
        #===============================
        #=========Set Connection========
        # btn1.clicked.connect(self.Onbtn1Clicked)
        # btn2.clicked.connect(self.Onbtn2Clicked)
        # btn3.clicked.connect(self.Onbtn3Clicked)
        # btn4.clicked.connect(self.Onbtn4Clicked)
        #=========Show==================
        self.show()
        #===============================

    def HSize(self,Scale=1.0):
        return int(Scale*self.HIGHT/self.HDiv)
    def LSize(self,Scale=1.0):
        return int(Scale*self.LENGTH/self.LDiv)
        
    
    # def Onbtn1Clicked(self):
    #     msg_box = QMessageBox
    #     self.FileName=self.qle.text()
    #     if self.FileName != '':
    #         filter.filter(self.FileName)
    #         prowav.CreatWav(self.FileName[:-4]+'AF.TXT')
    #         QMessageBox.information(self, "提示"  ,"Save Successfully!",  QMessageBox.Ok)
    # def Onbtn2Clicked(self):
    #     self.FileName=self.qle.text()
    #     if self.FileName != '':
    #         filter.filter(self.FileName,fsN=37037)
    #         prowav.PlayfromRbTxt(self.FileName[:-4]+'AF.TXT')
    # def Onbtn3Clicked(self):
    #     self.openfile_name = QFileDialog.getOpenFileName(self,'选择文件','','Excel files(*.txt)')
    #     self.qle.setText(self.openfile_name[0])
    #     # self.lbl.setText("Path")
    #     # self.lbl.resize(self.LSize(1/2),self.HSize(1/2))
    #     # self.lbl.move(self.LSize(1/2),self.HSize(3))
    # def Onbtn4Clicked(self):
    #     self.FileName=self.qle.text()
    #     if self.FileName != '':
    #         prowav.PlayfromRbTxt(self.FileName)
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
