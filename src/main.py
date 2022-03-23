from src.AlgorithmFactory import AlgorithmFactory
from src.Enums import Enums
from src.problems.QAPProblem import QAPProblem
from src.solver.Solver import Solver

enum = Enums()
ga = AlgorithmFactory.get(enum.algo.ga)

ga.set_hyper_parameter(enum.hyperParam.numberOfIteration, 100) \
    .set_hyper_parameter(enum.hyperParam.numberOfPopulation, 10) \
    .set_hyper_parameter(enum.hyperParam.crossoverPercentage, 0.6) \
    .set_hyper_parameter(enum.hyperParam.mutationPercentage, 0.1)

qap = QAPProblem()
qap.set_parameter_from_url(url='https://www.opt.math.tugraz.at/qaplib/data.d/bur26b.dat')

solver = Solver(ga, qap)
solver.with_plot()
solver.solve()

print(solver.get_best_found_answer())
solver.show_plot()
