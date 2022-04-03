from gas_solver_christian_Mehdi import GASolver

import mastermind_module as mm

# mastermind game --------------------------
match = mm.MastermindMatch(secretSize=4)
solver = GASolver(match)
solver.resetPopulation()

# solver.test()
solver.evolveUntil(threshold_fitness=match.maxScore())
# print(match.maxScore())
solver.evolveForOneGeneration()
best = solver.getBestIndividual()
#
# # match.test()
# match.test()
print(f"the right answer ")
solver.test()
print(best.chromosome)
print(f"Best guess {mm.decodeGuess(best.chromosome)}")
print(f"Problem solved? {match.isCorrect(best.chromosome)}")
