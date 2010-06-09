# -*- coding: utf-8 -*-

## autor: Зубков Никита Владимирович
## email: zubchik@gmail.com
## version: 0.1
## date: Wed Jun  9 21:09:35 2010

from base import Block
import math

class Sin(Block):
    """ Блок косинус """
    image = 'images/blocks/sin.png'
    name = u"Sin"
    doc = u"Функция синуса"
    def execute(self):
        self.out_signals[0] = math.sin(self.inp_signals[0])
