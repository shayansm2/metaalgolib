from abc import ABC, abstractmethod

from src.algorithms.lib.HyperParameterStorage import HyperParameterStorage
from src.lib.FunctionObject import FunctionObject


class Algorithm(FunctionObject, ABC):
    def __init__(self):
        self.hyperParameter = HyperParameterStorage()

    def set_hyper_parameter(self, name, value):
        self.hyperParameter.set_hyper_parameter(name, value)
        return self

    @abstractmethod
    def execute(self):
        pass  # TODO should be implemented on the child

    def set_stop_criteria(self):
        pass
