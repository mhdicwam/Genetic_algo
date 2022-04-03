# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving Mastermind example)
"""
from GASolver_module import GAProblem
import genetic_part1.mastermind_module as mm
import random as r


class MastermindProblem(GAProblem):
    """Implementation of GAProblem for the mastermind problem"""

    def __init__(self, this_match: mm.MastermindMatch):
        self.match = this_match

    def getRandomChromosome(self):
        return mm.generateRandomSecret(self.match.secretSize())

    def getFitness(self, this_chromosome):
        return self.match.rateGuess(this_chromosome)

    def crossover(self, p1, p2):
        # random cross point
        cross_point = r.randint(1, len(p1) - 1)
        # p2[:cross_point]
        ch1 = p1[:cross_point] + p2[cross_point:]
        ch2 = p2[:cross_point] + p1[cross_point:]
        return [ch1, ch2]

    def mutation(self, this_mutation_rate, this_children):
        for i in range(len(this_children)):
            # check for a mutation
            if r.random() < this_mutation_rate:
                # change the chromosome
                this_children[i] = 1 - this_children[i]
        return this_children


if __name__ == '__main__':

    from GASolver_module import GASolver

    match = mm.MastermindMatch(secretSize=6)
    print(match.secretSize())
    problem = MastermindProblem(match)
    solver = GASolver(problem)

    solver.resetPopulation()
    solver.evolveUntil()

    print(f'Shhhh here the secret code {match._secret}')
    print(
            f"Best guess {mm.decodeGuess(solver.getBestDNA())} {solver.getBestIndividual()}"
    )
    print(
            f"Problem solved? {match.isCorrect(solver.getBestIndividual().chromosome)}"
    )
