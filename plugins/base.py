#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Block(object):
    """ Блок, основной кирпичик программы """
    def __init__(self):
        self.index = 0
        # Индексы блоков с которых приходит(ят)/уходит(ят) сигналы
        # Номер в списке - это номер входа/выхода
        self.inputs = [] # с каких блоков приходит сигнал
        self.outputs = [] # на какие уходит. Индексы.

        self.inp_signals = {} # значения сигналов
        self.out_signals = {} # number:value = номер входа/выхода:значение
        self.type = ''
        self.defaults = {}

    name = "Anonimus" # Отображаемое имя блока

    def execute(self):
        """
        Основной метод, который должен быть
        переопределен потомками

        """
        pass
