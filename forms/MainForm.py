#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys
import about
import prop
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

        self.background = self.scene.addPixmap(QtGui.QPixmap("")) # без фона

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

        # mode - состояние программы
        self.mode = 'normal'

        # draw - line
        act_draw_line = QtGui.QAction(QtGui.QIcon('images/draw_line.png'),
                                 u'Установить связь', self.main)
        act_draw_line.setStatusTip(u'Установить связь между блоками')
        MainWindow.connect(act_draw_line, QtCore.SIGNAL('triggered()'),
                           self.draw_line)

        # background-image
        act_bgr_img = QtGui.QAction(QtGui.QIcon('images/background.png'),
                                 u'Установить фон', self.main)
        act_bgr_img.setStatusTip(u'Устанофить фон для рабочей области')
        MainWindow.connect(act_bgr_img, QtCore.SIGNAL('triggered()'),
                           self.add_background)

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

        ## self.menuEdit.addAction(act_bgr_img)

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
        toolbar.addAction(act_bgr_img)
        toolbar.addAction(act_draw_line)
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
        self.dockWidget.setMinimumSize(180, 50)

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
        ## item = self.scene.addPixmap(QtGui.QPixmap(BlockClass.image))
        ## item.setFlags(QtGui.QGraphicsItem.ItemIsMovable)
        ## item.setZValue(3)
        if self.mode == 'normal':
            item = IBlock(QtGui.QPixmap(BlockClass.image), None, self.scene)
            item.block = BlockClass()
            item.block.index = hash(str(item.block))
            item.setZValue(3)
            item.setFlags(QtGui.QGraphicsItem.ItemIsMovable)
            item.setToolTip(item.block.get_out())
            self.block_list.append(item)
            print 'Add to form ', BlockClass

    def add_background(self):
        """ Добавить фоновую картинку на рабочее поле """
        if self.mode == 'normal':
            img = QtGui.QFileDialog.getOpenFileName(caption = u'Выбрать фон',
                                                    filter = u'Картинки (*.png *.jpg)')
            self.scene.removeItem(self.background)
            self.background = self.scene.addPixmap(QtGui.QPixmap(img))
            self.background.setFlags(QtGui.QGraphicsItem.ItemIsMovable)
            print 'Background add to form ', img

    def draw_line(self):
        """ Рисует линию между двумя блоками """
        if self.mode == 'normal':
            self.mode = 'draw_line_mode'
            print '%s mode set' % self.mode.capitalize()
            cursor = QtGui.QCursor(QtGui.QPixmap('images/draw_line.png'))
            self.view.setCursor(cursor)
        elif self.mode == 'draw_line_mode':
            self.set_normal_mode()

    def set_normal_mode(self):
        self.mode = 'normal'
        cursor = QtGui.QCursor(QtCore.Qt.ArrowCursor)
        self.view.setCursor(cursor)
        print '%s mode set' % self.mode.capitalize()


class IBlock(QtGui.QGraphicsPixmapItem):
    def __init__(self, pixmap, parent = None, scene = None):
        self.parent = parent
        QtGui.QGraphicsPixmapItem.__init__(self, pixmap, parent, scene)

    def mousePressEvent(self, event):
        if event.button() != QtCore.Qt.LeftButton: # только левая клавиша мыши
            event.ignore()
            return
        print 'You pressed ', self.block

    def mouseDoubleClickEvent(self, event):
        if event.button() != QtCore.Qt.LeftButton: # только левая клавиша мыши
            event.ignore()
            return
        property_window = prop.Property(MainWindow)
        property_window.setupUi(self.block)
        property_window.show()
        print 'You doubleClecked ', self.block

class Scene(QtGui.QGraphicsScene):
    def __init__(self, parent = None):
        QtGui.QGraphicsScene.__init__(self, parent)

    ## def mousePressEvent(self, e):
    ##     self.add_line(e.x(), e.y())
    ##     self.update()

    def add_line(self, x, y):
        line = Line(x, y)

class Line(QtCore.QLineF):
    def __init__(self, start, stop):
        QtCore.QLineF.__init__(self)
        self.color = QtCore.Qt.black
        self.path = QtGui.QPainterPath()
        self.path.moveTo(self)
        self.start = start
        self.stop = stop

    def paint(self, painter):
        """ внешний вид """
        painter.setPen(QtGui.QPen(self.color, 1))
        painter.drawLine(self, QtCore.QPointF(self.x() + 15, self.y() + 15))

    def clearPath(self):
        """очистить шлейф"""
        self.path = QtGui.QPainterPath()
        self.path.moveTo(self)


def init():
    app = QtGui.QApplication(sys.argv)
    global MainWindow
    MainWindow = QtGui.QMainWindow()
    form = MyMainWindow()
    form.setupUi(MainWindow)
    return app, form, MainWindow

if __name__ == '__main__':
    app, mainForm, window = init()
    window.show()
    sys.exit(app.exec_())
