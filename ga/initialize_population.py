#-*-coding: utf-8 -*-

import numpy as np
from individual import Individual

class InitializePopulation:
    """
    Инициализирует исходную популяцию
    """

    def __init__(self, population_size, x_min, x_max):
        """
        Получает параметры - размер популяции, записывает его
        в поле класса, начало и конец интервала, на котором определена функция
        """
        self.population_size = population_size
        self.x_min = x_min
        self.x_max = x_max

    def perform(self):
        """
        Выполняет инициализацию популяции и возвращает ее
        """

        return map(self.__initialize_individual, self.__initialize_by_x())


    def __initialize_by_x(self):
        return np.random.uniform(self.x_min, self.x_max, self.population_size)

    def __initialize_individual(self, x):
        return Individual(x)
