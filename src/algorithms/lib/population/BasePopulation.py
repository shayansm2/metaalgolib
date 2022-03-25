import random

import numpy as np

from src.algorithms.lib.EncodedSolution import EncodedSolution
from src.algorithms.lib.population.Population import Population


class BasePopulation(Population):
    def __init__(self):
        self.population = []
        self.is_sorted = False

    def insert(self, individual: EncodedSolution):
        self.population.append(individual)
        self.is_sorted = False

    def insert_many(self, individuals: list[EncodedSolution]):
        self.population += individuals
        self.is_sorted = False

    def get_best_answer(self) -> EncodedSolution:
        assert self.population != [], 'population is empty'

        best = self.population[0]
        best: EncodedSolution
        min_cost = best.get_cost_function_value()

        if self.is_sorted:
            return best

        for individual in self.population:
            individual: EncodedSolution
            if min_cost < individual.get_cost_function_value():
                best, min_cost = individual, individual.get_cost_function_value()

        return best

    def get_random_individuals(self, count: int) -> list[EncodedSolution]:
        assert self.population != [], 'population is empty'
        assert count < len(self.population), 'count is more than population'

        indices = random.sample(range(len(self.population)), count)
        return list(np.array(self.population)[indices])

    def get_top_individuals(self, count: int) -> list[EncodedSolution]:
        assert self.population != [], 'population is empty'
        assert count < len(self.population), 'count is more than population'

        self.population.sort(key=lambda x: x.get_cost_function_value(), reverse=True)
        self.is_sorted = True
        return self.population[:count]

    def keep_top_individuals(self, count: int):
        count = min(count, len(self.population))
        self.population.sort(key=lambda x: x.get_cost_function_value(), reverse=True)
        self.is_sorted = True
        self.population = self.population[:count]
