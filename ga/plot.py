#-*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

class Plot:
    def __init__(self, fitness_function, x_min, x_max):
        self.fitness_function = fitness_function
        self.x_min = x_min
        self.x_max = x_max
        self.__init_data()
        self.__init()


    def update_points(self, individuals):
        plt.clf()
        self.__init()
        x = map(lambda ind: ind.x, individuals)
        y = map(lambda ind: ind.y, individuals)
        plt.plot(x, y, 'ro')
        plt.draw()
        plt.pause(0.01)


    def finalize(self):
        plt.show()


    def __init(self):
        plt.grid(True)
        plt.plot(self.__x_axis, self.__y_axis)
        plt.ion()
        plt.show()


    def __init_data(self):
        self.__x_axis = np.arange(self.x_min, self.x_max, 0.1)
        self.__y_axis = self.fitness_function(self.__x_axis)
