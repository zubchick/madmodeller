# -*- coding: utf-8 -*-

## autor: Зубков Никита Владимирович
## email: zubchik@gmail.com
## version: 0.1
## date: Sun May 16 21:33:40 2010

from base import Block

class Integrator(Block):
    """ Интегратор """
    name = u"Integrator"
    doc = u'Интегратор производит численное интегрирование'
    image = 'images/blocks/integrator.png'

    def __init__(self, k=1):
        Block.__init__(self)

    def execute(self):
        self.out_signals[0] = self.inp_signals[0] * self.time
