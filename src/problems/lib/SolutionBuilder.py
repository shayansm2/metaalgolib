from typing import final

from src.lib.FunctionObject import FunctionObject
from src.problems.lib.ProblemCalculator import ProblemCalculator
from src.problems.lib.Solution import Solution


@final
class SolutionBuilder(FunctionObject):
    def __init__(self, calculator: ProblemCalculator):
        self.calculator = calculator

    def build(self, decision_variables: any) -> Solution:
        solution = Solution()
        solution.set_decision_variables(decision_variables)
        solution.set_objective_function_value(self.calculator.get_objective_function(decision_variables))
        solution.set_is_feasible(self.calculator.check_is_feasible(decision_variables))
        return solution
