from src.Enums import Enums
from src.algorithms.genetic import GeneticAlgorithm
from src.algorithms.lib.Algorithm import Algorithm


class AlgorithmFactory(object):
    @staticmethod
    def get(name: str) -> Algorithm:
        if name == Enums.algo.ga:
            return GeneticAlgorithm()

        raise Exception('algorithm not found')
