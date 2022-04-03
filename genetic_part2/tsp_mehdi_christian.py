# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:24:15 2022

@author: agademer & tdrumond
"""
import random as r
from math import floor

from genetic_part2 import cities_module

cities = cities_module.loadCities("cities.txt")


def crossover_tsp(p1: list, p2: list) -> list:
    # random cross point
    cross_point = r.randint(1, len(p1) - 1)
    # p2[:cross_point]
    chromosome = cities_module.defaultRoad(cities)
    ch1_tmp = list(set(p1[:cross_point] + p2[cross_point:]))  # get the unique values
    ch1 = ch1_tmp + [idx_city for idx_city in chromosome if
                     idx_city not in ch1_tmp]  # add the cities missing after rooting
    # out the duplicates
    ch2_tmp = list(set(p2[:cross_point] + p1[cross_point:]))
    ch2 = ch2_tmp + [idx_city for idx_city in chromosome if idx_city not in ch2_tmp]
    return [ch1, ch2]


# function to mutate the children
def mutation_tsp(this_mutation_rate, this_children):
    for i in range(len(this_children)):
        # check for a mutation
        if r.random() < this_mutation_rate:
            # change the position of a random gene with another
            k = r.randint(0, len(this_children) - 1)
            tmp = this_children[i]
            this_children[i] = this_children[k]
            this_children[k] = tmp

    return this_children


class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm 

        Args:
            chromosome (list[]): a list representing the individual's chromosome
            fitness (float): the individual's fitness (the higher, the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GASolver:
    def __init__(self, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a GASolver for a given GAProblem

        Args:
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    def resetPopulation(self, pop_size=52):
        """ Initialize the population with pop_size random Individuals """
        for i in range(pop_size):
            # chromosome : the index of the ordered list of the visited cities
            chromosome = cities_module.defaultRoad(cities)
            r.shuffle(chromosome)
            # The shorter the road, the higher the fitness is
            fitness = -cities_module.roadLength(cities, chromosome)
            new_individual = Individual(chromosome, fitness)
            self._population.append(new_individual)
        
    def test(self):
        self._population.sort(reverse=True)
        print(self._population)

    def evolveForOneGeneration(self):
        """ Apply the process for one generation : 
            -	Sort the population (Descending order)
            -	Remove x% of population (less adapted)
            -   Recreate the same quantity by crossing the surviving ones 
            -	For each new Individual, mutate with probability mutation_rate 
                i.e., mutate it if a random value is below mutation_rate"""

        pop_size = len(self._population)

        # sort the population by descending order
        self._population.sort(reverse=True)
        l_pop = self._population
        # extract the population with the highest fitness
        l_pop = l_pop[0:(floor(pop_size * self._selection_rate))]
        # crossing and mutation of the childrens
        for i in range(0, len(l_pop) - 1, 2):
            # select the parents two by two
            p1 = l_pop[i].chromosome
            p2 = l_pop[i + 1].chromosome
            for c in crossover_tsp(p1, p2):
                c = mutation_tsp(self._mutation_rate, c)
                # print(c)
                fitness = -cities_module.roadLength(cities, c)
                new_children = Individual(c, fitness)
                l_pop.append(new_children)
        # update the population
        self._population = l_pop

    def showGenerationSummary(self):
        """ Print some debug information on the current state of the population """
        print(f"the sorted populations : {self._population}")
        print(f"cities : {cities}")
        print(f"best individual :  {self.getBestIndividual()}")
        print(f"population length : {len(self._population)}")

    def getBestIndividual(self):
        """ Return the best Individual of the population """
        best_individual = self._population[0]
        return best_individual

    def evolveUntil(self, max_nb_of_generations=500):
        """ Launch the evolveForOneGeneration function until one of the two condition is achieved :
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        iteration = 0
        while iteration != max_nb_of_generations:
            iteration += 1
            self.evolveForOneGeneration()
            if iteration < 100:
                print(iteration)
                print(self._population)
