from abc import abstractmethod
from typing import Callable

from src.lib.DataStructure import DataStructure


class Operators(DataStructure):
    @classmethod
    @abstractmethod
    def get_random_generator(cls) -> Callable:
        pass
