from abc import ABC

import numpy as np

from src.algorithms.genetic.GeneticEncodedSolution import GeneticEncodedSolution
from src.algorithms.genetic.GeneticEncodedSolutionBuilder import GeneticEncodedSolutionBuilder
from src.algorithms.lib.EncodedSolution import EncodedSolution
from src.enums.problems import ProblemNames
from src.problems.lib.Problem import Problem
from src.problems.lib.Solution import Solution
from src.problems.lib.SolutionBuilder import SolutionBuilder


class QAPProblem(Problem, ABC):
    def get_problem_name(self) -> str:
        return ProblemNames.qap

    def set_parameter_from_url(self, url):
        string = super().get_from_url(url)
        problem = string.split('\n\n')

        self.parameter.problem_size = int(problem[0])

        self.parameter.facility_flow_matrix = \
            np.array([int(i) for i in problem[1].split()]) \
            .reshape(self.parameter.problem_size, self.parameter.problem_size)

        self.parameter.transport_cost_matrix = \
            np.array([int(i) for i in problem[2].split()]) \
            .reshape(self.parameter.problem_size, self.parameter.problem_size)

        return self


class QAPSolution(Solution):
    pass


class QAPSolutionBuilder(SolutionBuilder, ABC):
    # def get_problem(self) -> Problem:
    #     return QAPProblem()

    def build_randomly(self) -> Solution:
        pass


class QAPGeneticEncodedSolutionBuilder(GeneticEncodedSolutionBuilder, ABC):
    def __init__(self, problem: QAPProblem):
        super().__init__(problem)

    def build_randomly(self) -> EncodedSolution:
        chromosome = np.arange(self.problem.parameter.problem_size)  # todo fix this shit
        np.random.shuffle(chromosome)
        chromosome = list(chromosome)
        return self.build(chromosome)

    def build(self, chromosome) -> EncodedSolution:
        encoded_solution = GeneticEncodedSolution()
        encoded_solution.set_chromosome(chromosome)
        return encoded_solution

    def build_from_solution(self, solution: Solution) -> EncodedSolution:
        pass

    def build_from_crossover(self, parent1: EncodedSolution, parent2: EncodedSolution):
        pass

    def build_from_mutation(self, parent: EncodedSolution):
        pass
