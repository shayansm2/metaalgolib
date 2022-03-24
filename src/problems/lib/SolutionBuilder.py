from abc import abstractmethod, ABC

from src.lib.FunctionObject import FunctionObject
from src.problems.lib.Problem import Problem
from src.problems.lib.Solution import Solution


class SolutionBuilder(FunctionObject, ABC):
    def __init__(self, problem: Problem):
        self.problem = problem

    @abstractmethod
    def build(self, *args) -> Solution:
        pass

    @abstractmethod
    def build_randomly(self) -> Solution:
        pass

    @abstractmethod
    def build_from_decision_variables(self, decision_variables: any) -> Solution:
        pass

    @abstractmethod
    def calculate_objective_function(self, decision_variables: any) -> float:
        pass

    @abstractmethod
    def check_is_feasible(self, decision_variables: any) -> bool:
        pass
