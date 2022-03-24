from abc import ABC, abstractmethod

from src.algorithms.lib.EncodedSolution import EncodedSolution
from src.algorithms.lib.EncodedSolutionBuilder import EncodedSolutionBuilder


class GeneticEncodedSolutionBuilder(EncodedSolutionBuilder, ABC):
    @abstractmethod
    def build_from_crossover(self, parent1: EncodedSolution, parent2: EncodedSolution):
        pass

    @abstractmethod
    def build_from_mutation(self, parent: EncodedSolution):
        pass
