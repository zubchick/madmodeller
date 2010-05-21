#!/usr/bin/env python
# -*- coding: utf-8 -*-

## autor: Зубков Никита Владимирович
## email: zubchik@gmail.com
## version: 0.1
## date: Sun May 16 21:52:32 2010

from base import Block

class Sum(Block):
    """ Сумматор  """
    def __init__(self, k=1):
        Block.__init__(self)

    name = u"Sum"
    doc = u'Складывает входящие сигналы'
    image = u'images/blocks/sum.png'

    def execute(self):
        pass
