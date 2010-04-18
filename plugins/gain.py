#!/usr/bin/env python
# -*- coding: utf-8 -*-

## autor: Зубков Никита Владимирович
## email: zubchik@gmail.com
## version: 0.1
## date: 17.01.10

import base

class Gain(base.Block):
    """Усилитель
    """
    
    def __init__(self, k=1):
        self._k = k
        base.Block.__init__()

    def execute(self):
        pass
