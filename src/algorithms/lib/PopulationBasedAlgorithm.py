from abc import ABC, abstractmethod
from typing import Type

from src.algorithms.lib.Algorithm import Algorithm
from src.algorithms.lib.EncodedSolution import EncodedSolution
from src.algorithms.lib.EncodedSolutionBuilder import EncodedSolutionBuilder
from src.algorithms.lib.Operators import Operators
from src.algorithms.lib.population.BasePopulation import BasePopulation
from src.problems.lib.SolutionBuilder import SolutionBuilder


class PopulationBasedAlgorithm(Algorithm, ABC):
    def __init__(self):
        super().__init__()
        self.algorithm_builder = None
        self.calculator = None
        self.convertor = None
        self.operators = None
        self.population = None
        self.solution_builder = None
        self.generationNumber = 0

    @abstractmethod
    def get_algorithm_operator(self) -> Type[Operators]:
        pass

    @abstractmethod
    def get_algorithm_encoded_solution(self) -> Type[EncodedSolution]:
        pass

    def initiate(self):
        self.init_hyper_parameters()
        self.init_calculator()
        self.init_convertor()
        self.init_operators()
        self.init_builders()
        self.init_population()

    @abstractmethod
    def init_hyper_parameters(self):
        pass

    def init_calculator(self):
        self.calculator = self.problem.get_calculator()

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
        assert isinstance(operators, self.get_algorithm_operator()), \
            'the defined operator is not suited for this algorithm'
        self.operators = operators

    def init_builders(self):
        self.solution_builder = SolutionBuilder(self.calculator)
        self.algorithm_builder = EncodedSolutionBuilder(
            self.convertor,
            self.solution_builder,
            self.get_algorithm_encoded_solution()
        )

    def init_population(self):
        self.population = BasePopulation()

    def set_selection_method(self):
        pass

    @abstractmethod
    def run_per_generation(self, *args):
        pass

    def _run_per_generation(self, *args):
        self.run_per_generation(*args)

        if self.keepLog:
            self.result.insert_answer_log(self.population.get_best_answer())
        if self.keepUniqueAnswers:
            self.result.insert_unique_answer_count(self.calculate_number_of_unique_answers())

        self.generationNumber += 1

    def calculate_number_of_unique_answers(self) -> int:
        unique_answers = {}
        for encodedSolution in self.population.get_all():
            hash_value = self.get_hash(encodedSolution.get_encoded_representation())

            if unique_answers.get(hash_value):
                unique_answers[hash_value] += 1
            else:
                unique_answers[hash_value] = 1

        return len(unique_answers)

    def reached_stop_criteria(self, n_generation: int) -> bool:
        return self.generationNumber > n_generation
