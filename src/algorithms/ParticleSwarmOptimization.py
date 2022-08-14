from __future__ import annotations

from abc import abstractmethod
from typing import Type

from src.Enums import Enums
from src.algorithms.lib.EncodedSolution import EncodedSolution
from src.algorithms.lib.Operators import Operators
from src.algorithms.lib.PopulationBasedAlgorithm import PopulationBasedAlgorithm


class PSOEncodedSolution(EncodedSolution):
    def __init__(self):
        super().__init__()
        self.velocity = None
        self.position = None
        self.bestAns = None

    def set_position(self, position: list):
        self.position = position
        return self

    def get_position(self) -> list:
        return self.position

    def set_velocity(self, velocity: list):
        self.velocity = velocity
        return self

    def get_velocity(self) -> list:
        return self.velocity

    def set_best_ans(self, best_ans: PSOEncodedSolution):
        self.bestAns = best_ans
        return self

    def get_best_ans(self):
        return self.bestAns

    def get_encoded_representation(self) -> dict:
        return {
            'position': self.get_position(),
            'velocity': self.get_velocity(),
            'best_ans': self.get_best_ans(),
        }

    def set_encoded_representation(self, encoded_representation: dict):
        self.position = encoded_representation.get('position', None)
        self.velocity = encoded_representation.get('velocity', None)
        self.bestAns = encoded_representation.get('best_ans', None)
        return self


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
        w = self.hyperParameter.get(Enums.hyperParam.psoInertiaWeight)
        assert 0 <= w <= 1, 'inertia_weight should be between o and 1'

        if not self.hyperParameter.exists(Enums.hyperParam.psoInertiaWeightDecay):
            self.hyperParameter.set(Enums.hyperParam.psoInertiaWeightDecay, 1)

    def init_first_population(self, *args):
        pass

    def run_per_generation(self, *args):
        pass

    def create_random_solutions(self, count) -> list:
        self.operators = PSOOperators

        particles = []
        for _ in range(count):
            particles.append(self.operators.random_generator(self.problem))
