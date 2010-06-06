# -*- coding: utf-8 -*-

## autor: Зубков Никита Владимирович
## email: zubchik@gmail.com
## version: 0.1
## date: Sun May 16 21:52:32 2010

from base import Block

class Sum(Block):
    """ Сумматор  """
    name = u"Sum"
    doc = u'Складывает входящие сигналы'
    image = u'images/blocks/sum.png'

    def __init__(self, k=1):
        Block.__init__(self)
        self._changeInput = self.inp

    @property
    def changeInput(self):
        return self._changeInput

    @changeInput.setter
    def changeInput(self, value):
        self.inp = value
        self._changeInput = self.inp

    def execute(self):
        pass
