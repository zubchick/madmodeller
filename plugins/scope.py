# -*- coding: utf-8 -*-

## autor: Зубков Никита Владимирович
## email: zubchik@gmail.com
## version: 0.1
## date: 6.06.10

from base import Block
import matplotlib.pyplot as plt

class Scope(Block):
    """ Вывод графика изменяющегося параметра во времени  """
    image = 'images/blocks/scope.png'
    name = u"Scope"
    doc = u"Отображает график изменяющегося параметра"

    def __init__(self):
        Block.__init__(self)
        self.pure = False
        self.x = []
        self.y = []
        self.out = 0

    def execute(self):
        self.x.append(self.time)
        self.y.append(self.inp_signals[0])

    def show(self):
        ## plt.title('My first normal plot')  # название графика
        plt.xlabel(u'Время')
        plt.ylabel(u'Значение')
        plt.plot(self.x, self.y)
        plt.show()
