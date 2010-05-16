#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import inspect

import plugins.base

def load(plugin_dir="plugins"):
    """
    Процедура подгрузки плагинов из plugin_dir
    возвращает {Имя-плагина:Класс, ...}

    """

    class_list = set()
    class_name_list = set()
    # Сюда добавляем имена загруженных модулей
    modules = []

    # Перебирем файлы в папке plugins
    print "Load plugins:"
    for fname in os.listdir(plugin_dir):

        # Нас интересуют только файлы с расширением .py
        if fname.endswith(".py"):

            # Обрежем расширение .py у имени файла
            module_name = fname[: -3]

            # Пропустим файлы base.py и __init__.py
            if module_name != "base" and module_name != "__init__":
                print "\tLoad module %s" % fname

                # Загружаем модуль и добавляем его имя в список загруженных модулей
                package_obj = __import__(plugin_dir + "." +  module_name)
                modules.append(module_name)
            else:
                print "\tSkip " + fname

    print "\nLoad Classes:"
    # Перебираем загруженные модули
    for modulename in modules:
        module_obj = getattr(package_obj, modulename)

        # Перебираем все, что есть внутри модуля
        for elem in dir(module_obj):
            obj = getattr(module_obj, elem)

            # Это класс?
            if inspect.isclass(obj):

                # Класс производный от baseplugin?
                if (issubclass(obj, plugins.base.Block)): #and obj != plugins.base.Block):
                    class_list.add(obj)
                    class_name_list.add(obj.name)
                    print '\tLoad Class ', objx

    return dict(zip(class_name_list, class_list))

if __name__ == '__main__':
    print load()
