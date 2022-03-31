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
        self.withConvergenceAnalysis = False

    def with_plot(self):
        self.withPlot = True
        self.algorithm.keep_log()
        return self

    def with_convergence_report(self):
        self.withConvergenceAnalysis = True
        self.algorithm.keep_unique_answers()
        return self

    def solve(self):
        self.algorithm.set_problem(self.problem)
        self.algorithm.execute()

    def get_best_found_answer(self) -> Solution:
        return self.algorithm.result.get_best_answer().get_decoded_solution()

    def show_plots(self):
        if self.withPlot:
            plt.plot(list(map(self.get_objective_function_values, self.algorithm.get_result().get_answer_logs())))
            plt.ylabel('objective function value')
            plt.xlabel('generation number')
            plt.show()

        if self.withConvergenceAnalysis:
            plt.plot(self.algorithm.get_result().get_unique_answer_count())
            plt.ylabel('# unique answers')
            plt.xlabel('generation number')
            plt.show()

    @staticmethod
    def get_objective_function_values(solution: EncodedSolution):
        return solution.get_decoded_solution().get_objective_function_value()

