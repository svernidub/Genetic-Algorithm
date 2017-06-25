import numpy as np
from initialize_population import InitializePopulation
from calculate_function_value import CalculateFunctionValue
from reproduction_selection import ReproductionSelection
from crossingover import Crossingover
from mutation import Mutation
from append_childs import AppendChilds
from reduction import Reduction
from plot import Plot

class Algorithm:
    def __init__(self, fitness_function, x_min, x_max, population_size,
                mutation_probability, epochs):
        self.fitness_function = fitness_function
        self.x_min = x_min
        self.x_max = x_max
        self.population_size = population_size
        self.mutation_probability = mutation_probability
        self.epochs = epochs


    def perform(self):
        self.__init_plot()
        self.__initialize_population()
        self.__calculate_function_value(self.__population)

        for epoch in range(0, self.epochs):
            self.__reproduction_selection()
            self.__crossingover()
            self.__mutation()
            self.__calculate_function_value(self.__childs)
            self.__append_childs()
            self.__reduction()
            self.__draw_to_plot()
            self.__debug(epoch)

        self.__finalize_plot()


    def __initialize_population(self):
        initializator = InitializePopulation(self.population_size,
                                             self.x_min, self.x_max)
        self.__population = initializator.perform()


    def __calculate_function_value(self, individuals):
        calculator = CalculateFunctionValue(individuals,
                                            self.fitness_function)
        calculator.perform()


    def __reproduction_selection(self):
        reproductor = ReproductionSelection(self.__population)
        self.__parents = reproductor.perform()


    def __crossingover(self):
        crosser = Crossingover(self.__parents)
        self.__childs = crosser.perform()


    def __mutation(self):
        mutator = Mutation(self.__childs, self.mutation_probability)
        mutator.perform()


    def __append_childs(self):
        appender = AppendChilds(self.__population, self.__childs)
        appender.perform()


    def __reduction(self):
        reductor = Reduction(self.__population, self.population_size,
                             self.x_min, self.x_max)
        reductor.perform()


    def __debug(self, epoch):
        print 'Epoch ', epoch, ':\t', self.__population[0]


    def __init_plot(self):
        self.__plot = Plot(self.fitness_function, self.x_min, self.x_max)


    def __draw_to_plot(self):
        self.__plot.update_points(self.__population)


    def __finalize_plot(self):
        self.__plot.finalize()



import math
func = lambda x: np.sin(x*2)-x*x/100+x/3

a = Algorithm(func, 0, 10, 20, 0.02, 100)
a.perform()
