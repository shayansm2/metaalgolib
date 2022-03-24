from abc import ABC, abstractmethod

from src.lib.FunctionObject import FunctionObject
from src.problems.lib.Problem import Problem


class Calculator(FunctionObject, ABC):
    def __init__(self, problem: Problem):
        self.problem = problem

    @abstractmethod
    def get_objective_function(self, decision_variables: any):
        pass

    @abstractmethod
    def check_is_feasible(self, decision_variables: any):
        pass
