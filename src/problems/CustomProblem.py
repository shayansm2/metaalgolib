from abc import ABC

from src.algorithms.CustomAlgorithm import CustomAlgorithmOperators
from src.problems.lib.Convertor import Convertor
from src.problems.lib.Problem import Problem
from src.problems.lib.ProblemCalculator import ProblemCalculator


class CustomProblem(Problem, ABC):
    def get_problem_name(self) -> str:
        # return problem name
        pass

    def get_problem_calculator(self) -> ProblemCalculator:
        return CustomProblemCalculator(self)

    def get_problem_convertors_mapping(self) -> dict:
        return {
            # algorithm 1: convertor for algorithm 1,
            # algorithm 2: convertor for algorithm 2,
            # ...
        }

    def get_problem_operators_mapping(self) -> dict:
        return {
            # algorithm 1: operators for algorithm 1,
            # algorithm 2: operators for algorithm 2,
            # ...
        }

    def set_parameters(self, *args):
        # by implementing this method, you can give your desired parameters to the problem
        # you can use self.get_from_url, self.get_from_excel and self.get_from_csv for easier implementation
        pass


# problem calculators aim is to calculate the objective function and check the feasibility of a solution
class CustomProblemCalculator(ProblemCalculator, ABC):
    def get_objective_function(self, decision_variables: any):
        # this method should calculate the objective function of given decision variables
        pass

    def check_is_feasible(self, decision_variables: any):
        # this method should check whether a solution is feasible or not given decision variables
        pass


# following two classes should be implemented for each algorithm you want to use for this problem

# convertors should convert the decision variable to algorithm's solution representation and vice versa
class CustomProblemCustomAlgorithmConvertor(Convertor, ABC):
    @staticmethod
    def decode(encoded: any):
        # this method should convert the algorithm's solution representation to decision variable
        pass

    @staticmethod
    def encode(decoded: any):
        # this method should convert the decision variable to an algorithm's solution representation
        pass


# operators should contain the implementation of all the operators an algorithm use for this problem
class CustomProblemCustomAlgorithmOperators(CustomAlgorithmOperators, ABC):
    # should implement all the abstract method in custom algorithm operators
    pass
