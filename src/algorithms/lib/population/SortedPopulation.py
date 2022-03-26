from abc import ABC

from src.algorithms.lib.population.Population import Population
from src.lib.BinarySearchTree import BinarySearchTree


class SortedPopulation(Population, ABC):  # remove ABC later
    def __init__(self):
        self.population = BinarySearchTree()
