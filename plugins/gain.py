# -*- coding: utf-8 -*-

## autor: Зубков Никита Владимирович
## email: zubchik@gmail.com
## version: 0.1
## date: 17.01.10

from base import Block

class Gain(Block):
    """ Усилитель """
    def __init__(self, k=1):
        Block.__init__(self)
        self.changek = k
        ## self.inputs = [None] # обозначаем что вход 1н
        ## self.outputs = [None] # обозначаем что выход 1н

    image = 'images/blocks/gain.png'
    name = u"Gain"
    doc = u"Увеличивает приходящий сигнал на постоянный коэффициент"
    def execute(self):
        """ На выходе сигнал умноженный на коэффициент усиления """
        self.out_signals[0] = self.changek * self.inp_signals[0]
