#-*-coding: utf-8 -*-

class CalculateFunctionValue:
    """
    Оценивает значения фитнес функции для популяции
    """

    def __init__(self, population, fitness_function):
        """
        Получает два параметра - популяцию особей
        и фитнес функцию в виде лямбды
        """
        self.population = population
        self.fitness_function = fitness_function


    def perform(self):
        """
        Рассчитывает значение для каждой особи популяции
        Ничего не возвращает (массив передан по ссылке)
        """
        for i in self.population:
            i.y = self.fitness_function(i.x)
