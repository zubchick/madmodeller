# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys

class Logger(object):
    def setupUi(self, Dialog, log):
        Dialog.setGeometry(400, 600, 500, 600)
        Dialog.setWindowFlags(QtCore.Qt.Window)

        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.addWidget(log)

        Dialog.setWindowTitle(u"Консоль отладки")


def init(parrentwindow, log):
    LoggerWindow = QtGui.QWidget(parrentwindow)
    form = Logger()
    form.setupUi(LoggerWindow, log)
    return form, LoggerWindow
