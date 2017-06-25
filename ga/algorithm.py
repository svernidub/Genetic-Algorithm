from initialize_population import InitializePopulation
from calculate_function_value import CalculateFunctionValue
from reproduction_selection import ReproductionSelection

class Algorithm:
    def __init__(self, fitness_function, x_min, x_max, population_size, mutation_probability):
        self.fitness_function = fitness_function
        self.x_min = x_min
        self.x_max = x.max
        self.population_size = population_size
        self.mutation_probability = mutation_probability
        
    
    def perform(self):
        self.__initialize_population()
        self.__calculate_function_value()
        self.__reproduction_selection()
        
    
    def __initialize_population(self):
        initializator = InitializePopulation(self.population_size, self.x_min, self.x_max)
        self.__population = initializator.perform()
        
    
    def __calculate_function_value(self):
        calculator = CalculateFunctionValue(self.__population, self.fitness_function)
        calculator.perform()
        
        
    def __reproduction_selection(self):
        reproductor = ReproductionSelection(self.__population)
        self.__parents = reproductor.perform()