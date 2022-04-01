from typing import Type

import numpy as np
import pandas as pd

from src.Enums import Enums
from src.algorithms.Genetic import GeneticOperators
from src.problems.lib.Convertor import Convertor
from src.problems.lib.ParameterStorage import ParameterStorage
from src.problems.lib.Problem import Problem
from src.problems.lib.ProblemCalculator import ProblemCalculator


class QAPParameters(ParameterStorage):
    def __init__(self):
        self.problem_size = None
        self.facility_flow_matrix = None
        self.transport_cost_matrix = None


class QAPProblem(Problem):
    def get_problem_name(self) -> str:
        return Enums.problem.qap

    def set_parameters(self, url):
        string = super().get_from_url(url)
        problem = string.split('\n\n')

        self.parameters: QAPParameters
        problem_size = int(problem[0])

        self.parameters.problem_size = int(problem[0])

        self.parameters.facility_flow_matrix = \
            np.array([int(i) for i in problem[1].split()]).reshape(problem_size, problem_size)

        self.parameters.transport_cost_matrix = \
            np.array([int(i) for i in problem[2].split()]).reshape(problem_size, problem_size)

        return self

    def get_parameter_storage(self) -> ParameterStorage:
        return QAPParameters()

    def get_problem_calculator(self) -> Type[ProblemCalculator]:
        return QAPCalculator

    def get_problem_convertors_mapping(self) -> dict:
        return {
            Enums.algo.ga: QAPGeneticConvertor()
        }

    def get_problem_operators_mapping(self) -> dict:
        return {
            Enums.algo.ga: QAPGeneticOperators()
        }


class QAPCalculator(ProblemCalculator):
    def get_objective_function(self, decision_variables: list[list]):
        self.parameters: QAPParameters

        flow = self.parameters.facility_flow_matrix
        cost = self.parameters.transport_cost_matrix
        decision_variables = np.array(decision_variables)
        return sum(sum(flow * np.dot(np.dot(decision_variables.transpose(), cost), decision_variables)))

    def check_is_feasible(self, decision_variables: any):
        return True


class QAPGeneticConvertor(Convertor):
    @staticmethod
    def decode(chromosome: list) -> list[list]:
        n = len(chromosome)
        decision_variables = np.zeros((n, n))
        for i in range(n):
            decision_variables[i][chromosome[i]] = 1
        return list(decision_variables)

    @staticmethod
    def encode(decision_variables: list[list]) -> list:
        n = len(decision_variables)
        chromosome = [0] * n
        # todo complete this
        return chromosome


class QAPGeneticOperators(GeneticOperators):
    @staticmethod
    def random_generator(problem: Problem) -> list:  # not a good code, but I had no other idea
        assert isinstance(problem, QAPProblem), 'problem type is wrong'
        problem_size = problem.parameters.problem_size
        chromosome = np.arange(problem_size)
        np.random.shuffle(chromosome)
        return list(chromosome)

    @staticmethod
    def crossover(parent1: list, parent2: list) -> tuple:
        p1 = np.random.rand(len(parent1))
        p1.sort()
        p1 = np.array(p1[parent1])
        p2 = np.random.rand(len(parent2))
        p2.sort()
        p2 = np.array(p2[parent2])
        alpha = np.random.rand()
        c1 = pd.Series(alpha * p1 + (1 - alpha) * p2)
        c2 = pd.Series((1 - alpha) * p1 + alpha * p2)
        child1 = c1.sort_values().reset_index().reset_index().set_index('index').sort_index()['level_0'].tolist()
        child2 = c2.sort_values().reset_index().reset_index().set_index('index').sort_index()['level_0'].tolist()
        return child1, child2

    @staticmethod
    def mutation(parent: list) -> list:
        a = np.arange(len(parent))
        np.random.shuffle(a)
        child = parent.copy()
        child[a[0]], child[a[1]] = parent[a[1]], parent[a[0]]
        return child
