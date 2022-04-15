from abc import ABC, abstractmethod

from src.lib.Calculator import Calculator
from src.problems.lib.ParameterStorage import ParameterStorage


class ProblemCalculator(Calculator, ABC):
    def __init__(self, parameters: ParameterStorage):
        self.parameters = parameters

    @abstractmethod
    def get_objective_function(self, decision_variables: any):
        pass

    @abstractmethod
    def check_is_feasible(self, decision_variables: any) -> bool:
        pass
