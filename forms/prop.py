#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui


class Property(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.Window)

    def setupUi(self, block_obj):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowModality(QtCore.Qt.WindowModal)
        params = block_obj.get_params()
        if params:
            layout = QtGui.QVBoxLayout(self)

            self.setWindowTitle(u'Свойства блока {0}'.format(block_obj.name))

            self.form_dict = {}

            for key, value in block_obj.get_params().items():
                layout.addWidget(QtGui.QLabel(key))
                edit = QtGui.QLineEdit(str(value))
                self.form_dict[key] = edit
                layout.addWidget(edit)

            self.button_ok = QtGui.QPushButton(u'Ок')
            self.button_cancel = QtGui.QPushButton(u'Отмена')
            layout.addWidget(self.button_ok)
            layout.addWidget(self.button_cancel)
            self.connect(self.button_cancel, QtCore.SIGNAL('clicked()'),
                           QtCore.SLOT('close()'))
            self.connect(self.button_ok, QtCore.SIGNAL('clicked()'),
                         lambda val = block_obj: self.set_new_params(val))

    def set_new_params(self, block_obj):
        for key, value in self.form_dict.items():
            val = float(value.text())
            setattr(block_obj, key, val)
        print '{0} new parameters'.format(block_obj)
        self.close()
