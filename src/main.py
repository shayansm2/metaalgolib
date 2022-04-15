import math

import numpy as np

from src.AlgorithmFactory import AlgorithmFactory
from src.Enums import Enums
from src.lib.Solver import Solver
from src.problems.MathematicalOptimizationProblem import MathematicalOptimizationProblem

ga = AlgorithmFactory.get(Enums.algo.ga)

ga.set_hyper_parameter(Enums.hyperParam.numberOfIteration, 100) \
    .set_hyper_parameter(Enums.hyperParam.numberOfPopulation, 100) \
    .set_hyper_parameter(Enums.hyperParam.geneticCrossoverPercentage, 0.4) \
    .set_hyper_parameter(Enums.hyperParam.geneticMutationPercentage, 0.1) \
    .set_stop_criteria(Enums.algoSetting.stopCriteriaNumberOfGeneration, 100)


# problem = QAPProblem()
# problem.set_parameters(url='https://www.opt.math.tugraz.at/qaplib/data.d/chr12a.dat')


# https://www.sfu.ca/~ssurjano/crossit.html
def cross_in_tray_function(x: list):
    x1 = x[0]
    x2 = x[1]

    fact1 = math.sin(x1) * math.sin(x2)
    fact2 = math.exp(abs(100 - math.sqrt(x1 ** 2 + x2 ** 2) / math.pi))

    return -0.0001 * (abs(fact1 * fact2) + 1) ** 0.1


# https://www.sfu.ca/~ssurjano/ackley.html
def ackley_function(x: list):
    a = 20
    b = 0.2
    c = 2 * math.pi

    d = len(x)

    x = np.array(x)
    sum1 = np.dot(x, x)
    sum2 = sum(np.cos(c * x))

    term1 = -a * math.exp(-b * math.sqrt(sum1 / d))
    term2 = -math.exp(sum2 / d)

    return term1 + term2 + a + math.e


problem = MathematicalOptimizationProblem()
# problem.set_parameters(2, (-10, 10), cross_in_tray_function)
problem.set_parameters(10, (-32.768, 32.768), ackley_function)

solver = Solver(ga, problem)
solver.with_objective_function_progress() \
    .with_convergence_report()

solver.solve()

print(solver.get_best_found_answer())
solver.show_plots()
