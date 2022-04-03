# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving Mastermind example)
"""
from GASolver_module import GAProblem
import mastermind_module as mm


class MastermindProblem(GAProblem):
    """Implementation of GAProblem for the mastermind problem"""
    pass  # REPLACE WITH YOUR CODE


if __name__ == '__main__':

    from GASolver_module import GASolver

    match = mm.MastermindMatch(secretSize=6)
    problem = MastermindProblem(match)
    solver = GASolver(problem)

    solver.resetPopulation()
    solver.evolveUntil()

    print(
        f"Best guess {mm.decodeGuess(solver.getBestDNA())} {solver.getBestIndividual()}")
    print(
        f"Problem solved? {match.isCorrect(solver.getBestIndividual().chromosome)}")
