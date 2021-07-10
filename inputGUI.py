from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
import sys

class Window3(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('手动就手动')
        self.setIcon()

        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        text, okPressed = QtWidgets.QInputDialog.getText(self,
                                                         '潮流方式名',
                                                         '潮流方式名称:',
                                                         QtWidgets.QLineEdit.Normal)
        text2,okPressed2 = QtWidgets.QInputDialog.getText(self,
                                                          '工程名',
                                                          '工程名称:',
                                                          QtWidgets.QLineEdit.Normal)
        print('(POWERFLOW, CASEID='+text+', PROJECT='+text2+')')
        text3, okPressed3 = QtWidgets.QInputDialog.getText(self,
                                                           'PQ分解法次数',
                                                           'PQ分解法次数:',
                                                           QtWidgets.QLineEdit.Normal)
        text4, okPressed4 = QtWidgets.QInputDialog.getText(self,
                                                           '改进牛拉次数',
                                                           '改进牛拉法次数:',
                                                           QtWidgets.QLineEdit.Normal)
        text5, okPressed5 = QtWidgets.QInputDialog.getText(self,
                                                           '牛拉法次数',
                                                           '牛拉法次数:',
                                                           QtWidgets.QLineEdit.Normal)
        print('/SOL_ITER,DECOUPLED=' + text3 + ',CURRENT=' + text4 + ',NEWTON=' + text5 + '\ ')
        text6, okPressed6 = QtWidgets.QInputDialog.getText(self,
                                                           '控制收敛误差吗',
                                                           '若控制请收敛误差输入y'+'\n'+'否则请直接点击OK跳过:',
                                                           QtWidgets.QLineEdit.Normal)
        if text6 == 'y':
            text7, okPressed7 = QtWidgets.QInputDialog.getText(self,
                                                               '节点电压收敛误差',
                                                               '节点电压收敛误差:'+'\n'+'(如果没有特定需求请输入0.0001)',
                                                               QtWidgets.QLineEdit.Normal)
            text8, okPressed8 = QtWidgets.QInputDialog.getText(self,
                                                               '电功率收敛误差',
                                                               '电功率收敛误差'+'\n'+'(如果没有特定需求请填写0.0001):',
                                                               QtWidgets.QLineEdit.Normal)
            text9, okPressed9 = QtWidgets.QInputDialog.getText(self,
                                                               'TX收敛误差',
                                                               'TX收敛误差:'+'\n'+'(如果没有特定需求请填写0.0001)',
                                                               QtWidgets.QLineEdit.Normal)
            text10, okPressed10 = QtWidgets.QInputDialog.getText(self,
                                                                 '无功收敛误差',
                                                                 '无功收敛误差:'+'\n'+'(如果没有特定需求请填写0.0001)',
                                                                 QtWidgets.QLineEdit.Normal)
            text11, okPressed11 = QtWidgets.QInputDialog.getText(self,
                                                                 'OPCUT收敛误差',
                                                                 'OPCUT收敛误差:'+'\n'+'(如果没有特定需求请填写0.0001)',
                                                                 QtWidgets.QLineEdit.Normal)
            print('/TOLERANCE,BUSV='+text7+',AIPOWER='+text8+',TX='+text9+',Q='+text10+',OPCUT='+text11+'\ ')
        text12, okPressed12 = QtWidgets.QInputDialog.getText(self,
                                                             '需要分区输出输入数据吗',
                                                             '若需要分区输出输入数据请输入y'+'\n'+'不需要请输入n:',
                                                             QtWidgets.QLineEdit.Normal)
        if text12 == 'n':
            text13, okPressed13 = QtWidgets.QInputDialog.getText(self,
                                                                 '选择输出内容',
                                                                 '不输(缺省)请输入NONE'+'\n'+'全输出请输入FULL',
                                                                 QtWidgets.QLineEdit.Normal)
            print('/P_INPUT_LIST,'+text13+'\ ')
        if text12 == 'y':
            text14, okPressed14 = QtWidgets.QInputDialog.getText(self,
                                                                 '分区名',
                                                                 '分区名称不输出请输入NONE'+'\n'+'全输出请输入ALL,FULL',
                                                                 QtWidgets.QLineEdit.Normal)
            print('/P_INPUT_LIST,ZONES='+text14+'\ ')
        text15, okPressed15 = QtWidgets.QInputDialog.getText(self,
                                                             '致命性错误',
                                                             '如果存在致命性错误仍要输出' + '\n' + '请输入相关内容:'+'\n'+'按节点字符顺序输出请输入BUS'+'\n'+'按分区顺序顺序输出请输入ZONE'+'\n'+'按区域顺序输出请输入AREA'+'\n'+'否则请直接点击OK跳过',
                                                             QtWidgets.QLineEdit.Normal)
        if text15 != '':
            print('/PARTIAL_LIST='+text15+'\ ')
        text16, okPressed16 = QtWidgets.QInputDialog.getText(self,
                                                             '分区输出潮流计算结果',
                                                             '若需要分区输出潮流计算结果请输入y' + '\n' + '不需要请输入n',
                                                             QtWidgets.QLineEdit.Normal)
        if text16 == 'y':
            text17, okPressed17 = QtWidgets.QInputDialog.getText(self,
                                                                 '输出内容',
                                                                 '内容不输出(缺省)请输入NONE'+'\n'+'全输出请输入FULL',
                                                                 QtWidgets.QLineEdit.Normal)
            print('/P_OUTPUT_LIST,' + text17 + '\ ')
        if text16 == 'n':
            text18, okPressed18 = QtWidgets.QInputDialog.getText(self,
                                                                 '分区名',
                                                                 '分区名称不输出请输入NONE'+'\n'+'全输出请输入ALL,FULL',
                                                                 QtWidgets.QLineEdit.Normal)
            print('/P_OUTPUT_LIST,' + text18 + '\ ')
        text18, okPressed18 = QtWidgets.QInputDialog.getText(self,
                                                             '迭代不收敛',
                                                             '迭代不收敛时:' + '\n' + '输出全部节点请输入a'+'\n'+'不输出任何节点请输入b'+'\n'+'输出部分节点请输入c'+'\n'+'不需要显示请直接点击OK跳过',
                                                             QtWidgets.QLineEdit.Normal)
        if text18 == 'c':
            text19, okPressed19 = QtWidgets.QInputDialog.getText(self,
                                                                 '分区名',
                                                                 '分区名称:'+'\n'+'(默认输入ZONE)',
                                                                 QtWidgets.QLineEdit.Normal)
            print('/PARTIAL_LIST='+text19+'\ ')
        if text18 == 'a':
            print('/PARTIAL_LIST=FULL_LIST\ ')
        if text18 == 'b':
            print('/PARTIAL_LIST=NO_LIST\ ')
        text20, okPressed20 = QtWidgets.QInputDialog.getText(self,
                                                             '潮流结果输出二进制文件名',
                                                             '潮流结果输出二进制文件名称:',
                                                             QtWidgets.QLineEdit.Normal)
        print('/NEW_BASE,FILE='+text20+'.BSE\ ')
        text21, okPressed21 = QtWidgets.QInputDialog.getText(self,
                                                             '指定潮流图的数据文件名',
                                                             '指定潮流图的数据文件名称:',
                                                             QtWidgets.QLineEdit.Normal)
        print('/PF_MAP,FILE+' + text21 + '.MAP\ ')
        print('/NETWORK_DATA\ ')
        QtWidgets.QMessageBox.information(self,
                                          '控制语句',
                                          '结果命令行见',
                                          QtWidgets.QMessageBox.Save)

        grid = QtWidgets.QGridLayout(centralWidget)
        grid.addWidget(okPressed)
        grid.addWidget(okPressed2)
        grid.addWidget(okPressed3)
        grid.addWidget(okPressed4)
        grid.addWidget(okPressed5)
        grid.addWidget(okPressed6)
        grid.addWidget(okPressed7)
        grid.addWidget(okPressed8)
        grid.addWidget(okPressed9)
        grid.addWidget(okPressed10)
        grid.addWidget(okPressed11)
        grid.addWidget(okPressed12)
        grid.addWidget(okPressed13)
        grid.addWidget(okPressed14)
        grid.addWidget(okPressed15)
        grid.addWidget(okPressed16)
        grid.addWidget(okPressed17)
        grid.addWidget(okPressed18)
        grid.addWidget(okPressed19)
        grid.addWidget(okPressed20)
        grid.addWidget(okPressed21)

    def setIcon(self):
        appICON = QIcon('1.ico')
        self.setWindowIcon(appICON)

class Window2(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('项目名称确定')
        self.setIcon()

        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        text,okPressed = QtWidgets.QInputDialog.getText(self, '请输入项目名', '项目名称:', QtWidgets.QLineEdit.Normal)
        if text != '':
            print('(POWERFLOW,CASEID='+text+',PROJECT='+text+'_TEST_SYSTEM)'+'\n'+'/SOL_ITER,DECOUPLED=2,NEWTON=15,OPITM=0\ '+'\n'+'/P_OUTPUT_LIST,ZONES=ALL\ '+'\n'+'/RPT_SORT=ZONE\ '+'\n'+'/NEW_BASE,FILE='+text+'.BSE\ '+'\n'+'/PF_MAP,FILE = '+text+'.MAP\ '+'\n'+'/NETWORK_DATA\ ')
            QtWidgets.QMessageBox.information(self,
                                              '控制语句',
                                              '(POWERFLOW,CASEID='+text+',PROJECT='+text+'_TEST_SYSTEM)'+'\n'+'/SOL_ITER,DECOUPLED=2,NEWTON=15,OPITM=0\ '+'\n'+'/P_OUTPUT_LIST,ZONES=ALL\ '+'\n'+'/RPT_SORT=ZONE\ '+'\n'+'/NEW_BASE,FILE='+text+'.BSE\ '+'\n'+'/PF_MAP,FILE = '+text+'.MAP\ '+'\n'+'/NETWORK_DATA\ ',
                                              QtWidgets.QMessageBox.Save)

        grid = QtWidgets.QGridLayout(centralWidget)
        grid.addWidget(okPressed)

    def setIcon(self):
        appICON = QIcon('1.ico')
        self.setWindowIcon(appICON)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('dat输入控制')
        self.setIcon()

        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        button = QtWidgets.QPushButton('使用默认参考值')
        button.clicked.connect(self.open_new_window)
        button2 = QtWidgets.QPushButton('手动输入')
        button2.clicked.connect(self.open_new_window2)

        grid = QtWidgets.QGridLayout(centralWidget)
        grid.addWidget(button)
        grid.addWidget(button2)

    def open_new_window(self):
        self.window2 = Window2()
        self.window2.show()
        self.close
    def open_new_window2(self):
        self.window3 = Window3()
        self.window3.show()
        self.close

    def setIcon(self):
        appICON = QIcon('1.ico')
        self.setWindowIcon(appICON)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())









