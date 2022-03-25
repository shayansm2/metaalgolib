from src.algorithms.lib.EncodedSolution import EncodedSolution
from src.algorithms.lib.population.Population import Population


class BasePopulation(Population):
    def __init__(self):
        self.population = []

    def insert(self, individual: EncodedSolution):
        self.population.append(individual)

    def insert_many(self, individuals: list[EncodedSolution]):
        self.population += individuals

    def get_best_answer(self) -> EncodedSolution:
        assert self.population != [], 'population is empty'

        best = self.population[0]
        best: EncodedSolution
        min_cost = best.get_cost_function_value()

        for individual in self.population:
            individual: EncodedSolution
            if min_cost < individual.get_cost_function_value():
                best, min_cost = individual, individual.get_cost_function_value()

        return best
