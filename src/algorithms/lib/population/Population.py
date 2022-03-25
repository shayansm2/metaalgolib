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

    @abstractmethod
    def get_top_individuals(self, count: int) -> list[EncodedSolution]:
        pass

    @abstractmethod
    def get_random_individuals(self, count: int) -> list[EncodedSolution]:
        pass

    def get_random_individual(self) -> EncodedSolution:
        return self.get_random_individuals(1).pop()

    @abstractmethod
    def keep_top_individuals(self, count: int):
        pass
