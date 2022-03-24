from abc import ABC, abstractmethod

from src.algorithms.lib.HyperParameterStorage import HyperParameterStorage
from src.lib.FunctionObject import FunctionObject
from src.problems.lib.Problem import Problem


class Algorithm(FunctionObject, ABC):
    def __init__(self):
        self.problem = None
        self.hyperParameter = HyperParameterStorage()

    @abstractmethod
    def get_algorithm_name(self) -> str:
        pass

    def set_hyper_parameter(self, name, value):
        self.hyperParameter.set_hyper_parameter(name, value)
        return self

    def set_problem(self, problem: Problem):
        self.problem = problem

    @abstractmethod
    def execute(self):
        self.validate_inputs()
        self.initiate()
        pass  # TODO should be implemented on the child

    def set_stop_criteria(self):
        pass

    def validate_inputs(self):
        assert self.problem is not None, 'problem not defined'

    @abstractmethod
    def initiate(self):
        pass
