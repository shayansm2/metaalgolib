from abc import ABC

import numpy as np

from src.Enums import Enums
from src.algorithms.lib.AlgorithmCalculator import AlgorithmCalculator
from src.problems.lib.Convertor import Convertor
from src.problems.lib.Problem import Problem
from src.problems.lib.ProblemCalculator import ProblemCalculator


class QAPProblem(Problem, ABC):
    def __init__(self):
        self.transport_cost_matrix = None
        self.facility_flow_matrix = None
        self.problem_size = None

    def get_problem_name(self) -> str:
        return Enums.problem.qap

    def set_parameters(self, url):
        string = super().get_from_url(url)
        problem = string.split('\n\n')

        self.problem_size = int(problem[0])

        self.facility_flow_matrix = \
            np.array([int(i) for i in problem[1].split()]).reshape(self.problem_size, self.problem_size)

        self.transport_cost_matrix = \
            np.array([int(i) for i in problem[2].split()]).reshape(self.problem_size, self.problem_size)

        return self

    def get_problem_calculator(self) -> ProblemCalculator:
        return QAPCalculator(self)

    def get_problem_convertors_mapping(self) -> dict:
        return {
            Enums.algo.ga: QAPGeneticConvertor()
        }


class QAPCalculator(ProblemCalculator, ABC):
    def get_objective_function(self, decision_variables: list[list]):
        self.problem: QAPProblem

        flow = self.problem.facility_flow_matrix
        cost = self.problem.transport_cost_matrix
        decision_variables = np.array(decision_variables)
        return sum(sum(flow * np.dot(np.dot(decision_variables.transpose(), cost), decision_variables)))

    def check_is_feasible(self, decision_variables: any):
        return True


class QAPGeneticConvertor(Convertor, ABC):
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


class QAPGeneticCalculator(AlgorithmCalculator, ABC):
    def get_cost_function(self, objective_function: float):
        return objective_function
