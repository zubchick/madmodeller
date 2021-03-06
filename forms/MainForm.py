# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys
import about
import logger
import prop
import arrow as arr_ # вот так все сложно да.
import flowlayout as flow
import logica

## class Logger(object):
##     def __init__(self, output):
##         self.output = output

##     def write(self, string):
##         if not (string == "\n"):
##             trstring = QtGui.QApplication.translate("MainWindow", string.strip(),
##                                                     None, QtGui.QApplication.UnicodeUTF8)
##             self.output.append(trstring)


class MyMainWindow(QtGui.QMainWindow):
    """ Главное окно программы """
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.log = QtGui.QTextEdit()
        self.log.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.log.append("Log started")
        # вывод в консоль ctr-C
        ## sys.stdout = Logger(self.log)
        ## sys.stderr = Logger(self.log)

    def setupUi(self, MainWindow_):
        MainWindow_.setWindowTitle(u'MadModeller')
        MainWindow_.resize(800, 600)

        self.block_list = [] # список для блоков на экране

        self.main = MainWindow_


        self.scene = Scene(self.main)
        self.scene.setSceneRect(QtCore.QRectF(0, 0, 500, 500))
        self.scene.itemInserted.connect(self.itemInserted)
        self.scene.backInserted.connect(self.backInserted)
        # graphics
        self.view = QtGui.QGraphicsView(self.scene, self.main)

        # параметры качества прорисовки для виджета представления:
        self.view.setRenderHints(QtGui.QPainter.Antialiasing |
                                 QtGui.QPainter.SmoothPixmapTransform)


        MainWindow_.setCentralWidget(self.view)

        self.menubar = QtGui.QMenuBar(MainWindow_)

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile = self.menubar.addMenu(u'Файл')
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit = self.menubar.addMenu(u'Правка')
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools = self.menubar.addMenu(u'Инструменты')
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp = self.menubar.addMenu(u'Справка')

        MainWindow_.setMenuBar(self.menubar)

        # mode - состояние программы
        self.mode = 'normal'


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
        MainWindow_.connect(act_exit, QtCore.SIGNAL('triggered()'),
                     QtCore.SLOT('close()'))

        # delete
        act_delete = QtGui.QAction(QtGui.QIcon('images/delete.png'),
                u'Удалить элемент', self, shortcut="Delete",
                statusTip=u'Удалить элемент с рабочего поля.',
                triggered=self.deleteItem)

        # background-image
        act_bgr_img = QtGui.QAction(QtGui.QIcon('images/background.png'),
                                 u'Установить фон', self.main)
        act_bgr_img.setStatusTip(u'Устанофить фон для рабочей области')
        MainWindow_.connect(act_bgr_img, QtCore.SIGNAL('triggered()'),
                           self.add_background)

        # delete background
        act_bgr_del = QtGui.QAction(QtGui.QIcon('images/delete_background.png'),
                                 u'Удалить фон', self.main)
        act_bgr_del.setStatusTip(u'Удалить фон с рабочей области')
        MainWindow_.connect(act_bgr_del, QtCore.SIGNAL('triggered()'),
                           self.del_background)

        # draw - line
        act_draw_line = QtGui.QAction(QtGui.QIcon('images/draw_line.png'),
                                 u'Установить связь', self.main)
        act_draw_line.setCheckable(True)
        act_draw_line.setShortcut('Space')
        act_draw_line.setStatusTip(u'Установить связь между блоками')
        MainWindow_.connect(act_draw_line, QtCore.SIGNAL('triggered()'),
                           self.draw_line)

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
        MainWindow_.connect(act_console, QtCore.SIGNAL('triggered()'),
                           self.show_console)

        # run
        act_run = QtGui.QAction(QtGui.QIcon('images/run.png'),
                                 u'Запуск', self.main)
        act_run.setShortcut('Ctrl+R')
        act_run.setStatusTip(u'Запуск симуляции')
        MainWindow_.connect(act_run, QtCore.SIGNAL('triggered()'),
                           self.start_sim)


        # help
        act_help = QtGui.QAction(QtGui.QIcon('images/help.png'),
                                 u'Справка', self.main)
        act_help.setShortcut('F1')
        act_help.setStatusTip(u'Открыть справку')

        # about
        act_about = QtGui.QAction(QtGui.QIcon('images/about.png'),
                                 u'О программе', self.main)
        act_about.setStatusTip(u'О программе')
        MainWindow_.connect(act_about, QtCore.SIGNAL('triggered()'),
                           self.showAboutWindow)

        self.menuFile.addAction(act_open)
        self.menuFile.addAction(act_save)
        self.menuFile.addAction(act_save_as)
        self.menuFile.addAction(act_exit)

        self.menuEdit.addAction(act_bgr_img)
        self.menuEdit.addAction(act_bgr_del)
        self.menuEdit.addAction(act_delete)
        self.menuEdit.addAction(act_draw_line)


        self.menuTools.addAction(act_plugins)
        self.menuTools.addAction(act_console)
        self.menuTools.addAction(act_run)

        self.menuHelp.addAction(act_help)
        self.menuHelp.addAction(act_about)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        toolbar = QtGui.QToolBar(MainWindow_)
        toolbar.addAction(act_open)
        toolbar.addAction(act_save)
        toolbar.addAction(act_save_as)
        toolbar.addAction(act_bgr_img)
        toolbar.addAction(act_draw_line)
        toolbar.addAction(act_delete)
        toolbar.addAction(act_run)
        toolbar.addAction(act_help)
        toolbar.addAction(act_exit)

        toolbar.setWindowTitle(u'Панель инструментов')
        MainWindow_.addToolBar(toolbar)

        self.statusbar = QtGui.QStatusBar(MainWindow_)
        MainWindow_.setStatusBar(self.statusbar)

        self.dockWidget = QtGui.QDockWidget(MainWindow_)
        self.dockWidget.setWindowTitle(u'Блоки')
        self.dockWidget.setMinimumSize(160, 10)

        doc_contents = QtGui.QWidget()
        layout_main = QtGui.QVBoxLayout(self)
        doc_contents.setLayout(layout_main)
        self.scroll_area = QtGui.QScrollArea()
        layout_main.addWidget(self.scroll_area)
        self.scroll_widget = QtGui.QWidget()

        self.flowlayout = flow.FlowLayout()
        self.scroll_widget.setLayout(self.flowlayout)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)

        self.dockWidget.setWidget(doc_contents)
        MainWindow_.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

    def backInserted(self):
        self.set_cursor()

    def itemInserted(self, item):
        self.blocks_button[item.block.name].setChecked(False)
        self.set_cursor()

    def show_console(self):
        print 'console'
        log_form, log_window = logger.init(self.main, self.log)
        log_window.show()
        ## console = myQThread() # До лучших времен
        ## console.run()

    ## @QtCore.pyqtSignature("")
    ## def threadFinished(self):
    ##     print 'Thread finished'

    def showAboutWindow(self):
        print 'About window'
        about_form, about_window = about.init(self.main)
        about_window.show()

    def set_blocks(self, block_dict):
        """ рисует кнопочки-блоки в Doc'е """
        self.blocks_button = {}
        for key, value in block_dict.items():
            iBlock = QtGui.QWidget()

            layout = QtGui.QGridLayout(iBlock)

            label = QtGui.QLabel(key)
            label.setAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(7)
            label.setFont(font)

            button = QtGui.QToolButton()
            button.setIcon(QtGui.QIcon(value.image))
            button.setIconSize(QtCore.QSize(30, 30))
            button.setStatusTip(value.doc)
            button.setCheckable(True)

            layout.addWidget(button, 0, 1, 1, 1)
            layout.addWidget(label, 1, 0, 1, 3)
            self.connect(button, QtCore.SIGNAL("clicked()"),
                         lambda val=value: self.add_block(val))
            self.blocks_button[key] = button
            self.flowlayout.addWidget(iBlock)

    def add_block(self, BlockClass):
        """ Добавить блок на рабочее поле """
        if self.mode == 'normal':
            item = IBlock(QtGui.QPixmap(BlockClass.image))
            item.block = BlockClass()
            item.block.index = hash(str(item.block))
            item.setZValue(3)
            item.setToolTip(item.block.get_out())
            self.scene.current = item
            self.scene.set_mode('insert')
            self.set_cursor(BlockClass.image)
            ## self.set_cursor('images/cross.png')# или так
            self.block_list.append(item)
            # убираем выделение с остальных кнопочек
            for button in self.blocks_button.values():
                button.setChecked(False)
            # и устанавливаем на нужной
            self.blocks_button[BlockClass.name].setChecked(True)

    def add_background(self):
        """ Добавить фоновую картинку на рабочее поле """
        if self.mode == 'normal':
            img = QtGui.QFileDialog.getOpenFileName(caption = u'Выбрать фон',
                                                    filter = u'Картинки (*.png *.jpg)')
            if img:
                self.scene.set_mode('background')
                self.set_cursor('images/cross.png')
                self.scene.removeItem(self.scene.background)
                self.scene.backgound = img

    def del_background(self):
        """ Удалить фоновую картинку """
        self.scene.removeItem(self.scene.background)

    def set_cursor(self, pic=None):
        """ Устанавливает вид курсора """
        if pic == None:
            self.view.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        else:
            self.view.setCursor(QtGui.QCursor(QtGui.QPixmap(pic)))

    def draw_line(self):
        """ Рисует линию между двумя блоками """
        if self.mode == 'normal':
            self.mode = 'draw_line'
            self.scene.mode = 'draw_line'
            print '%s mode set' % self.mode.capitalize()
            self.set_cursor('images/draw_line.png')
        elif self.mode == 'draw_line':
            self.set_normal_mode()


    def set_normal_mode(self):
        self.mode = 'normal'
        self.scene.mode = 'normal'
        self.set_cursor()
        print '%s mode set' % self.mode.capitalize()

    def deleteItem(self):
        for item in self.scene.selectedItems():
            if isinstance(item, IBlock):
                item.removeArrows()
            elif isinstance(item, arr_.Arrow):
                item.startItem.removeArrow(item)
                item.endItem.removeArrow(item)
                item.scene().remove_arrow(item)
            self.scene.removeItem(item)

    def start_sim(self):
        scheme = logica.Scheme(self.scene.arrows)
        scheme.simulation()
        ok = QtGui.QMessageBox.information(self, u'Симуляция завершилась успешно',
                                   u"Симуляция завершена", QtGui.QMessageBox.Ok)

