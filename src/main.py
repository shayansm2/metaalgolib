from src.AlgorithmFactory import AlgorithmFactory
from src.Enums import Enums
from src.problems.QAP import QAPProblem
from src.lib.Solver import Solver

ga = AlgorithmFactory.get(Enums.algo.ga)

ga.set_hyper_parameter(Enums.hyperParam.numberOfIteration, 100) \
    .set_hyper_parameter(Enums.hyperParam.numberOfPopulation, 10) \
    .set_hyper_parameter(Enums.hyperParam.crossoverPercentage, 0.6) \
    .set_hyper_parameter(Enums.hyperParam.mutationPercentage, 0.1)

qap = QAPProblem()
qap.set_parameters(url='https://www.opt.math.tugraz.at/qaplib/data.d/bur26b.dat')

solver = Solver(ga, qap)
solver.with_plot()
solver.solve()

print(solver.get_best_found_answer())
solver.show_plot()
