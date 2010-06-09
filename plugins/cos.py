# -*- coding: utf-8 -*-

## autor: Зубков Никита Владимирович
## email: zubchik@gmail.com
## version: 0.1
## date: Wed Jun  9 21:09:35 2010

from base import Block
import math

class Cos(Block):
    """ Блок косинус """
    image = 'images/blocks/cos.png'
    name = u"Cos"
    doc = u"Функция косинуса"
    def execute(self):
        self.out_signals[0] = math.cos(self.inp_signals[0])
