from abc import ABC, abstractmethod

from src.lib.Calculator import Calculator
from src.problems.lib.Problem import Problem


class ProblemCalculator(Calculator, ABC):
    def __init__(self, problem: Problem):
        self.problem = problem

    @abstractmethod
    def get_objective_function(self, decision_variables: any):
        pass

    @abstractmethod
    def check_is_feasible(self, decision_variables: any):
        pass
