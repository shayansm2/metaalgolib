from abc import abstractmethod

from src.lib.DataStructure import DataStructure
from src.problems.lib.Problem import Problem


class Operators(DataStructure):
    @staticmethod
    @abstractmethod
    def random_generator(problem: Problem) -> any:
        pass