class IBlock(QtGui.QGraphicsPixmapItem):
    def __init__(self, pixmap, parent = None, contextMenu = None):
        self.parent = parent
        QtGui.QGraphicsPixmapItem.__init__(self, pixmap, parent)
        self.arrows = []
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
        self.pix = pixmap

    @property
    def pos(self):
        return (super(IBlock, self).scenePos() +
                QtCore.QPointF(self.pix.rect().center()))

    @property
    def back_points(self):
        """ Возвращаяет две точки, лежащие на 'задней'
        линии картинки блока, для рассчета точки
        соприкосновения стрелки

        """
        end_center = self.pix.rect().center()
        return (QtCore.QPointF(-end_center.x(), -end_center.y()),
                QtCore.QPointF(-end_center.x(), end_center.y()))

    def removeArrow(self, arrow):
        try:
            self.arrows.remove(arrow)
        except ValueError:
            pass

    def removeArrows(self):
        for arrow in self.arrows[:]:
            arrow.startItem.removeArrow(arrow)
            arrow.endItem.removeArrow(arrow)
            self.scene().removeItem(arrow)
            self.scene().remove_arrow(arrow)

    def addArrow(self, arrow):
        self.arrows.append(arrow)

    ## def itemChange(self, change, value):
    ##     if change == QtGui.QGraphicsItem.ItemPositionChange:
    ##         for arrow in self.arrows:
    ##             arrow.updatePosition()

    ##     return value

    def contextMenuEvent(self, event):
        self.scene().clearSelection()
        self.setSelected(True)
        self.myContextMenu.exec_(event.screenPos())


