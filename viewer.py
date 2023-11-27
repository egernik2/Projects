from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(299, 274)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(110, 220, 75, 23))
        self.btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn.setAutoDefault(False)
        self.btn.setObjectName("btn")
        self.btn.setText('Нажми меня')
        self.btn.clicked.connect(self.view_files)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.grid = QtWidgets.QGridLayout()
        self.listCheckBox = []

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Заменятор текста"))

    def view_files(self):
        with open('fio.list', 'r') as f:
            out = f.readlines()
        self.listCheckBox = out
        for i, v in enumerate(self.listCheckBox):
            self.listCheckBox[i] = QtWidgets.QCheckBox(v.strip())
            self.grid.addWidget(self.listCheckBox[i], i, 0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
