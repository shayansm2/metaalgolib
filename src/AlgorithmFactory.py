from src.algorithms.GeneticAlgorithm import GeneticAlgorithm
from src.algorithms.lib.Algorithm import Algorithm
from src.enums.algorithms import AlgorithmNames


class AlgorithmFactory(object):
    @staticmethod
    def get(name: str) -> Algorithm:
        if name == AlgorithmNames.ga:
            return GeneticAlgorithm()

        raise Exception('algorithm not found')
