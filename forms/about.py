# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class About(object):
    def setupUi(self, Dialog):
        Dialog.setFixedSize(350, 180)
        Dialog.setWindowFlags(QtCore.Qt.Window)

        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)

        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.pushButton)
        Dialog.connect(self.pushButton, QtCore.SIGNAL('clicked()'), QtCore.SLOT('close()'))


        Dialog.setWindowTitle(u"О программе")
        self.pushButton.setText(u"Закрыть")
        self.label.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p align=\"center\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#000000;\">MadModeller</span></p>\n"
"<p align=\"center\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">версия 0.0.1</p>\n"
"<p align=\"center\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana\'; font-size:9pt;\">© 2010, </span>Зубков Никита <a href=\"mailto:zubchick@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">&lt;zubchick@gmail.com&gt;</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))



def init(parrentwindow):
    AboutWindow = QtGui.QWidget(parrentwindow)
    form = About()
    form.setupUi(AboutWindow)
    return form, AboutWindow
