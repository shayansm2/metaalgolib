from abc import ABC, abstractmethod

from src.lib.Calculator import Calculator


class AlgorithmCalculator(Calculator, ABC):
    @abstractmethod
    def get_cost_function(self, *args):
        pass
