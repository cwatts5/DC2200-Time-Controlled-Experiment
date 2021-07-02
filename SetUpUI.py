# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\clowe\Desktop\Python\DC2200\DC2200_brightness.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(181, 178)
        self.run_button = QtWidgets.QPushButton(Dialog)
        self.run_button.setGeometry(QtCore.QRect(10, 30, 56, 17))
        self.run_button.setObjectName("run_button")
        self.DarkTimeLine = QtWidgets.QLineEdit(Dialog)
        self.DarkTimeLine.setGeometry(QtCore.QRect(110, 90, 31, 20))
        self.DarkTimeLine.setObjectName("DarkTimeLine")
        self.IlluminationTimeLine = QtWidgets.QLineEdit(Dialog)
        self.IlluminationTimeLine.setGeometry(QtCore.QRect(110, 120, 31, 20))
        self.IlluminationTimeLine.setObjectName("IlluminationTimeLine")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 90, 81, 21))
        self.label.setObjectName("label")
        self.StepSizeLine = QtWidgets.QLineEdit(Dialog)
        self.StepSizeLine.setGeometry(QtCore.QRect(110, 150, 31, 20))
        self.StepSizeLine.setObjectName("StepSizeLine")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 101, 21))
        self.label_3.setObjectName("label_3")
        self.CurrentPercentLine = QtWidgets.QLineEdit(Dialog)
        self.CurrentPercentLine.setGeometry(QtCore.QRect(80, 30, 61, 20))
        self.CurrentPercentLine.setObjectName("CurrentPercentLine")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 10, 81, 21))
        self.label_4.setObjectName("label_4")
        self.rev_Check = QtWidgets.QCheckBox(Dialog)
        self.rev_Check.setGeometry(QtCore.QRect(40, 60, 71, 21))
        self.rev_Check.setObjectName("rev_Check")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "DC2200 Controller"))
        self.run_button.setText(_translate("Dialog", "Run"))
        self.DarkTimeLine.setAccessibleDescription(_translate("Dialog", "This is the time the shutter will be closed in seconds."))
        self.IlluminationTimeLine.setAccessibleDescription(_translate("Dialog", "This is the time the shutter will be open in seconds."))
        self.label.setAccessibleDescription(_translate("Dialog", "This is the time the shutter will be closed in seconds."))
        self.label.setText(_translate("Dialog", "Dark time (s)"))
        self.StepSizeLine.setAccessibleDescription(_translate("Dialog", "This is the time between each sample illuminaton step. It will be used to calculate the step size in % brightness."))
        self.label_2.setAccessibleDescription(_translate("Dialog", "This is the time the shutter will be open in seconds."))
        self.label_2.setText(_translate("Dialog", "Illumination time (s)"))
        self.label_3.setAccessibleDescription(_translate("Dialog", "This is the time between each sample illuminaton step. It will be used to calculate the step size in % brightness."))
        self.label_3.setText(_translate("Dialog", "Time between step (s)"))
        self.label_4.setAccessibleDescription(_translate("Dialog", "This is the current brightness level."))
        self.label_4.setText(_translate("Dialog", "Current brightness (%)"))
        self.rev_Check.setAccessibleDescription(_translate("Dialog", "This will add in a reverse to the sample. The actual time of the experiment will be double the illumination time in this case."))
        self.rev_Check.setText(_translate("Dialog", "include reverse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

