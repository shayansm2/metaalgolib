from src.AlgorithmFactory import AlgorithmFactory
from src.enums.algorithms import AlgorithmNames as Algo
from src.enums.hyper_parameters import HyperParameterNames as HyperParams
from src.problems.QAPProblem import QAPProblem
from src.solver.Solver import Solver

ga = AlgorithmFactory.get(Algo.ga)

ga.set_hyper_parameter(HyperParams.numberOfIteration, 100) \
    .set_hyper_parameter(HyperParams.numberOfPopulation, 10) \
    .set_hyper_parameter(HyperParams.crossoverPercentage, 0.6) \
    .set_hyper_parameter(HyperParams.mutationPercentage, 0.1)

qap = QAPProblem()
qap.set_parameter_from_url(url='https://www.opt.math.tugraz.at/qaplib/data.d/bur26b.dat')

solver = Solver(ga, qap)
solver.with_plot()
solver.solve()

print(solver.get_best_found_answer())
solver.show_plot()
