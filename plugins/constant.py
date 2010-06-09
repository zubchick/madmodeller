# -*- coding: utf-8 -*-

## autor: Зубков Никита Владимирович
## email: zubchik@gmail.com
## version: 0.1
## date: 6.06.10

from base import Block

class Constant(Block):
    """ Усилитель """
    image = 'images/blocks/constant.png'
    name = u"Constant"
    doc = u"Испускает постоянный сигнал"

    def __init__(self):
        Block.__init__(self)
        self.changeConstant = 1
        self.inp = 0
        self.inp_signals = [self.changeConstant] # значение по умолчанию

    def execute(self):
        self.out_signals[0] = self.changeConstant
