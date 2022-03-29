import matplotlib.pyplot as plt

from src.algorithms.lib.Algorithm import Algorithm
from src.algorithms.lib.EncodedSolution import EncodedSolution
from src.lib.FunctionObject import FunctionObject
from src.problems.lib.Problem import Problem
from src.problems.lib.Solution import Solution


class Solver(FunctionObject):
    def __init__(self, algorithm: Algorithm, problem: Problem):
        self.algorithm = algorithm
        self.problem = problem
        self.withPlot = False

    def with_plot(self):
        self.withPlot = True
        self.algorithm.keep_log()

    def solve(self):
        self.algorithm.set_problem(self.problem)
        self.algorithm.execute()

    def get_best_found_answer(self) -> Solution:
        return self.algorithm.result.get_best_answer().get_decoded_solution()

    def show_plot(self):
        assert self.withPlot, 'cannot display the plot. please set the with_plot before running the solver'

        plt.plot(list(map(self.get_objective_function_values, self.algorithm.get_result().get_answer_logs())))
        plt.ylabel('objective function value')
        plt.xlabel('generation number')
        plt.show()

    @staticmethod
    def get_objective_function_values(solution: EncodedSolution):
        return solution.get_decoded_solution().get_objective_function_value()

