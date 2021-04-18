from PyQt5.QtWidgets import *
import this_path
import json
import sys
import os
import DESKPETDEMO2

class Appwindow(QWidget):
    def __init__(self,parent=None,**kwargs):
        super(Appwindow,self).__init__(parent)
        self.initUI()
        self.n=0

    def initUI(self):
        self.setGeometry(200,200,650,400)
        self.bt1=Petbutton(self)
        self.bt1.setGeometry(50,50,100,100)
        self.bt1.setText('dusk')
        self.bt1.show()
        self.bt1.clicked.connect(self.choice)
        self.bt2=Petbutton(self)
        self.bt2.setGeometry(200,50,100,100)
        self.bt2.setText('rosmon')
        self.bt2.show()
        self.bt2.clicked.connect(self.choice)
        self.bt3=Petbutton(self)
        self.bt3.setGeometry(350,50,100,100)
        self.bt3.setText('dusk')
        self.bt3.show()
        self.bt3.clicked.connect(self.acted)
        self.bt4=Petbutton(self)
        self.bt4.setGeometry(500,50,100,100)
        self.bt4.setText('dusk')
        self.bt4.show()
        self.bt4.clicked.connect(self.acted)

    def acted(self):
        #app = QApplication(sys.argv)
        #sys.exit(app.exec_())
        self.pet=DESKPETDEMO2.Window()
        self.pet.show()

    def choice(self):
        sender = self.sender()
        c_dict={}
        idpath=os.getcwd()
        if sender.text()=='dusk':
            list_relax=this_path.image_path(idpath+'\\character\\dusk\\dusk relax\\')
            list_interact=this_path.image_path(idpath+'\\character\\dusk\\dusk interact\\')
            list_voice=this_path.image_path('.\\dusk voice\\')
        elif sender.text()=='rosmon':
            list_relax=this_path.image_path(idpath+'\\character\\rosmon\\rosmon relax\\')
            list_interact=this_path.image_path(idpath+'\\character\\rosmon\\rosmon interact\\')
            list_voice=this_path.image_path('.\\rosmon voice\\')

        c_dict['list1']=list_relax
        c_dict['list2']=list_interact
        c_dict['list3']=list_voice
        with open('character.json','w',encoding='utf-8') as f:
            json.dump(c_dict,f)

        self.acted()

class Petbutton(QPushButton):
    def charater(self):
        if self==bt1:
            list_relax=this_path.image_path(idpath+'\\character\\dusk\\dusk relax\\')
            list_interact=this_path.image_path(idpath+'\\character\\dusk\\dusk interact\\')
        elif self==bt2:
            list_relax=this_path.image_path(idpath+'\\character\\ftrtal\\ftrtal idle\\')
            list_interact=this_path.image_path(idpath+'\\character\\ftrtal\\ftrtal attack\\')
        c_dict['list1']=list_relax
        c_dict['list2']=list_interact
        with open('character.json','w',encoding='utf-8') as f:
            json.dump(c_dict,f)
    #self.charater


        
if __name__=='__main__':
    app = QApplication(sys.argv)
    apppet=Appwindow()
    apppet.show()
    sys.exit(app.exec_())


