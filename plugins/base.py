#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Block(object):
    """ Блок, основной кирпичик программы """
    def __init__(self):
        self.index = 0
        self.inputs = []
        self.outputs = []
        self.type = ''
        self.defaults = {}

    def execute(self):
        """Основной метод, который должен быть
        переопределен потомками
        
        """
        pass
