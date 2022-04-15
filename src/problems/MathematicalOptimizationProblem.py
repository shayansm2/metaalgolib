import random
from typing import Callable, Type

import numpy as np

from src.Enums import Enums
from src.algorithms.Genetic import GeneticOperators
from src.problems.lib.DefaultConvertor import DefaultConvertor
from src.problems.lib.ParameterStorage import ParameterStorage
from src.problems.lib.Problem import Problem
from src.problems.lib.ProblemCalculator import ProblemCalculator


class MathematicalOptimizationParameters(ParameterStorage):
    def __init__(self):
        self.dimension = None
        self.objective_function = None
        self.domain = None


class MathematicalOptimizationProblem(Problem):
    def get_problem_name(self) -> str:
        return Enums.problem.math

    def get_parameter_storage(self) -> ParameterStorage:
        return MathematicalOptimizationParameters()

    def get_problem_calculator(self) -> Type[ProblemCalculator]:
        return MathematicalOptimizationCalculator

    def get_problem_convertors_mapping(self) -> dict:
        return {
            Enums.algo.ga: DefaultConvertor()
        }

    def get_problem_operators_mapping(self) -> dict:
        return {
            Enums.algo.ga: MathematicalOptimizationGeneticOperators()
        }

    def set_parameters(self, dimension: int, domain: tuple, objective_function: Callable):
        self.parameters: MathematicalOptimizationParameters
        self.parameters.dimension = dimension
        self.parameters.domain = domain
        self.parameters.objective_function = objective_function
        return self


class MathematicalOptimizationCalculator(ProblemCalculator):
    def get_objective_function(self, decision_variables: list):
        self.parameters: MathematicalOptimizationParameters
        return self.parameters.objective_function(decision_variables)

    def check_is_feasible(self, decision_variables: list) -> bool:
        self.parameters: MathematicalOptimizationParameters
        for decision_variable in decision_variables:
            if decision_variable < self.parameters.domain[0] or decision_variable > self.parameters.domain[1]:
                return False
        return True


class MathematicalOptimizationGeneticOperators(GeneticOperators):
    @staticmethod
    def random_generator(problem: Problem) -> list:
        assert isinstance(problem, MathematicalOptimizationProblem), 'problem type is wrong'
        return list(np.random.uniform(
            problem.parameters.domain[0],
            problem.parameters.domain[1],
            problem.parameters.dimension)
        )

    @staticmethod
    def crossover(parent1: list, parent2: list) -> tuple:
        assert len(parent1) == len(parent2)
        alpha = random.uniform(0, 1)
        parent1, parent2 = np.array(parent1), np.array(parent2)
        child1 = alpha * parent1 + (1 - alpha) * parent2
        child2 = (1 - alpha) * parent1 + alpha * parent2
        return list(child1), list(child2)

    @staticmethod
    def mutation(parent: list) -> list:
        randomIndex = random.randint(0, len(parent) - 1)
        parent[randomIndex] = - parent[randomIndex]
        return parent
