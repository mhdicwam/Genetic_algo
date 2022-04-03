# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(generic genetic algorithm module)
"""
from math import floor


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


class GAProblem:
    """Defines a Genetic algorithm problem to be solved by GASolver"""

    # a genetic problem is defined by its genes and fitness and how you cross and mutate
    def __init__(self):
        self.getRandomChromosome()
        # fonction that calculate the fitness of a chromomosome
        self.getFitness()
        self.crossover()
        # the instance that handle the mutation of chromomosome
        self.mutation()


class GASolver:
    def __init__(self, problem: GAProblem, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a GASolver for a given GAProblem

        Args:
            problem (GAProblem): GAProblem to be solved by this GASolver
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._problem = problem
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    def resetPopulation(self, pop_size=50):
        """ Initialize the population with pop_size random Individuals """
        for i in range(pop_size):
            chromosome = self._problem.getRandomChromosome()
            fitness = self._problem.getFitness(chromosome)
            new_individual = Individual(chromosome, fitness)
            self._population.append(new_individual)

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
        for i in range(0, len(l_pop), 2):
            # select the parents two by two
            p1 = l_pop[i].chromosome
            p2 = l_pop[i + 1].chromosome
            for c in self._problem.crossover(p1, p2):
                c = self._problem.mutation(self._mutation_rate, c)
                fitness = self._problem.getFitness(c)
                new_children = Individual(c, fitness)
                l_pop.append(new_children)
        # update the population
        self._population = l_pop

    def showGenerationSummary(self):
        """ Print some debug information on the current state of the population """
        print(f"population length : {len(self._population)}")
        print(f"best individual :  {self.getBestIndividual()}")

    def getBestIndividual(self):
        """ Return the best Individual of the population """
        best_individual = self._population[0]
        return best_individual

    def getBestDNA(self):
        best_dna = self._population[0].chromosome
        return best_dna

    def evolveUntil(self, max_nb_of_generations=500, threshold_fitness=None):
        """ Launch the evolveForOneGeneration function until one of the two condition is achieved :
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        iteration = 0
        while iteration != max_nb_of_generations and self.getBestIndividual().fitness < threshold_fitness:
            iteration += 1
            self.evolveForOneGeneration()
