#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys
import about
import flowlayout as flow

class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle(u'MadModeller')
        MainWindow.resize(600, 450)

        self.main = MainWindow
        self.graphicsView = QtGui.QGraphicsView(self.main)
        MainWindow.setCentralWidget(self.graphicsView)

        self.menubar = QtGui.QMenuBar(MainWindow)

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile = self.menubar.addMenu(u'&Файл')
        ## self.menuEdit = QtGui.QMenu(self.menubar)
        ## self.menuEdit = self.menubar.addMenu(u'&Правка')
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools = self.menubar.addMenu(u'&Инструменты')
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp = self.menubar.addMenu(u'&Справка')

        MainWindow.setMenuBar(self.menubar)


        # open
        act_open = QtGui.QAction(QtGui.QIcon('images/open.png'),
                                 u'Открыть', self.main)
        act_open.setShortcut('Ctrl+O')
        act_open.setStatusTip(u'Открыть файл')


        # save
        act_save = QtGui.QAction(QtGui.QIcon('images/save.png'),
                                 u'Сохранить', self.main)
        act_save.setShortcut('Ctrl+S')
        act_save.setStatusTip(u'Сохранить файл')

        # save as
        act_save_as = QtGui.QAction(QtGui.QIcon('images/save_as.png'),
                                 u'Сохранить как', self.main)
        act_save_as.setShortcut('Ctrl+Shift+S')
        act_save_as.setStatusTip(u'Сохранить файл как...')

        # exit
        act_exit = QtGui.QAction(QtGui.QIcon('images/exit.png'),
                                 u'Выход', self.main)
        act_exit.setShortcut('Ctrl+Q')
        act_exit.setStatusTip(u'Выйти из приложения')
        MainWindow.connect(act_exit, QtCore.SIGNAL('triggered()'),
                     QtCore.SLOT('close()'))

        # plugin manager
        act_plugins = QtGui.QAction(QtGui.QIcon('images/plugins.png'),
                                 u'Блоки', self.main)
        act_plugins.setShortcut('Ctrl+P')
        act_plugins.setStatusTip(u'Окно с блоками')

        # console
        act_console = QtGui.QAction(QtGui.QIcon('images/console.png'),
                                 u'Консоль', self.main)
        act_console.setShortcut('Ctrl+C')
        act_console.setStatusTip(u'Консоль отладки')

        # run
        act_run = QtGui.QAction(QtGui.QIcon('images/run.png'),
                                 u'Запуск', self.main)
        act_run.setShortcut('Ctrl+R')
        act_run.setStatusTip(u'Запуск симуляции')

        # help
        act_help = QtGui.QAction(QtGui.QIcon('images/help.png'),
                                 u'Справка', self.main)
        act_help.setShortcut('F1')
        act_help.setStatusTip(u'Открыть справку')

        # about
        act_about = QtGui.QAction(QtGui.QIcon('images/about.png'),
                                 u'О программе', self.main)
        act_about.setStatusTip(u'О программе')
        MainWindow.connect(act_about, QtCore.SIGNAL('triggered()'),
                           self.showAboutWindow)

        self.menuFile.addAction(act_open)
        self.menuFile.addAction(act_save)
        self.menuFile.addAction(act_save_as)
        self.menuFile.addAction(act_exit)

        ## self.menuEdit.addAction(act_help)

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
        toolbar.setWindowTitle(u'Панель инструментов')
        MainWindow.addToolBar(toolbar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidget.setWindowTitle(u'Блоки')
        self.dockWidget.setMinimumSize(180, 180)

        self.flowlayout = flow.FlowLayout()
        ## self.flowlayout.addWidget(QtGui.QPushButton("Short"))
        ## self.flowlayout.addWidget(QtGui.QPushButton("Longer"))
        ## self.flowlayout.addWidget(QtGui.QPushButton("Different text"))
        ## self.flowlayout.addWidget(QtGui.QPushButton("More text"))
        ## self.flowlayout.addWidget(QtGui.QPushButton("Even longer button text"))
        self.dockWidgetContents.setLayout(self.flowlayout)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

    def showAboutWindow(self):
        about_form, about_window = about.init(self.main)
        about_window.show()

    def set_blocks(self, block_dict):
        """ рисует кнопочки-блоки """
        self.blocks = {}
        iblocks = {}
        for key, value in block_dict.items():
            print key, value
            Iblock = QtGui.QWidget()

            layout = QtGui.QGridLayout(Iblock)

            label = QtGui.QLabel(key)
            label.setAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(7)
            label.setFont(font)

            button = QtGui.QPushButton()
            button.setIcon(QtGui.QIcon(value.image))
            button.setIconSize(QtCore.QSize(30, 30))
            button.setStatusTip(value.doc)

            layout.addWidget(button, 0, 1, 1, 1)
            layout.addWidget(label, 1, 0, 1, 3)

            Iblock.class_ = value
            self.blocks[key] = button
            iblocks[key] = Iblock
            self.flowlayout.addWidget(iblocks[key])


def init():
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
