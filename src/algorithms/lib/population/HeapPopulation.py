from src.algorithms.lib.population.Population import Population
import heapq


class HeapPopulation(Population):
    def __init__(self):
        self.population = []
        heapq.heapify(self.population)  # todo remove this after implementation
