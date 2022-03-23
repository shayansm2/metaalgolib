from abc import ABC

import numpy as np

from src.enums.problems import ProblemNames
from src.problems.lib.Problem import Problem


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
