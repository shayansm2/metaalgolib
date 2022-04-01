from abc import ABC
from typing import final, Type

from src.algorithms.lib.AlgorithmCalculator import AlgorithmCalculator
from src.algorithms.lib.BaseAlgorithmCalculator import BaseAlgorithmCalculator
from src.algorithms.lib.EncodedSolution import EncodedSolution
from src.lib.FunctionObject import FunctionObject
from src.problems.lib.Convertor import Convertor
from src.problems.lib.SolutionBuilder import SolutionBuilder


@final
class EncodedSolutionBuilder(FunctionObject, ABC):
    def __init__(
            self,
            convertor: Convertor,
            solution_builder: SolutionBuilder,
            encoded_solution: Type[EncodedSolution],
            calculator: AlgorithmCalculator = BaseAlgorithmCalculator()
    ):
        self.convertor = convertor
        self.solutionBuilder = solution_builder
        self.encodedSolution = encoded_solution
        self.calculator = calculator

    def build(self, encoded_representation: any) -> EncodedSolution:
        encoded_solution = self.encodedSolution()
        encoded_solution.set_encoded_representation(encoded_representation)
        decoded_solution = self.solutionBuilder.build(self.convertor.decode(encoded_representation))
        encoded_solution.set_cost_function_value(self.get_cost_function_value(decoded_solution))
        encoded_solution.set_decoded_solution(decoded_solution)
        return encoded_solution

    def get_cost_function_value(self, decoded_solution):
        return self.calculator.get_cost_function(decoded_solution.get_objective_function_value())
