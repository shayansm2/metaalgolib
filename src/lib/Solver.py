from src.algorithms.lib.Algorithm import Algorithm
from src.lib.FunctionObject import FunctionObject
from src.problems.lib.Problem import Problem


class Solver(FunctionObject):
    def __init__(self, algorithm: Algorithm, problem: Problem):
        self.algorithm = algorithm
        self.problem = problem
        self.withPlot = False

    def with_plot(self):
        self.withPlot = True

    def solve(self):
        pass

    def get_best_found_answer(self):
        pass

    def show_plot(self):
        assert self.withPlot, 'cannot display the plot. please set the with_plot before running the solver'
        pass
