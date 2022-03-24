from abc import ABC, abstractmethod

from src.lib.FunctionObject import FunctionObject
from src.algorithms.lib.EncodedSolution import EncodedSolution
from src.problems.lib.Problem import Problem
from src.problems.lib.Solution import Solution


class EncodedSolutionBuilder(FunctionObject, ABC):
    def __init__(self, problem: Problem):
        # assert isinstance(problem, self.get_problem_type())
        self.problem = problem

    # @abstractmethod
    # def get_problem_type(self) -> Type[Problem]:
    #     pass

    # @abstractmethod
    # def get_algorithm(self) -> Algorithm:
    #     pass

    @abstractmethod
    def build(self, *args) -> EncodedSolution:
        pass

    @abstractmethod
    def build_randomly(self) -> EncodedSolution:
        pass

    @abstractmethod
    def build_from_solution(self, solution: Solution) -> EncodedSolution:
        pass
