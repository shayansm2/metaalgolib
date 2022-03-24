from abc import ABC, abstractmethod

from src.algorithms.lib.AlgorithmCalculator import AlgorithmCalculator
from src.algorithms.lib.EncodedSolution import EncodedSolution
from src.lib.FunctionObject import FunctionObject
from src.problems.lib.Convertor import Convertor
from src.problems.lib.SolutionBuilder import SolutionBuilder


class EncodedSolutionBuilder(FunctionObject, ABC):
    def __init__(self, convertor: Convertor, solution_builder: SolutionBuilder, calculator: AlgorithmCalculator):
        self.convertor = convertor
        self.solutionBuilder = solution_builder
        self.calculator = calculator

    @abstractmethod
    def build(self, *args) -> EncodedSolution:
        pass
