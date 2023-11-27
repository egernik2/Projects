from PyQt5 import QtCore, QtGui, QtWidgets
from getpass import getpass
import paramiko
import re
import time
import json
import threading

FILE_NAME = 'list.txt'
CODING = 'CP866'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 80, 281, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 91, 16))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setWhatsThis("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 91, 16))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setWhatsThis("")
        self.label_3.setObjectName("label_3")
        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 120, 761, 441))
        self.listView.setAutoScroll(True)
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.read_data)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label.setText(_translate("MainWindow", "Пользователь"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.label_3.setText(_translate("MainWindow", "Команда"))
        self.pushButton.setText(_translate("MainWindow", "Пуск"))

    def recv_all(self, paramiko_channel):
        parts = []
        while paramiko_channel.recv_ready():
            parts.append(paramiko_channel.recv(4096))
        return b"".join(parts)

    def recv_stderr(self, paramiko_channel):
        parts = []
        while paramiko_channel.recv_stderr_ready():
            parts.append(paramiko_channel.recv_stderr(4096))
        return b"".join(parts)

    def autossh(self, host, user, password, cmd):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=password, timeout=30)
        # Получаем транспорт SSH подключения
        transport = ssh.get_transport()
        # Открываем канал
        paramiko_channel = ssh.get_transport().open_session()
        paramiko_channel.set_combine_stderr(True)
        paramiko_channel.exec_command(cmd)
        output = b''
        while not paramiko_channel.exit_status_ready():
            buffer = self.recv_all(paramiko_channel)
            output += buffer
            if re.search(b'continue connecting (yes/no)?', buffer.lower()):
                paramiko_channel.send("yes\n")
            time.sleep(0.1)
        ecode = paramiko_channel.recv_exit_status()
        output = self.recv_all(paramiko_channel)
        errors = self.recv_stderr(paramiko_channel)
        if ecode == 0:
            self.listView.addItem('{} OUTPUT: {}'.format(host, output.decode(CODING)))
            self.listView.scrollToBottom()
        else:
            self.listView.addItem('{} ERROR'.format(host))
            self.listView.scrollToBottom()

    def print_info(self):
        self.listView.addItem('Данные для входа:')
        self.listView.scrollToBottom()
        self.listView.addItem('Пользователь: {}'.format(self.user))
        self.listView.scrollToBottom()
        self.listView.addItem('Команда: {}'.format(self.cmd))
        self.listView.scrollToBottom()
        self.listView.addItem('Имя файла со списком хостов: {}\n'.format(FILE_NAME))
        self.listView.scrollToBottom()

    def read_data(self):
        self.user = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        self.cmd = self.lineEdit_3.text()
        if self.user != '' and self.password != '' and self.cmd != '':
            self.print_info()
            try:
                with open(FILE_NAME, 'r') as f:
                        list_of_hosts = f.read().splitlines()
                thread = threading.Thread(target=self.do_this, args=(list_of_hosts, ), daemon=True)
                thread.start()
            except:
                self.listView.addItem('Файл со списком хостов list.txt отсутствует')
                self.listView.scrollToBottom()
        else:
            self.listView.addItem('Неполные данные')
            self.listView.scrollToBottom()

    def do_this(self, list_of_hosts):
        for host in list_of_hosts:
            try:
                self.autossh(host, self.user, self.password, self.cmd)
            except Exception as ex:
                self.listView.addItem('{}: {}'.format(host, ex))
                self.listView.scrollToBottom()
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
