# TSP
# chromosome = [list_of_all_cities]
# fitness = the shorter the road the higher the fitness
from random import shuffle

from genetic_part2.cities_module import loadCities, defaultRoad, drawCities, roadLength
from tsp_mehdi_christian import GASolver, crossover_tsp

cities = loadCities("cities.txt")
print(f"the cities : {cities}")
road = defaultRoad(cities)
# road.reverse()
shuffle(road)
print(f"the random road :{road}")
# drawCities(cities, road)

solver = GASolver()
solver.resetPopulation()
solver.evolveUntil()
best = solver.getBestIndividual()

print(
        f"the length of the random road :{roadLength(cities, road)} km\nthe length of the path after applying the "
        f"genetic algo : {best.chromosome} : {roadLength(cities, best.chromosome)} km\nwe shortened the path by "
        f"{roadLength(cities, road) - roadLength(cities, best.chromosome)} km "
)

drawCities(cities, best.chromosome)
