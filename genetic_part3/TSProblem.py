# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving TSP example)
"""
from GASolver_module import GAProblem
import cities_module

class TSProblem(GAProblem):
    """Implementation of GAProblem for the traveling salesperson problem"""
    pass # REPLACE WITH YOUR CODE


if __name__ == '__main__':

    from GASolver_module import GASolver

    cities = cities_module.loadCities("cities.txt")
    problem = TSProblem()
    solver = GASolver(problem)
    solver.resetPopulation()
    solver.evolveUntil()
    cities_module.drawCities(cities, solver.getBestIndiv().chromosome)
