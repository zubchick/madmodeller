#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys

class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle(u'MadModeller')
        MainWindow.resize(600, 450)

        self.main = QtGui.QWidget(MainWindow)
        self.graphicsView = QtGui.QGraphicsView(self.main)
        MainWindow.setCentralWidget(self.graphicsView)

        self.menubar = QtGui.QMenuBar(MainWindow)


        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile =self.menubar.addMenu(u'&Файл')
        ## self.menuEdit = QtGui.QMenu(self.menubar)
        ## self.menuEdit =self.menubar.addMenu(u'&Правка')
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools =self.menubar.addMenu(u'&Инструменты')
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp =self.menubar.addMenu(u'&Справка')
        MainWindow.setMenuBar(self.menubar)


        # open
        act_open = QtGui.QAction(QtGui.QIcon('../images/open.png'),
                                 u'Открыть', self.main)
        act_open.setShortcut('Ctrl+O')
        act_open.setStatusTip(u'Открыть файл')


        # save
        act_save = QtGui.QAction(QtGui.QIcon('../images/save.png'),
                                 u'Сохранить', self.main)
        act_save.setShortcut('Ctrl+S')
        act_save.setStatusTip(u'Сохранить файл')

        # save as
        act_save_as = QtGui.QAction(QtGui.QIcon('../images/save_as.png'),
                                 u'Сохранить как', self.main)
        act_save_as.setShortcut('Ctrl+Shift+S')
        act_save_as.setStatusTip(u'Сохранить файл как...')

        # exit
        act_exit = QtGui.QAction(QtGui.QIcon('../images/exit.png'),
                                 u'Выход', self.main)
        act_exit.setShortcut('Ctrl+Q')
        act_exit.setStatusTip(u'Выйти из приложения')
        MainWindow.connect(act_exit, QtCore.SIGNAL('triggered()'),
                     QtCore.SLOT('close()'))

        # plugin manager
        act_plugins = QtGui.QAction(QtGui.QIcon('../images/plugins.png'),
                                 u'Блоки', self.main)
        act_plugins.setShortcut('Ctrl+P')
        act_plugins.setStatusTip(u'Окно с блоками')

        # console
        act_console = QtGui.QAction(QtGui.QIcon('../images/console.png'),
                                 u'Консоль', self.main)
        act_console.setShortcut('Ctrl+C')
        act_console.setStatusTip(u'Консоль отладки')

        # run
        act_run = QtGui.QAction(QtGui.QIcon('../images/run.png'),
                                 u'Запуск', self.main)
        act_run.setShortcut('Ctrl+R')
        act_run.setStatusTip(u'Запуск симуляции')

        # help
        act_help = QtGui.QAction(QtGui.QIcon('../images/help.png'),
                                 u'Справка', self.main)
        act_help.setShortcut('F1')
        act_help.setStatusTip(u'Открыть справку')

        # about
        act_about = QtGui.QAction(QtGui.QIcon('../images/about.png'),
                                 u'О программе', self.main)
        act_about.setStatusTip(u'О программе')

        self.menuFile.addAction(act_open)
        self.menuFile.addAction(act_save)
        self.menuFile.addAction(act_save_as)
        self.menuFile.addAction(act_exit)

        self.menuTools.addAction(act_plugins)
        self.menuTools.addAction(act_console)
        self.menuTools.addAction(act_run)

        self.menuHelp.addAction(act_help)
        self.menuHelp.addAction(act_about)

        self.menubar.addAction(self.menuFile.menuAction())
        ## self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        toolbar = QtGui.QToolBar(MainWindow)
        toolbar.addAction(act_open)
        toolbar.addAction(act_save)
        toolbar.addAction(act_save_as)
        toolbar.addAction(act_run)
        toolbar.addAction(act_help)
        toolbar.addAction(act_exit)
        MainWindow.addToolBar(toolbar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidgetContents = QtGui.QWidget()

        self.gridLayoutWidget = QtGui.QWidget(self.dockWidgetContents)
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)


def init():
    # инициализируем Qt
    app = QtGui.QApplication(sys.argv)
    # создаем отдельный, независимый объект окна...
    MainWindow = QtGui.QMainWindow()
    # ...и прогоняем его через наш класс
    form = MyMainWindow()
    form.setupUi(MainWindow)
    return app, form, MainWindow

if __name__ == '__main__':
    app, mainForm, window = init()
    window.show()
    sys.exit(app.exec_())
