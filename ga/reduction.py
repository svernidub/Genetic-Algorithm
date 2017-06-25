#-*-coding: utf-8 -*-

class Reduction:
    """
    Сокращает популяцию
    """

    def __init__(self, population, population_size, x_min, x_max):
        """
        Принимает популяцию с потомками
        """
        self.population = population
        self.population_size = population_size
        self.x_min = x_min
        self.x_max = x_max


    def perform(self):
        """
        Сокращает популяцию
        """
        self.__kill_outgoing()
        self.__sort()
        for ind in self.population[self.population_size:]:
            self.population.remove(ind)


    def __kill_outgoing(self):
        for ind in self.population:
            if ind.x < self.x_min or ind.x > self.x_max:
                self.population.remove(ind)

    def __sort(self):
        return self.population.sort(key=lambda ind: ind.y, reverse=True)
