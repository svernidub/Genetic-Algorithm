#-*-coding: utf-8 -*-
import random
import itertools

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
        self.__sort()
        self.__calculate_probability()
        self.__select_parents()
        return self.__compile_pairs()


    def __sort(self):
        return self.population.sort(key=lambda i: i.y, reverse=True)


    def __calculate_probability(self):
        for i, ind in enumerate(self.population):
            ind.probability = self.__probability(i)

    def __probability(self, index):
        return (1.0 / self.__n) * \
               (self.__a - (self.__a - self.__b) * index / (self.__n - 1.0))


    def __select_parents(self):
        self.__parents = []

        for ind in self.population:
            if ind.probability >= self.__random_number():
                self.__parents.append(ind)


    def __compile_pairs(self):
        pairs = self.__pairwise(self.__parents)

        pairs_n = len(self.__parents)
        if pairs_n % 2 == 1:
            pairs.append([self.__parents[0], self.__parents[-1]])

        return pairs


    def __random_number(self):
        return random.random() / 10


    def __pairwise(self, parents):
        it = iter(parents)
        return list(itertools.izip(it,it))
