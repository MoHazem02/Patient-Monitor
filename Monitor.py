from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import resources
import sys
from App import *
from mplwidget import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 680)
        MainWindow.setMinimumSize(QtCore.QSize(1126, 680))
        MainWindow.setMaximumSize(QtCore.QSize(1126, 680))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/Assets/monitor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:#3A3B3C;\n"
"background-image: url(:/images/Assets/bg2.jpg);\n"
"color: white;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 751, 301))
        self.groupBox.setObjectName("groupBox")
        self.ECG_Graph = PlotWidget(self.groupBox)
        self.ECG_Graph.setGeometry(QtCore.QRect(10, 20, 731, 271))
        self.ECG_Graph.setObjectName("ECG_Graph")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(790, 30, 311, 301))
        self.groupBox_2.setObjectName("groupBox_2")
        self.spectrogram = MplWidget(self.groupBox_2)
        self.spectrogram.setGeometry(QtCore.QRect(10, 20, 291, 271))
        self.spectrogram.setObjectName("spectrogram")
        self.current_temp_LCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.current_temp_LCD.setGeometry(QtCore.QRect(330, 350, 221, 81))
        self.current_temp_LCD.setObjectName("current_temp_LCD")
        self.average_temp_LCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.average_temp_LCD.setGeometry(QtCore.QRect(720, 350, 221, 81))
        self.average_temp_LCD.setObjectName("average_temp_LCD")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 440, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(730, 440, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.status_ok_label = QtWidgets.QLabel(self.centralwidget)
        self.status_ok_label.setGeometry(QtCore.QRect(400, 520, 91, 91))
        self.status_ok_label.setText("")
        self.status_ok_label.setPixmap(QtGui.QPixmap(":/images/Assets/checked.png"))
        self.status_ok_label.setScaledContents(True)
        self.status_ok_label.setObjectName("status_ok_label")
        self.status_warning_label = QtWidgets.QLabel(self.centralwidget)
        self.status_warning_label.setGeometry(QtCore.QRect(810, 520, 91, 91))
        self.status_warning_label.setStyleSheet("opacity: 0.1;")
        self.status_warning_label.setText("")
        self.status_warning_label.setPixmap(QtGui.QPixmap(":/images/Assets/warning.png"))
        self.status_warning_label.setScaledContents(True)
        self.status_warning_label.setObjectName("status_warning_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Patient Monitor"))
        self.groupBox.setTitle(_translate("MainWindow", "ECG"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Spectrogram"))
        self.label.setText(_translate("MainWindow", "Current Temperature"))
        self.label_2.setText(_translate("MainWindow", "Average Temperature"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    Main = ApplicationManager(ui)
    MainWindow.show()
    sys.exit(app.exec_())
