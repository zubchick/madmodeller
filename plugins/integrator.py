#!/usr/bin/env python
# -*- coding: utf-8 -*-

## autor: Зубков Никита Владимирович
## email: zubchik@gmail.com
## version: 0.1
## date: Sun May 16 21:33:40 2010

from base import Block

class Integrator(Block):
    """ Интегратор """
    def __init__(self, k=1):
        Block.__init__(self)

    name = u"Integrator"
    doc = u'Интегратор интегрирует интегрированные интегралы'

    def execute(self):
        pass

