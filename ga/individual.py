#-*-coding: utf-8 -*-

import struct

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
        return bin(struct.unpack('!i',struct.pack('!f',1.0))[0])[2:]


    def load_genes(self, genes):
        integer = int(genes, 2)
        hex = struct.pack('!i', integer)
        return struct.unpack('!f', hex)[0]


    def __str__(self):
        return "(" + str(self.x) + ", " +  str(self.y) + ")"
