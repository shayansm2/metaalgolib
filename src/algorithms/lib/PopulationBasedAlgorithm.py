from abc import ABC, abstractmethod
from typing import Type

from src.algorithms.lib.Algorithm import Algorithm
from src.algorithms.lib.EncodedSolutionBuilder import EncodedSolutionBuilder
from src.algorithms.lib.Operators import Operators
from src.problems.lib.SolutionBuilder import SolutionBuilder


class PopulationBasedAlgorithm(Algorithm, ABC):
    def __init__(self):
        super().__init__()
        self.algorithm_builder = None
        self.solution_builder = None
        self.calculator = None
        self.convertor = None
        self.operators = None

    @abstractmethod
    def get_algorithm_operator_type(self) -> Type[Operators]:
        pass

    @abstractmethod
    def get_algorithm_builder_type(self) -> Type[EncodedSolutionBuilder]:
        pass

    def initiate(self):
        self.init_hyper_parameters()
        self.init_calculator()
        self.init_convertor()
        self.init_operators()
        self.init_builders()

    @abstractmethod
    def init_hyper_parameters(self):
        pass

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

    def init_builders(self):
        self.solution_builder = SolutionBuilder(self.calculator)
        self.algorithm_builder = self.get_algorithm_builder_type()(self.convertor, self.solution_builder)

    def set_selection_method(self):
        pass
