import numpy as np

from src.problems.lib.ParameterStorage import ParameterStorage
from src.problems.lib.Problem import Problem


class QAPProblem(Problem):
    def __init__(self):
        super().__init__()
        self.parameter = ParameterStorage()

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
