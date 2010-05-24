#!/usr/bin/env python
# -*- coding: utf-8 -*-

## autor: Зубков Никита Владимирович
## email: zubchik@gmail.com
## version: 0.1
## date: Sun May 16 21:34:10 2010

from base import Block

class Splitter(Block):
    """ Разветвитель """
    def __init__(self, out=2):
        Block.__init__(self)
        self.out = out

    name = u"Splitter"
    doc = u'Разделяет сигнал на несколько одинаковых'
    image = u'images/blocks/splitter.png'

    def execute(self):
        pass

