# TSP
# chromosome = [list_of_all_cities]
# fitness = the shorter the road the higher the fitness

from tsp_mehdi_christian import GASolver, crossover_tsp

solver = GASolver()
l = crossover_tsp([4, 2, 3, 0, 5, 6, 8], [3, 4, 5, 8, 1, 2, 6])
print(l)
# solver.resetPopulation()
# solver.test()
