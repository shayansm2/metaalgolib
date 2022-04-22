from abc import abstractmethod
from typing import Type

from src.Enums import Enums
from src.algorithms.lib.EncodedSolution import EncodedSolution
from src.algorithms.lib.Operators import Operators
from src.algorithms.lib.PopulationBasedAlgorithm import PopulationBasedAlgorithm


class PSOEncodedSolution(EncodedSolution):
    def __init__(self):
        super().__init__()
        self.bestCostFunctionValue = None
        self.bestPosition = None
        self.velocity = None
        self.position = None

    def set_position(self, position: list):
        self.position = position
        return self

    def get_position(self) -> list:
        return self.position

    def get_encoded_representation(self):
        return self.get_position()

    def set_encoded_representation(self, encoded_representation: any):
        return self.set_position(encoded_representation)

    def set_velocity(self, velocity: list):
        self.velocity = velocity
        return self

    def get_velocity(self) -> list:
        return self.velocity

    def set_best_position(self, best_position: list):
        self.bestPosition = best_position
        return self

    def get_best_position(self) -> list:
        return self.bestPosition

    def set_best_cost_function_value(self, value: float):
        self.bestCostFunctionValue = value
        return self

    def get_best_cost_function_value(self) -> float:
        return self.bestCostFunctionValue


class PSOOperators(Operators):
    @staticmethod
    @abstractmethod
    def subtraction(vendor1: any, vendor2: any):
        pass


class ParticleSwarmOptimizationAlgorithm(PopulationBasedAlgorithm):
    def get_algorithm_name(self) -> str:
        return Enums.algo.pso

    def get_algorithm_encoded_solution(self) -> Type[EncodedSolution]:
        return PSOEncodedSolution

    def get_algorithm_operator(self) -> Type[Operators]:
        return PSOOperators

    def init_hyper_parameters(self):
        pass

    def run_per_generation(self, *args):
        pass
