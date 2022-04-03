# TSP
# chromosome = [list_of_all_cities]
# fitness = the shorter the road the higher the fitness
from genetic_part2 import cities_module
from tsp_mehdi_christian import GASolver, crossover_tsp

cities = cities_module.loadCities("cities.txt")

solver = GASolver()
solver.resetPopulation()

solver.test()
solver.evolveUntil()

# You can plot the best path found by calling:
best = solver.getBestIndividual()
solver.showGenerationSummary()
cities_module.drawCities(cities, best.chromosome)
