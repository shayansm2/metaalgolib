from abc import ABC

from src.algorithms.lib.AlgorithmCalculator import AlgorithmCalculator


class BaseAlgorithmCalculator(AlgorithmCalculator):
    def get_cost_function(self, objective_function: float):
        return objective_function
