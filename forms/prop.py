#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui


class Property(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.Window)

    def setupUi(self, block_obj):
        params = block_obj._get_params()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowModality(QtCore.Qt.WindowModal)
        layout = QtGui.QVBoxLayout(self)

        self.button_ok = QtGui.QPushButton(u'Ок')
        self.button_cancel = QtGui.QPushButton(u'Отмена')
        self.connect(self.button_cancel, QtCore.SIGNAL('clicked()'),
                     QtCore.SLOT('close()'))
        self.connect(self.button_ok, QtCore.SIGNAL('clicked()'),
                     lambda val = block_obj: self.set_new_params(val))

        if params:
            self.setWindowTitle(u'Свойства блока {0}'.format(block_obj.name))

            self.form_dict = {}

            for key, value in block_obj._get_params().items():
                layout.addWidget(QtGui.QLabel(key[6:])) # отрезаем 6 букв от 'change'
                edit = QtGui.QLineEdit(str(value))
                self.form_dict[key] = edit
                layout.addWidget(edit)
            layout.addWidget(self.button_ok)
            layout.addWidget(self.button_cancel)

        else:
            layout.addWidget(QtGui.QLabel(u'<strong>У блока нет изменяемых свойств.<strong>'))
            layout.addWidget(self.button_cancel)

    def set_new_params(self, block_obj):
        for key, value in self.form_dict.items():
            val = float(value.text())
            setattr(block_obj, key, val)
        print '{0} new parameters'.format(block_obj)
        self.close()
