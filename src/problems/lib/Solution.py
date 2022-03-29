from typing import final

from src.lib.DataStructure import DataStructure


@final
class Solution(DataStructure):
    def __init__(self):
        self.isFeasible = None
        self.objectiveFunctionValue = None
        self.decisionVariables = None

    def set_objective_function_value(self, value: float):
        self.objectiveFunctionValue = value
        return self

    def get_objective_function_value(self) -> float:
        return self.objectiveFunctionValue

    def set_is_feasible(self, is_feasible: bool):
        self.isFeasible = is_feasible
        return self

    def is_feasible(self) -> bool:
        return self.isFeasible

    def set_decision_variables(self, decision_variables: any):
        self.decisionVariables = decision_variables
        return self

    def get_decision_variables(self) -> any:
        return self.decisionVariables

    def __repr__(self):
        output = ''
        output += ('objective function: ' + str(self.objectiveFunctionValue) + '\n')
        output += ('is feasible: ' + ('YES' if self.is_feasible() else 'NO') + '\n')
        output += '\n'
        output += ('decision variables: ' + str(self.decisionVariables) + '\n')

        return output
