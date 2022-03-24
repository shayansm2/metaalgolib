from abc import ABC
from typing import final

from src.algorithms.genetic.GeneticEncodedSolution import GeneticEncodedSolution
from src.algorithms.lib.EncodedSolutionBuilder import EncodedSolutionBuilder


@final
class GeneticEncodedSolutionBuilder(EncodedSolutionBuilder, ABC):
    def build(self, chromosome: any) -> GeneticEncodedSolution:
        encoded_solution = GeneticEncodedSolution()
        encoded_solution.set_chromosome(chromosome)
        decoded_solution = self.solutionBuilder.build(self.convertor.decode(chromosome))
        encoded_solution.set_cost_function_value(self.get_cost_function_value(decoded_solution))
        encoded_solution.set_decoded_solution(decoded_solution)
        return encoded_solution

    def get_cost_function_value(self, decoded_solution):
        return self.calculator.get_cost_function(decoded_solution.get_objective_function_value())
