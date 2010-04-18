#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import inspect


plugin_dir = "plugins"

import plugins.base

# Сюда добавляем имена загруженных модулей
modules = []

# Перебирем файлы в папке plugins
for fname in os.listdir(plugin_dir):

        # Нас интересуют только файлы с расширением .py
        if fname.endswith (".py"):

                # Обрежем расширение .py у имени файла
                module_name = fname[: -3]

                # Пропустим файлы base.py и __init__.py
                if module_name != "base" and module_name != "__init__":
                        print "Load module %s" % module_name

                        # Загружаем модуль и добавляем его имя в список загруженных модулей
                        package_obj = __import__(plugin_dir + "." +  module_name)
                        modules.append (module_name)

                        print "dir(package_obj) = " + str (dir(package_obj) )
                        print
                else:
                        print "Skip " + fname

# Перебираем загруженные модули
for modulename in modules:
        module_obj = getattr (package_obj, modulename)
        print modulename
        print dir (module_obj)

        # Перебираем все, что есть внутри модуля
        for elem in dir (module_obj):
                obj = getattr (module_obj, elem)

                # Это класс?
                if inspect.isclass (obj):

                        # Класс производный от baseplugin?
                        if issubclass (obj, plugins.base.Block):
                                # Создаем экземпляр и выполняем функцию run
                                a = obj()
                                a.run()
                                print
