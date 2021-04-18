import threading
import time
import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from playsound import playsound
import json
import os

with open('character.json','r',encoding='utf-8') as f:
    js=json.load(f)

class Window(QWidget):
    def __init__(self,parent=None,**kwargs):
        super(Window,self).__init__(parent)
        self.initUI()#用initUI函数创建窗口

    def initUI(self):
        
        self.setWindowFlags(Qt.WindowStaysOnTopHint|Qt.FramelessWindowHint)#设置窗口置顶、去边框
        self.setAttribute(Qt.WA_TranslucentBackground,True)#窗体背景透明
        #self.setScaledContents(True)
        self.repaint()
        self.show()
        #组件设置
        self.label= QLabel(self)
        self.label.setScaledContents(True)
        self.resize(700,750)#设置窗口的位置，大小
        self.label.setGeometry(0,0,517,483)
        self.label.show()

        self.iconpath = js['list1'][0]
        quit_action = QAction('退出', self, triggered=self.quit)
        quit_action.setIcon(QIcon(self.iconpath))
        self.tray_icon_menu = QMenu(self)
        self.tray_icon_menu.addAction(quit_action)
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(self.iconpath))
        self.tray_icon.setContextMenu(self.tray_icon_menu)
        self.tray_icon.show()

        self.images_path=js['list1']

        #动作参数
        self.is_running_action=False
        self.action_images=[]
        self.action_pointer=0
        self.action_max_len=0
        self.n=0

        self.timer = QTimer()
        self.timer.timeout.connect(self.Act)
        self.timer.start(30)

#鼠标点击事件
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            e.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            self.action_pointer=self.action_max_len
            if self.n!=3:
                self.n=1
            thread=threading.Thread(target=self.voice)
            thread.start()

    def mouseDoubleClickEvent(self, e):
        self.childwind()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False
            self.setCursor(QCursor(Qt.ArrowCursor))

    def mouseMoveEvent(self, e):
        if Qt.LeftButton and self.m_drag:
            self.move(e.globalPos() - self.m_DragPosition)
            e.accept()

#显示当前图片
    def setImage(self,a):
        png=QPixmap()#.scaled(self.label.width(), self.label.height())
        png.load(a)
        self.label.setPixmap(png)
        
#动作图片
    def Act(self):
        if not self.is_running_action:
            self.is_running_action=True
            self.action_images=self.images_path
            self.action_pointer=0
            self.action_max_len=len(self.action_images)
        self.run()
#逐帧传递
    def run(self):
        if self.action_pointer==self.action_max_len:
            self.is_running_action=False
            self.action_pointer=0
            self.action_max_len=0
            with open('character.json','r',encoding='utf-8') as f:
                js=json.load(f)
            #self.action_images=self.images_path
            if self.n!=0:
                self.actions()
                self.n=0
            else:
                self.images_path=js['list1']
        self.setImage(self.action_images[self.action_pointer])
        self.action_pointer += 1

    def childwind(self):
        self.cd=QWidget()
        self.cd.setGeometry(100,100,400,200)
        self.cd.show()
        self.cd.bt1=QPushButton(self.cd)
        self.cd.bt1.setGeometry(70,80,81,41)
        self.cd.bt1.setText("aaaa")
        self.cd.bt1.show()
        self.cd.bt1.clicked.connect(self.whichbtn)
        self.cd.bt2=QPushButton(self.cd)
        self.cd.bt2.setGeometry(10,80,81,41)
        self.cd.bt2.setText("music")
        self.cd.bt2.show()
        self.cd.bt2.clicked.connect(self.do)
        #layout.addWidget(self.cd.bt1)

    def whichbtn(self):
        QDesktopServices.openUrl(QUrl("https://www.bilibili.com"))
        self.n=2
        self.action_pointer=self.action_max_len
        thread=threading.Thread(target=self.voice)
        thread.start()

    def actions(self):
        if self.n==1:
            with open('character.json','r',encoding='utf-8') as f:
                js=json.load(f)
            self.images_path=js['list2']
            #playsound('dusk voice\dusk_touch.wav')
        elif self.n==2:
            self.images_path=this_path.list3
        elif self.n==3:
            self.images_path=this_path.list4

    def voice(self):
        with open('character.json','r',encoding='utf-8') as f:
            js=json.load(f)
        voice_path=js['list3'][0]
        if self.n==1:
            playsound(voice_path)
            time.sleep(1)
        elif self.n==2:
            voice_path=random.choice(['dusk voice\dusk_start1.wav','dusk voice\dusk_start2.wav'])
            playsound(voice_path)
            time.sleep(1)

    def do(self):
        self.action_pointer=self.action_max_len
        self.n=3
        thread=threading.Thread(target=self.music)
        thread.start()

    def music(self):
        self.n=3
        playsound('dusk music\dusk_music.mp3')
        time.sleep(1)

    def quit(self):
        self.close()
        self.exit()

#def timeoutvoice():
#    playsound('dusk voice\dusk_lieidle.wav')

'''class TheThreading(threading.Thread):

    def __init__(self,name=None):
        threading.Thread.__init__(self,name=name)'''

##if __name__=='__main__':
##    app = QApplication(sys.argv)
##    petwindow = Window()
##    petwindow.show()
##    timer=threading.Timer(interval=180,function=timeoutvoice)
##    timer.start()
##    sys.exit(app.exec_())
##    


