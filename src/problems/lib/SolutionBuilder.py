from abc import abstractmethod, ABC

from src.lib.FunctionObject import FunctionObject
from src.algorithms.lib.EncodedSolution import EncodedSolution
from src.problems.lib.Solution import Solution


class SolutionBuilder(FunctionObject, ABC):
    # @abstractmethod
    # def get_problem(self) -> Problem:
    #     pass

    @abstractmethod
    def build_randomly(self) -> Solution:
        pass

    @abstractmethod
    def build_from_decision_variables(self, decision_variables) -> Solution:
        pass

    @abstractmethod
    def build_from_encoded_solution(self, encoded_solution: EncodedSolution) -> Solution:
        pass
