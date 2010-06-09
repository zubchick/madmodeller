# -*- coding: utf-8 -*-

class Block(object):
    """ Блок, основной кирпичик программы """
    def __init__(self):
        self.index = 0
        # Индексы блоков с которых приходит(ят)/уходит(ят) сигналы
        # Номер в списке - это номер входа/выхода
        self.inputs = [] # с каких блоков приходит сигнал
        self.outputs = [] # на какие уходит. Индексы.

        self._inp = 1
        self._out = 1
        self.inp_signals = [None] # значения сигналов
        self.out_signals = [None] # number:value = номер входа/выхода:значение
        self.type = ''
        self.defaults = {}
        self.pure = True
        self.time = 0
        # Все свойства, которым можно изменить через форму,
        # которая появляется по двойному клику на блоке,
        # должны иметь префикс "change" или "_change".
        # Пример:
        # self.changeTestValue = 666 # будет отображаться как TestValue

    name = u"Anonimus" # Отображаемое имя блока
    doc = u'Если вы видите эту надпись, значит у блока нет doc-строки'
    image = "images/blocks/default_block.png" # картинка блока

    @property
    def inp(self):
        """ Возвращает количество сигналов, которые может принимать блок
        """
        return self._inp

    @inp.setter
    def inp(self, value):
        if value > 0:
            self._inp = value

    @property
    def out(self):
        """ Возвращает количество сигналов, которые может отдавать блок
        """
        return self._out

    @inp.setter
    def out(self, value):
        if value >= 0:
            self._out = value

    @property
    def can(self):
        if None in self.inp_signals:
            return False
        else:
            return True

    def get_out(self):
        """ Возвращает информацию о исходящих значениях
        в текстовом виде. """
        string = u'<b>%s</b>' % self.name
        ## for key, value in self.out_signals.items():
        ##     string += u'<b>{0}:</b> {1}\n'.format(key, value)
        return string

    def get_params(self):
        """ Возвращает список параметров, которые можно менять в блоке.
        Свойство не должно входить в базовый блок, а так же
        должно начинаться со слова 'change' или '_change'.

        """
        # ключи базового блока
        base_key_list = Block().__dict__.keys()
        # ключи изменяемых параметров
        ret_key_list = [key for key in self.__dict__ if (key not in base_key_list
                                                          and (key.startswith('change') or
                                                          key.startswith('_change')))]
        strip_key_list = map(lambda x: x.lstrip('_'), ret_key_list)
        # значения изменяемых параметров
        ret_value_list = [self.__dict__[key] for key in ret_key_list]
        return dict(zip(strip_key_list, ret_value_list))

    def execute(self):
        """
        Основной метод, который должен быть
        переопределен потомками

        """
        pass
