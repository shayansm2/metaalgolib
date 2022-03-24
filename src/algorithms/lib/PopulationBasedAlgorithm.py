from abc import ABC, abstractmethod
from typing import Type

from src.algorithms.lib.Algorithm import Algorithm
from src.algorithms.lib.Operators import Operators


class PopulationBasedAlgorithm(Algorithm, ABC):
    def __init__(self):
        super().__init__()
        self.calculator = None
        self.convertor = None
        self.operators = None

    @abstractmethod
    def get_algorithm_operator_type(self) -> Type[Operators]:
        pass

    def initiate(self):
        self.init_calculator()
        self.init_convertor()
        self.init_operators()

    def init_calculator(self):
        self.calculator = self.problem.get_problem_calculator()

    def init_convertor(self):
        convertors = self.problem.get_problem_convertors_mapping()
        convertors: dict
        assert self.get_algorithm_name() in convertors.keys(), \
            'algorithm cannot solve the problem. please define the convertors for the algorithm'
        self.convertor = convertors[self.get_algorithm_name()]

    def init_operators(self):
        all_operators = self.problem.get_problem_operators_mapping()
        all_operators: dict
        assert self.get_algorithm_name() in all_operators.keys(), \
            'algorithm cannot solve the problem. please define the operators for the algorithm'
        operators = all_operators[self.get_algorithm_name()]
        assert isinstance(operators, self.get_algorithm_operator_type()), \
            'the defined operator is not suited for this algorithm'
        self.operators = operators

    def set_selection_method(self):
        pass
