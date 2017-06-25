#-*-coding: utf-8 -*-
import math
import random
import itertools
from functools import reduce

class ReproductionSelection:
    """
    Осуществляет выбор родителей для размножения
    """

    def __init__(self, population):
        """
        Получает исходную популяцию
        """
        self.population = population
        self.__n = len(population)
        self.__a = random.random() + 1
        self.__b = 2 - self.__a


    def perform(self):
        """
        Возвращает отобранные пары родителей для кроссинговера
        [[ind1, ind2], [ind3, ind4]]
        """
        self.__calculate_probability()
        self.__select_parents()
        return self.__compile_pairs()


    def __sort(self):
        return self.population.sort(key=lambda i: i.y, reverse=True)


    def __calculate_probability(self):
        self.__probabilities = []
        common = 0
        for ind in self.population:
            common += ind.y

        prob = 0
        for ind in self.population:
            prob += ind.y / common
            self.__probabilities.append([ind, prob])


    def __select_parents(self):
        self.__parents = []
        pairs_n = int(math.ceil(len(self.population) * 1))
        for n in range(0, pairs_n):
            r = random.random()

            for prb in self.__probabilities:
                if prb[1] >= r:
                    self.__parents.append(prb[0])
                    break




    def __compile_pairs(self):
        pairs = self.__pairwise(self.__parents)

        pairs_n = len(self.__parents)
        if pairs_n % 2 == 1:
            pairs.append([self.__parents[0], self.__parents[-1]])

        return pairs


    def __pairwise(self, parents):
        it = iter(parents)
        return list(itertools.izip(it,it))
