# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple.ui'
#
# Created: Tue Jul  9 11:59:42 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui
import pdb

class simpleMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 220, 114, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.buttonPressed)
        self.pushButton.clicked.connect(self.buttonPressed)


        self.currentValue = '' 


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "push me", None, QtGui.QApplication.UnicodeUTF8))

    def buttonPressed(self):
        print 'PRESSED'
        self.pushButton.setText('stop it')

def runSimple():
    try:
        app = QtGui.QApplication(sys.argv)
    except RuntimeError:
        app = QtCore.QCoreApplication.instance()

    MainWindow = QtGui.QMainWindow()
    gui = simpleMainWindow()
    gui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.raise_()

    app.exec_()

if __name__ == "__main__":
    try:
        app = QtGui.QApplication(sys.argv)
    except RuntimeError:
        app = QtCore.QCoreApplication.instance()

    MainWindow = QtGui.QMainWindow()
    gui = simpleMainWindow()
    gui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.raise_()

    app.exec_()
