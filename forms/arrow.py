# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import math

class Arrow(QtGui.QGraphicsLineItem):
    def __init__(self, startItem, endItem, parent=None, scene=None):
        super(Arrow, self).__init__(parent, scene)

        self.arrowHead = QtGui.QPolygonF()


        self.myStartItem = startItem
        self.myEndItem = endItem
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        self.myColor = QtCore.Qt.black
        self.setPen(QtGui.QPen(self.myColor, 2, QtCore.Qt.SolidLine,
                QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))

    @property
    def startItem(self):
        return self.myStartItem

    @property
    def endItem(self):
        return self.myEndItem

    def boundingRect(self):
        extra = (self.pen().width() + 20) / 2.0
        p1 = self.line().p1()
        p2 = self.line().p2()
        return QtCore.QRectF(p1, QtCore.QSizeF(p2.x() - p1.x(), p2.y() - p1.y())).normalized().adjusted(-extra, -extra, extra, extra)

    def shape(self):
        path = super(Arrow, self).shape()
        path.addPolygon(self.arrowHead)
        return path

    ## def updatePosition(self):
    ##     line = QtCore.QLineF(self.mapFromItem(self.myStartItem, 0, 0),
    ##                          self.mapFromItem(self.myEndItem, 0, 0))
    ##     self.setLine(line)

    def paint(self, painter, option, widget=None):
        if (self.myStartItem.collidesWithItem(self.myEndItem)):
            return

        myStartItem = self.myStartItem
        myEndItem = self.myEndItem
        myColor = self.myColor
        myPen = self.pen()
        arrowSize = 10.0
        painter.setPen(myPen)
        painter.setBrush(self.myColor)

        p1, p2 = myEndItem.back_points

        back_line = QtCore.QLineF(p1+ myEndItem.pos(), p2 + myEndItem.pos())
        in_number = 1 # потом надо будет получать это от пользователя
        in_count = 2 # потом надо будет получать от блока
        # Pi(x,y)=> x=x1; y = ((i/N+1)*(y2-y1)+y1)
        end_point = QtCore.QPointF(back_line.p1().x(),
                                   ((back_line.p2().y() - back_line.p1().y()) *
                                   (in_number / float(in_count + 1)) + back_line.p1().y()))

        self.setLine(QtCore.QLineF(end_point, myStartItem.pos()))

        # Рисуем наконечник!
        line = self.line()

        angle = math.acos(line.dx() / line.length())
        if line.dy() >= 0:
            angle = (math.pi * 2.0) - angle

        arrowP1 = line.p1() + QtCore.QPointF(math.sin(angle + math.pi / 3.0) * arrowSize,
                                        math.cos(angle + math.pi / 3) * arrowSize)
        arrowP2 = line.p1() + QtCore.QPointF(math.sin(angle + math.pi - math.pi / 3.0) * arrowSize,
                                        math.cos(angle + math.pi - math.pi / 3.0) * arrowSize)

        self.arrowHead.clear()
        for point in [line.p1(), arrowP1, arrowP2]:
            self.arrowHead.append(point)

        painter.drawLine(line)
        painter.drawPolygon(self.arrowHead)
        if self.isSelected():
            painter.setPen(QtGui.QPen(myColor, 1, QtCore.Qt.DashLine))
            myLine = QtCore.QLineF(line)
            myLine.translate(0, 4.0)
            painter.drawLine(myLine)
            myLine.translate(0,-8.0)
            painter.drawLine(myLine)
