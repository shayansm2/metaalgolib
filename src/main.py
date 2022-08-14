import numpy as np

from src.AlgorithmFactory import AlgorithmFactory
from src.Enums import Enums
from src.lib.Solver import Solver
from src.problems.MathematicalOptimizationProblem import MathematicalOptimizationProblem


# problem = QAPProblem()
# problem.set_parameters(url='https://www.opt.math.tugraz.at/qaplib/data.d/chr12a.dat')


# https://www.sfu.ca/~ssurjano/crossit.html
def cross_in_tray_function(x: list):
    x1 = x[0]
    x2 = x[1]

    fact1 = np.sin(x1) * np.sin(x2)
    fact2 = np.exp(abs(100 - np.sqrt(x1 ** 2 + x2 ** 2) / np.pi))

    return -0.0001 * (np.abs(fact1 * fact2) + 1) ** 0.1


# https://www.sfu.ca/~ssurjano/ackley.html
def ackley_function(x: list):  # todo fix it for numpy
    a = 20
    b = 0.2
    c = 2 * np.pi

    d = len(x)

    x = np.array(x)
    sum1 = np.dot(x, x)
    sum2 = sum(np.cos(c * x))

    term1 = -a * np.exp(-b * np.sqrt(sum1 / d))
    term2 = -np.exp(sum2 / d)

    return term1 + term2 + a + np.e


# https://machinelearningmastery.com/a-gentle-introduction-to-particle-swarm-optimization/
def custom_function(variables: list):
    x = variables[0]
    y = variables[1]

    return (x - 3.14) ** 2 + (y - 2.72) ** 2 + np.sin(3 * x + 1.41) + np.sin(4 * y - 1.73)


def sphere(x):
    return sum(x**2)


pso = AlgorithmFactory.get(Enums.algo.pso)

pso.set_hyper_parameter(Enums.hyperParam.numberOfIteration, 200) \
    .set(Enums.hyperParam.numberOfPopulation, 50) \
    .set(Enums.hyperParam.psoInertiaWeight, 0.995) \
    .set(Enums.hyperParam.psoSocialCoefficient, 1.5) \
    .set(Enums.hyperParam.psoCognitiveCoefficient, 1.5)

problem = MathematicalOptimizationProblem()
problem.set_parameters(10, (-5, 5), sphere)

solver = Solver(pso, problem)
solver.with_objective_function_progress() \
    .with_convergence_report()

solver.solve()

print(solver.get_best_found_answer())
solver.show_plots()
