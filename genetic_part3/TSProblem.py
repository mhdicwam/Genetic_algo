# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving TSP example)
"""
from GASolver_module import GAProblem

from genetic_part2 import cities_module
import random as r

from genetic_part2.cities_module import roadLength


class TSProblem(GAProblem):
    """Implementation of GAProblem for the traveling salesperson problem"""

    def __init__(self, this_cities):
        self.cities = this_cities

    def getRandomChromosome(self):
        chromosome = cities_module.defaultRoad(self.cities)
        r.shuffle(chromosome)
        return chromosome

    # The shorter the road, the higher the fitness is

    def getFitness(self, this_chromosome):
        fitness = -cities_module.roadLength(self.cities, this_chromosome)
        return fitness

    def crossover(self, p1: list, p2: list) -> list:
        # random cross point
        cross_point = r.randint(1, len(p1) - 1)
        # p2[:cross_point]
        chromosome = cities_module.defaultRoad(cities)
        ch1_tmp = list(set(p1[:cross_point] + p2[cross_point:]))  # get the unique values
        ch1 = ch1_tmp + [idx_city for idx_city in chromosome if
                         idx_city not in ch1_tmp]  # add the cities missing after rooting out the duplicates
        ch2_tmp = list(set(p2[:cross_point] + p1[cross_point:]))
        ch2 = ch2_tmp + [idx_city for idx_city in chromosome if idx_city not in ch2_tmp]
        return [ch1, ch2]

    # function to mutate the children
    def mutation(self, this_mutation_rate, this_children):
        for i in range(len(this_children)):
            # check for a mutation
            if r.random() < this_mutation_rate:
                # change the position of a random gene with another
                k = r.randint(0, len(this_children) - 1)
                tmp = this_children[i]
                this_children[i] = this_children[k]
                this_children[k] = tmp

        return this_children


if __name__ == '__main__':

    from GASolver_module import GASolver

    cities = cities_module.loadCities("cities.txt")
    problem = TSProblem(cities)
    solver = GASolver(problem)
    solver.resetPopulation()
    solver.evolveUntil()

    best = solver.getBestIndividual()
    road = cities_module.defaultRoad(cities)
    r.shuffle(road)
    print(
            f"the length of the random road :{road}:{roadLength(cities, road)} km\nthe length of the path after applying the "
            f"genetic algo : {best.chromosome} : {roadLength(cities, best.chromosome)} km\nwe shortened the path by "
            f"{roadLength(cities, road) - roadLength(cities, best.chromosome)} km "
    )

    cities_module.drawCities(cities, solver.getBestIndividual().chromosome)
