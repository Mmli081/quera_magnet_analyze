from PyQt5 import QtCore, QtGui, QtWidgets
from logic import main_func


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Backend = QtWidgets.QPushButton(self.centralwidget)
        self.Backend.setGeometry(QtCore.QRect(5, 50, 141, 31))
        self.Backend.setObjectName("Backend")
        self.Frontend = QtWidgets.QPushButton(self.centralwidget)
        self.Frontend.setGeometry(QtCore.QRect(5, 90, 141, 31))
        self.Frontend.setObjectName("Frontend")
        self.React = QtWidgets.QPushButton(self.centralwidget)
        self.React.setGeometry(QtCore.QRect(5, 210, 141, 31))
        self.React.setObjectName("React")
        self.Mobile = QtWidgets.QPushButton(self.centralwidget)
        self.Mobile.setGeometry(QtCore.QRect(5, 130, 141, 31))
        self.Mobile.setObjectName("Mobile")
        self.JavaScript = QtWidgets.QPushButton(self.centralwidget)
        self.JavaScript.setGeometry(QtCore.QRect(5, 170, 141, 31))
        self.JavaScript.setObjectName("JavaScript")
        self.Python = QtWidgets.QPushButton(self.centralwidget)
        self.Python.setGeometry(QtCore.QRect(5, 250, 141, 31))
        self.Python.setObjectName("Python")
        self.PHP = QtWidgets.QPushButton(self.centralwidget)
        self.PHP.setGeometry(QtCore.QRect(5, 290, 141, 31))
        self.PHP.setObjectName("PHP")
        self.Java = QtWidgets.QPushButton(self.centralwidget)
        self.Java.setGeometry(QtCore.QRect(5, 330, 141, 31))
        self.Java.setObjectName("Java")
        self.Linux = QtWidgets.QPushButton(self.centralwidget)
        self.Linux.setGeometry(QtCore.QRect(5, 370, 141, 31))
        self.Linux.setObjectName("Linux")
        self.Django = QtWidgets.QPushButton(self.centralwidget)
        self.Django.setGeometry(QtCore.QRect(5, 410, 141, 31))
        self.Django.setObjectName("Django")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(5, 0, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.generalOutput = QtWidgets.QTextEdit(self.centralwidget)
        self.generalOutput.setGeometry(QtCore.QRect(240, 60, 541, 371))
        self.generalOutput.setObjectName("generalOutput")
        self.log = QtWidgets.QTextBrowser(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(10, 450, 771, 101))
        self.log.setObjectName("log")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Backend.clicked.connect(lambda: main_func(ui, app, "backend"))
        self.Frontend.clicked.connect(lambda: main_func(ui, app, "frontend"))
        self.Mobile.clicked.connect(lambda: main_func(ui, app, "mobile"))
        self.JavaScript.clicked.connect(lambda: main_func(ui, app, "javascript"))
        self.Java.clicked.connect(lambda: main_func(ui, app, "java"))
        self.React.clicked.connect(lambda: main_func(ui, app, "reactjs"))
        self.Python.clicked.connect(lambda: main_func(ui, app, "python"))
        self.Linux.clicked.connect(lambda: main_func(ui, app, "linux"))
        self.Django.clicked.connect(lambda: main_func(ui, app, "django"))
        self.PHP.clicked.connect(lambda: main_func(ui, app, "php"))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Analysis Quera Careers"))
        self.Backend.setText(_translate("MainWindow", "Backend"))
        self.Frontend.setText(_translate("MainWindow", "Frontend"))
        self.React.setText(_translate("MainWindow", "React"))
        self.Mobile.setText(_translate("MainWindow", "Mobile"))
        self.JavaScript.setText(_translate("MainWindow", "JavaScript"))
        self.Python.setText(_translate("MainWindow", "Python"))
        self.PHP.setText(_translate("MainWindow", "PHP"))
        self.Java.setText(_translate("MainWindow", "Java"))
        self.Linux.setText(_translate("MainWindow", "Linux"))
        self.Django.setText(_translate("MainWindow", "Django"))
        self.label.setText(_translate("MainWindow", "select your technology"))
        self.generalOutput.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//FA\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
