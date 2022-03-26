from abc import ABC

from src.algorithms.lib.population.Population import Population
import heapq


class HeapPopulation(Population, ABC):  # remove ABC later
    def __init__(self):
        self.population = []
        heapq.heapify(self.population)  # todo remove this after implementation
