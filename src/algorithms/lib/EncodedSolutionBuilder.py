from abc import ABC, abstractmethod

from src.algorithms.lib.EncodedSolution import EncodedSolution
from src.lib.FunctionObject import FunctionObject
from src.problems.lib.Problem import Problem
from src.problems.lib.Solution import Solution


class EncodedSolutionBuilder(FunctionObject, ABC):
    def __init__(self, problem: Problem):
        self.problem = problem

    @abstractmethod
    def build(self, *args) -> EncodedSolution:
        pass

    @abstractmethod
    def build_randomly(self) -> EncodedSolution:
        pass

    @abstractmethod
    def build_from_solution(self, solution: Solution) -> EncodedSolution:
        pass

    @abstractmethod
    def build_decoded_solution(self, encoded_solution: EncodedSolution) -> Solution:
        pass
