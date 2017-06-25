#-*-coding: utf-8 -*-

import math
import random

from individual import Individual

class Mutation:
    """
    Производит мутацию у потомков
    """

    def __init__(self, childs, probability):
        """
        Получает массив особей-потомков и вероятность мутации
        """
        self.childs = childs
        self.probability = probability


    def perform(self):
        """
        Выполняет мутацию с заданной вероятностью
        """
        for i, ind in enumerate(self.childs):
            self.__mutate(i, ind)


    def __mutate(self, i, ind):
        if not self.__will_mutate(): return

        genes = list(ind.genes())
        mutation_gen = int(math.floor(random.random() * len(genes)))
        genes[mutation_gen] = str(1 -int(genes[mutation_gen]))
        ind = Individual()
        ind.load_genes(''.join(genes))
        self.childs[i] = ind

    def __will_mutate(self):
        return random.random() <= self.probability
