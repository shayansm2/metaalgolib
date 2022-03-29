from src.lib.DataStructure import DataStructure
from src.problems.lib.Solution import Solution


class EncodedSolution(DataStructure):
    def __init__(self):
        self.decodedSolution = None
        self.costFunctionValue = None

    def set_cost_function_value(self, value: float):
        self.costFunctionValue = value
        return self

    def get_cost_function_value(self) -> float:
        return self.costFunctionValue

    def set_decoded_solution(self, decoded_solution: Solution):
        self.decodedSolution = decoded_solution
        return self

    def get_decoded_solution(self) -> Solution:
        return self.decodedSolution
