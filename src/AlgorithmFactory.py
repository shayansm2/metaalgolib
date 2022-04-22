from src.Enums import Enums
from src.algorithms.Genetic import GeneticAlgorithm
from src.algorithms.ParticleSwarmOptimization import ParticleSwarmOptimizationAlgorithm
from src.algorithms.lib.Algorithm import Algorithm


class AlgorithmFactory(object):
    @staticmethod
    def get(name: str) -> Algorithm:
        if name == Enums.algo.ga:
            return GeneticAlgorithm()
        if name == Enums.algo.pso:
            return ParticleSwarmOptimizationAlgorithm()

        raise Exception('algorithm not found')
