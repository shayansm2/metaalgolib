from src.lib.DataStructure import DataStructure


class EncodedSolution(DataStructure):
    def __init__(self):
        self.costFunctionValue = None

    def set_cost_function_value(self, value: float):
        self.costFunctionValue = value
        return self

    def get_cost_function_value(self) -> float:
        return self.costFunctionValue
