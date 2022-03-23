from src.enums.algorithms import AlgorithmNames
from src.enums.hyper_parameters import HyperParameterNames
from src.enums.problems import ProblemNames


class Enums(object):
    def __init__(self):
        self.algo = AlgorithmNames()
        self.hyperParam = HyperParameterNames()
        self.problem = ProblemNames()
