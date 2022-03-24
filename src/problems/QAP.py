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
    def set_decision_variables(self, decision_variables: list[list]):
        return super().set_decision_variables(decision_variables)

    def get_decision_variables(self) -> list[list]:
        return super().get_decision_variables()


class QAPSolutionBuilder(SolutionBuilder, ABC):
    def __init__(self, problem: QAPProblem):
        super().__init__(problem)

    def calculate_objective_function(self, assignments: list[list]) -> float:
        assignments = np.array(assignments)
        flow = self.problem.parameter.facility_flow_matrix  # todo fix this shit
        cost = self.problem.parameter.transport_cost_matrix  # todo fix this shit
        return sum(sum(flow * np.dot(np.dot(assignments.transpose(), cost), assignments)))

    def check_is_feasible(self, decision_variables: list[list]) -> bool:
        return True

    def build_from_decision_variables(self, decision_variables: list[list]) -> Solution:
        objective_function = self.calculate_objective_function(decision_variables)
        is_feasible = self.check_is_feasible(decision_variables)
        return self.build(decision_variables, objective_function, is_feasible)

    def build(self, decision_variables: list[list], objective_function: float, is_feasible: bool) -> Solution:
        solution = Solution()
        solution.set_decision_variables(decision_variables) \
            .set_objective_function_value(objective_function) \
            .set_is_feasible(is_feasible)
        return solution


class QAPGeneticEncodedSolutionBuilder(GeneticEncodedSolutionBuilder, ABC):
    def __init__(self, problem: QAPProblem):
        super().__init__(problem)
        self.solutionBuilder = QAPSolutionBuilder(problem)

    def build_randomly(self) -> EncodedSolution:
        self.problem: QAPProblem
        chromosome = np.arange(self.problem.parameter.problem_size)  # todo fix this shit
        np.random.shuffle(chromosome)
        chromosome = list(chromosome)
        return self.build(chromosome)

    def build(self, chromosome) -> EncodedSolution:
        encoded_solution = GeneticEncodedSolution()
        cost_function_value = 1
        encoded_solution.set_chromosome(chromosome).set_cost_function_value(cost_function_value)
        return encoded_solution

    def build_from_solution(self, solution: Solution) -> EncodedSolution:
        pass

    def build_from_crossover(self, parent1: EncodedSolution, parent2: EncodedSolution):
        pass

    def build_from_mutation(self, parent: EncodedSolution):
        pass

    def build_decoded_solution(self, encoded_solution: EncodedSolution) -> Solution:
        encoded_solution: GeneticEncodedSolution
        chromosome = encoded_solution.get_chromosome()

        n = len(chromosome)
        matrix = np.zeros((n, n))
        for i in range(n):
            matrix[i][chromosome[i]] = 1

        return self.solutionBuilder.build_from_decision_variables(list(matrix))
