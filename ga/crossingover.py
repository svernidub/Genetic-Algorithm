#-*-coding: utf-8 -*-

import random
from individual import Individual

class Crossingover:
    """
    Осуществляет скрещивание (кроссинговер) пар
    родителей
    """

    def __init__(self, parents_pairs):
        """
        Получает массив пар родителей
        """
        self.parents = parents_pairs


    def perform(self):
        """
        Возвращает массив особей-потомков родителей
        """
        childs = []
        for pair in self.parents:
            for c in self.__cross(pair):
                childs.append(c)
        return childs


    def __cross(self, pair):
        genes1 = pair[0].genes()
        genes2 = pair[1].genes()

        genes1_start, genes1_end = self.__split(genes1)
        genes2_start, genes2_end = self.__split(genes2)

        return [self.__make_individual(genes1_start + genes2_end),
                self.__make_individual(genes2_start + genes1_end)]


    def __make_individual(self, genes):
        ind = Individual()
        ind.load_genes(genes)
        return ind



    def __split(self, genes):
        point = self.__crossing_point(genes)
        return [genes[:point], genes[point:]]


    def __crossing_point(self, genes):
        return len(genes) / 2