class Scene(QtGui.QGraphicsScene):
    itemInserted = QtCore.pyqtSignal(IBlock)
    backInserted = QtCore.pyqtSignal()
    itemSelected = QtCore.pyqtSignal(QtGui.QGraphicsItem)

    def __init__(self, parent = None):
        QtGui.QGraphicsScene.__init__(self, parent)
        self.mode = 'normal'
        self.line = None
        self.parent = parent
        self.background = self.addPixmap(QtGui.QPixmap('')) # без фона
        self.arrows = []

    def set_mode(self, mode):
        self.mode = mode

    def remove_arrow(self, arrow):
        self.arrows.remove(arrow)

    def mouseDoubleClickEvent(self, event):
        if event.button() != QtCore.Qt.LeftButton: # только левая клавиша мыши
            event.ignore()
            return
        if self.mode == 'normal':
            try:
                item = self.items(event.scenePos())[0]
                if item.block.pure:
                    property_window = prop.Property(self.parent)
                    property_window.setupUi(item.block)
                    property_window.show()
                else:
                    item.block.show()

                print 'You doubleClecked ', item.block
            except: # IndexError:
                super(Scene, self).mouseDoubleClickEvent(event)

    def mousePressEvent(self, event):
        if event.button() != QtCore.Qt.LeftButton: # только левая клавиша мыши
            event.ignore()
            return

        if self.mode == 'draw_line':
            # потом надо будет переопределить линию на кривую стрелку
            self.line = QtGui.QGraphicsLineItem(QtCore.QLineF(event.scenePos(),
                                                         event.scenePos()))
            self.line.setPen(QtGui.QPen(QtCore.Qt.black, 2))
            self.addItem(self.line)
            #self.update()

        elif self.mode == 'insert':
            print 'Add to form ', self.current.block
            self.addItem(self.current)
            # берем картинку блока
            image = QtGui.QPixmap(self.current.block.image)
            # вычисляем размеры
            ## move_to = QtCore.QPointF(image.width() / 2, image.height() / 2)
            move_to = QtCore.QPointF(image.rect().center())
            # двигаем ровно под мышьку
            self.current.setPos(event.scenePos() - move_to)
            self.set_mode('normal')
            self.itemInserted.emit(self.current)

        elif self.mode == 'background':
            image = QtGui.QPixmap(self.backgound)
            move_to = QtCore.QPointF(image.rect().center())
            self.background = self.addPixmap(image)
            self.background.setPos(event.scenePos() - move_to)
            self.background.setFlags(QtGui.QGraphicsItem.ItemIsMovable)
            self.background.setZValue(-1000.0)
            print 'Background add to form ', self.background
            self.set_mode('normal')
            self.backInserted.emit()

        else:
            super(Scene, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.mode == 'draw_line' and self.line:
            new_line = QtCore.QLineF(self.line.line().p1(), event.scenePos())
            self.line.setLine(new_line)
        else:
            super(Scene, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.line and self.mode == 'draw_line':
            startItems = self.items(self.line.line().p1())
            if len(startItems) and startItems[0] == self.line:
                startItems.pop(0)

            endItems = self.items(self.line.line().p2())
            if len(endItems) and endItems[0] == self.line:
                endItems.pop(0)

            self.removeItem(self.line)
            self.line = None

            if (len(startItems) and len(endItems) and
                isinstance(startItems[0], IBlock) and
                isinstance(endItems[0], IBlock) and
                startItems[0] != endItems[0]):
                startItem = startItems[0]
                endItem = endItems[0]
                max_inp = endItems[0].block.inp
                if max_inp > 1:
                    inp, ok = QtGui.QInputDialog.getInteger(self.parent, u'Выбор входа.',
                                                            u'Выберете вход (1..{0}):'.format(max_inp),
                                                            1, 1, max_inp, 1)
                else:
                    inp = 1

                arrow = arr_.Arrow(startItem, endItem, inp)
                startItem.addArrow(arrow)
                endItem.addArrow(arrow)
                arrow.setZValue(1)
                self.addItem(arrow)
                self.arrows.append(arrow)

        self.line = None
        super(Scene, self).mouseReleaseEvent(event)

    def isItemChange(self, type):
        for item in self.selectedItems():
            if isinstance(item, type):
                return True
        return False


def init():
    app = QtGui.QApplication(sys.argv)
    global MainWindow
    MainWindow = QtGui.QMainWindow()
    form = MyMainWindow()
    form.setupUi(MainWindow)
    return app, form, MainWindow

