#-*-coding: utf-8 -*-

class Individual:
    """
    Класс особи популяции
    """


    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


    def genes(self):
        """
        Возвращает массив генов 1/0
        """
        None
        
    def __str__(self):
        return "(" + str(self.x) + ", " +  str(self.y) + ")"