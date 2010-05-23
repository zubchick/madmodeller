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

    name = u"Anonimus" # Отображаемое имя блока
    doc = u'Если вы видите эту надпись, значит у блока нет doc-строки'
    image = "images/blocks/default_block.png"

    def get_out(self):
        """ Возвращает информацию о исходящих значениях
        в текстовом виде """
        string = u'<b>%s</b>\n' % self.name
        for key, value in self.out_signals.items():
            string += u'<b>{0}:</b> {1}\n'.format(key, value)
        return string

    def get_params(self):
        """ Возвращает список параметров, которые можно менять в блоке """
        base = Block()
        base_key_list = [key for key in base.__dict__]
        ret_key_list =  [key for key in self.__dict__ if key not in base_key_list]
        ret_value_list = [self.__dict__[key] for key in ret_key_list]
        return dict(zip(ret_key_list, ret_value_list))

    def execute(self):
        """
        Основной метод, который должен быть
        переопределен потомками

        """
        pass
