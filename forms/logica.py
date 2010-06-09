# -*- coding: utf-8 -*-

class Scheme(object):
    """ Класс - схема, производит все вычисления """
    def __init__(self, arr_list):
        self.step = 0.1 # пока захардкодим
        self.time = 10 # секунд
        self.arrows = arr_list
        self.points = set()
        for arrow in self.arrows:
            self.points.add(arrow.startItem)
            self.points.add(arrow.endItem)

    def simulation(self):
        """ жесткая процедура симуляции """
        if not self.arrows:
            print 'No arrows'
            return

        i = 0
        while i < self.time:
            self.uncolored()
            rounds = 0
            while not self.all_colored(): # or rounds < 10000: # 2 ** 20 - от балды
                for point in self.points:
                    if point.block.can and not point.colored:
                        point.block.time = i
                        point.block.execute()
                        point.colored = True
                        self.send_signals(point)
                rounds += 1
                if rounds > 10000:
                    break
            if not self.all_colored():
                print 'Iteration fault, check model'
                break
            i += self.step

    def uncolored(self):
        for point in self.points:
            point.colored = False

    def all_colored(self):
        for point in self.points:
            if point.colored == False:
                return False
        return True

    def send_signals(self, point):
        """ переписать полностью """
        for arrow in self.arrows:
            if arrow.startItem == point:
                arrow.endItem.block.inp_signals = point.block.out_signals
