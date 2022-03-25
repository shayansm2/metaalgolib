from abc import ABC, abstractmethod

from src.algorithms.lib.EncodedSolution import EncodedSolution
from src.lib.DataStructure import DataStructure


class Population(DataStructure, ABC):
    @abstractmethod
    def insert(self, individual: EncodedSolution):
        pass

    @abstractmethod
    def insert_many(self, individuals: list[EncodedSolution]):
        pass

    @abstractmethod
    def get_best_answer(self) -> EncodedSolution:
        pass
