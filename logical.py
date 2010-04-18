#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Scheme(object):
    """Схема, агрегирует в себя блоки.
    """
    
    def __init__(self, name):
        self._name = name
        self.graph = []
        self.block_lst = []

    def create(self):
        """Создает матрицу смежности (self.graph)
        на основе block_lst
        
        """
        graph = []
        # Формируем многомерный список
        len_block_lst = len(self.block_lst)
        for i in xrange(len_block_lst):
            graph.append([0 for j in xrange(len_block_lst)])
            
        # Формируем матрицу
        for block in self.block_lst:
            for inpt in block.inputs:
                graph[inpt][self.index] = 1



class Stack(object):
    """Стек, обычный стек
    """
    
    def __init__(self):
        self._stack = []

    def is_empty(self):
        return len(self._stack) == 0
    
    def top(self):
        return self._stack[-1]

    def push(self, x):
        self._stack.append(x)

    def pop(self):
        return self._stack.pop()

    def __str__(self):
        return str(self._stack)

    def __len__(self):
        return len(self._stack)

    
class Vertex(object):
    """ Вершина графа """
    
    def __init__(self, value = 0):
        self._value = value
        self.color = 'white'
        

def stack_test():
    st = Stack()
    for i in xrange(0, 10, 2):
        st.push(i)
        if  i % 4 and not st.is_empty():
            print st.pop()
        print st
    
if __name__ == '__main__':
    stack_test()
