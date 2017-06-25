#-*-coding: utf-8 -*-

class AppendChilds:
    """
    Добавляет потомков в исходную популяцию
    """

    def __init__(self, population, childs):
        """
        Получает исходную популяцию и массив потомков
        """
        self.population = population
        self.childs = childs


    def perform(self):
        """
        Добавляет потомков в популяцию
        """
        self.population += self.childs
