import hashlib
from abc import ABC, abstractmethod
from typing import final

from src.Enums import Enums
from src.algorithms.lib.AlgorithmResult import AlgorithmResult
from src.algorithms.lib.HyperParameterStorage import HyperParameterStorage
from src.lib.FunctionObject import FunctionObject
from src.problems.lib.Problem import Problem


class Algorithm(FunctionObject, ABC):
    def __init__(self):
        self.problem = None
        self.hyperParameter = HyperParameterStorage()
        self.result = AlgorithmResult()
        self.keepLog = False
        self.keepUniqueAnswers = False

    @abstractmethod
    def get_algorithm_name(self) -> str:
        pass

    def set_hyper_parameter(self, name, value):
        self.hyperParameter.set_hyper_parameter(name, value)
        return self

    def set_problem(self, problem: Problem):
        self.problem = problem

    @final
    def execute(self):
        self.validate_inputs()
        self.initiate()
        self.run()

    def set_stop_criteria(self, name: str, vale: int):
        assert name in Enums.algoSetting.all_stop_criteria
        return self

    def validate_inputs(self):
        assert self.problem is not None, 'problem not defined'

    @abstractmethod
    def initiate(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def get_result(self) -> AlgorithmResult:
        return self.result

    def keep_log(self):
        self.keepLog = True
        return self

    def keep_unique_answers(self):
        self.keepUniqueAnswers = True
        return self

    @staticmethod
    def get_hash(data: any):
        return hashlib.md5(str(data).encode()).hexdigest()
