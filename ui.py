# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(467, 417)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LeetCombo = QtWidgets.QLabel(self.centralwidget)
        self.LeetCombo.setGeometry(QtCore.QRect(50, 30, 151, 31))
        self.LeetCombo.setAutoFillBackground(True)
        self.LeetCombo.setObjectName("LeetCombo")
        self.WordList = QtWidgets.QLabel(self.centralwidget)
        self.WordList.setGeometry(QtCore.QRect(50, 70, 101, 16))
        self.WordList.setAutoFillBackground(True)
        self.WordList.setObjectName("WordList")
        self.LeetCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.LeetCheck.setGeometry(QtCore.QRect(20, 40, 16, 17))
        self.LeetCheck.setText("")
        self.LeetCheck.setObjectName("LeetCheck")
        self.WLcheck = QtWidgets.QCheckBox(self.centralwidget)
        self.WLcheck.setGeometry(QtCore.QRect(20, 70, 16, 17))
        self.WLcheck.setText("")
        self.WLcheck.setChecked(False)
        self.WLcheck.setObjectName("WLcheck")
        self.Settings = QtWidgets.QLabel(self.centralwidget)
        self.Settings.setGeometry(QtCore.QRect(10, 100, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Settings.setFont(font)
        self.Settings.setObjectName("Settings")
        self.Numbers = QtWidgets.QLabel(self.centralwidget)
        self.Numbers.setGeometry(QtCore.QRect(50, 150, 91, 16))
        self.Numbers.setObjectName("Numbers")
        self.NumCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.NumCheck.setGeometry(QtCore.QRect(20, 150, 16, 17))
        self.NumCheck.setText("")
        self.NumCheck.setObjectName("NumCheck")
        self.AlpaList = QtWidgets.QLabel(self.centralwidget)
        self.AlpaList.setGeometry(QtCore.QRect(50, 180, 161, 16))
        self.AlpaList.setObjectName("AlpaList")
        self.DefList = QtWidgets.QCheckBox(self.centralwidget)
        self.DefList.setGeometry(QtCore.QRect(20, 180, 16, 17))
        self.DefList.setText("")
        self.DefList.setObjectName("DefList")
        self.MinLength = QtWidgets.QLabel(self.centralwidget)
        self.MinLength.setGeometry(QtCore.QRect(80, 210, 91, 20))
        self.MinLength.setObjectName("MinLength")
        self.MinCombo = QtWidgets.QComboBox(self.centralwidget)
        self.MinCombo.setGeometry(QtCore.QRect(20, 210, 41, 26))
        self.MinCombo.setEditable(False)
        self.MinCombo.setMaxVisibleItems(26)
        self.MinCombo.setMinimumContentsLength(1)
        self.MinCombo.setPlaceholderText("")
        self.MinCombo.setObjectName("MinCombo")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MinCombo.addItem("")
        self.MaxCombo = QtWidgets.QComboBox(self.centralwidget)
        self.MaxCombo.setGeometry(QtCore.QRect(20, 250, 41, 26))
        self.MaxCombo.setEditable(False)
        self.MaxCombo.setMaxVisibleItems(26)
        self.MaxCombo.setMinimumContentsLength(1)
        self.MaxCombo.setPlaceholderText("")
        self.MaxCombo.setObjectName("MaxCombo")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxCombo.addItem("")
        self.MaxLength = QtWidgets.QLabel(self.centralwidget)
        self.MaxLength.setGeometry(QtCore.QRect(80, 250, 101, 20))
        self.MaxLength.setObjectName("MaxLength")
        self.CustomTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.CustomTextEdit.setGeometry(QtCore.QRect(20, 290, 101, 31))
        self.CustomTextEdit.setObjectName("CustomTextEdit")
        self.CustomCharList = QtWidgets.QLabel(self.centralwidget)
        self.CustomCharList.setGeometry(QtCore.QRect(140, 295, 271, 21))
        self.CustomCharList.setObjectName("CustomCharList")
        self.Generate = QtWidgets.QPushButton(self.centralwidget)
        self.Generate.setGeometry(QtCore.QRect(250, 330, 141, 41))
        self.Generate.setObjectName("Generate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 467, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.MinCombo.setCurrentIndex(0)
        self.MaxCombo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LeetCombo.setText(_translate("MainWindow", "Include Leet Combinatons"))
        self.WordList.setText(_translate("MainWindow", "Generate a word list"))
        self.Settings.setText(_translate("MainWindow", "Settings for word list"))
        self.Numbers.setText(_translate("MainWindow", "Include Numbers"))
        self.AlpaList.setText(_translate("MainWindow", "Use default alphabet list (abc...)"))
        self.MinLength.setText(_translate("MainWindow", "Min. Combo length"))
        self.MinCombo.setCurrentText(_translate("MainWindow", "1"))
        self.MinCombo.setItemText(0, _translate("MainWindow", "1"))
        self.MinCombo.setItemText(1, _translate("MainWindow", "2"))
        self.MinCombo.setItemText(2, _translate("MainWindow", "3"))
        self.MinCombo.setItemText(3, _translate("MainWindow", "4"))
        self.MinCombo.setItemText(4, _translate("MainWindow", "5"))
        self.MinCombo.setItemText(5, _translate("MainWindow", "6"))
        self.MinCombo.setItemText(6, _translate("MainWindow", "7"))
        self.MinCombo.setItemText(7, _translate("MainWindow", "8"))
        self.MinCombo.setItemText(8, _translate("MainWindow", "9"))
        self.MinCombo.setItemText(9, _translate("MainWindow", "10"))
        self.MinCombo.setItemText(10, _translate("MainWindow", "11"))
        self.MinCombo.setItemText(11, _translate("MainWindow", "12"))
        self.MinCombo.setItemText(12, _translate("MainWindow", "13"))
        self.MinCombo.setItemText(13, _translate("MainWindow", "14"))
        self.MinCombo.setItemText(14, _translate("MainWindow", "15"))
        self.MinCombo.setItemText(15, _translate("MainWindow", "16"))
        self.MinCombo.setItemText(16, _translate("MainWindow", "17"))
        self.MinCombo.setItemText(17, _translate("MainWindow", "18"))
        self.MinCombo.setItemText(18, _translate("MainWindow", "19"))
        self.MinCombo.setItemText(19, _translate("MainWindow", "20"))
        self.MinCombo.setItemText(20, _translate("MainWindow", "21"))
        self.MinCombo.setItemText(21, _translate("MainWindow", "22"))
        self.MinCombo.setItemText(22, _translate("MainWindow", "23"))
        self.MinCombo.setItemText(23, _translate("MainWindow", "24"))
        self.MinCombo.setItemText(24, _translate("MainWindow", "25"))
        self.MinCombo.setItemText(25, _translate("MainWindow", "26"))
        self.MaxCombo.setCurrentText(_translate("MainWindow", "1"))
        self.MaxCombo.setItemText(0, _translate("MainWindow", "1"))
        self.MaxCombo.setItemText(1, _translate("MainWindow", "2"))
        self.MaxCombo.setItemText(2, _translate("MainWindow", "3"))
        self.MaxCombo.setItemText(3, _translate("MainWindow", "4"))
        self.MaxCombo.setItemText(4, _translate("MainWindow", "5"))
        self.MaxCombo.setItemText(5, _translate("MainWindow", "6"))
        self.MaxCombo.setItemText(6, _translate("MainWindow", "7"))
        self.MaxCombo.setItemText(7, _translate("MainWindow", "8"))
        self.MaxCombo.setItemText(8, _translate("MainWindow", "9"))
        self.MaxCombo.setItemText(9, _translate("MainWindow", "10"))
        self.MaxCombo.setItemText(10, _translate("MainWindow", "11"))
        self.MaxCombo.setItemText(11, _translate("MainWindow", "12"))
        self.MaxCombo.setItemText(12, _translate("MainWindow", "13"))
        self.MaxCombo.setItemText(13, _translate("MainWindow", "14"))
        self.MaxCombo.setItemText(14, _translate("MainWindow", "15"))
        self.MaxCombo.setItemText(15, _translate("MainWindow", "16"))
        self.MaxCombo.setItemText(16, _translate("MainWindow", "17"))
        self.MaxCombo.setItemText(17, _translate("MainWindow", "18"))
        self.MaxCombo.setItemText(18, _translate("MainWindow", "19"))
        self.MaxCombo.setItemText(19, _translate("MainWindow", "20"))
        self.MaxCombo.setItemText(20, _translate("MainWindow", "21"))
        self.MaxCombo.setItemText(21, _translate("MainWindow", "22"))
        self.MaxCombo.setItemText(22, _translate("MainWindow", "23"))
        self.MaxCombo.setItemText(23, _translate("MainWindow", "24"))
        self.MaxCombo.setItemText(24, _translate("MainWindow", "25"))
        self.MaxCombo.setItemText(25, _translate("MainWindow", "26"))
        self.MaxLength.setText(_translate("MainWindow", "Max. Combo Length"))
        self.CustomCharList.setText(_translate("MainWindow", "Custom Characters (Overrides the default alphabet list)"))
        self.Generate.setText(_translate("MainWindow", "Generate Combinations"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())