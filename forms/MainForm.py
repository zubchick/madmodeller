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

        self.block_list = [] # список для блоков на экране

        self.main = MainWindow

        self.scene = Scene()
        # graphics
        self.view = QtGui.QGraphicsView(self.scene, self.main)
        # параметры качества прорисовки для виджета представления:
        self.view.setRenderHints(QtGui.QPainter.Antialiasing |
                                 QtGui.QPainter.SmoothPixmapTransform)


        MainWindow.setCentralWidget(self.view)

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
        self.dockWidgetContents.setLayout(self.flowlayout)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

    def showAboutWindow(self):
        about_form, about_window = about.init(self.main)
        about_window.show()

    def set_blocks(self, block_dict):
        """ рисует кнопочки-блоки """
        self.blocks = {}
        for key, value in block_dict.items():
            ## print key, value
            iBlock = QtGui.QWidget()

            layout = QtGui.QGridLayout(iBlock)

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
            self.connect(button, QtCore.SIGNAL("clicked()"),
                         lambda val=value: self.add_block(val))
            ## button.clicked.connect(lambda : self.add_block(value))
            self.blocks[key] = button
            self.flowlayout.addWidget(iBlock)

    def add_block(self, BlockClass):
        """ Добавить блок на рабочее поле """
        print 'Add to form ', BlockClass
        item = IBlock(QtGui.QPixmap(BlockClass.image), None, self.scene)
        item.block = BlockClass()
        item.setZValue(2)
        self.block_list.append(item)


class Scene(QtGui.QGraphicsScene):
    def __init__(self, parent = None):
        QtGui.QGraphicsScene.__init__(self, parent)

    # операция drag and drop входит в область сцены
    def dragEnterEvent(self, event):
        item = event.mimeData().IBlock
        # временный "затемнённый" рисунок перетаскиваемой картинки:
        tempPixmap = QtGui.QPixmap(item.pixmap())
        painter = QtGui.QPainter()
        painter.begin(tempPixmap)
        painter.fillRect(item.pixmap().rect(), QtGui.QColor(127, 127, 127, 127))
        painter.end()
        item.setPixmap(tempPixmap)

    # операция drag and drop покидает область сцены
    def dragLeaveEvent(self, event):
        item = event.mimeData().IBlock
        # восстанавливаем рисунок перетаскиваемой картинки:
        pixmap = QtGui.QPixmap(event.mimeData().imageData())
        item.setPixmap(pixmap)

    # в процессе выполнения операции drag and drop
    def dragMoveEvent(self, event):
        pass

    # завершение операции drag and drop
    def dropEvent(self, event):
        # создание копии перенесённого элемента на новом месте:
        pixmap = QtGui.QPixmap(event.mimeData().imageData())
        item = IBlock(pixmap, None, self)
        # установка положения элемента,
        # координаты курсора мыши на сцене корректируем координатами курсора мыши на элементе:
        item.setPos(event.scenePos() - event.mimeData().Pos)
        # удаление перенесённого элемента:
        self.removeItem(event.mimeData().IBlock)


class IBlock(QtGui.QGraphicsPixmapItem):
    def __init__(self, pixmap, parent = None, scene = None):
        QtGui.QGraphicsPixmapItem.__init__(self, pixmap, parent, scene)
        self.setTransformationMode(QtCore.Qt.SmoothTransformation) # качество прорисовки

    def mousePressEvent(self, event):
        if event.button() != QtCore.Qt.LeftButton: # только левая клавиша мыши
            event.ignore()
            return
        drag = QtGui.QDrag(event.widget()) # объект Drag
        mime = QtCore.QMimeData()
        mime.setImageData(QtCore.QVariant(self.pixmap())) # запоминаем рисунок
        mime.Pos = event.pos() # запоминаем позицию события в координатах элемента
        mime.z = self.zValue() # запоминаем z-позицию рисунка
        mime.IBlock = self # запоминаем сам элемент, который переносится
        # примечание: предыдущие три "запоминания" можно реализовать
        # и с помощью более "понятного" mime.setData(),
        # особенно, если нужно передавать данные не только в пределах одного приложения
        # (тогда использование mime.setData() будет даже предпочтительнее)
        drag.setMimeData(mime)

        drag.setPixmap(self.pixmap()) # рисунок, отображающийся в процессе переноса
        drag.setHotSpot(event.pos().toPoint()) # позиция "ухватки"

        drag.start() # запуск (начало) перетаскивания


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
