from src.AlgorithmFactory import AlgorithmFactory
from src.Enums import Enums
from src.lib.Solver import Solver
from src.problems.QAP import QAPProblem

ga = AlgorithmFactory.get(Enums.algo.ga)

ga.set_hyper_parameter(Enums.hyperParam.numberOfIteration, 100) \
    .set_hyper_parameter(Enums.hyperParam.numberOfPopulation, 100) \
    .set_hyper_parameter(Enums.hyperParam.crossoverPercentage, 0.4) \
    .set_hyper_parameter(Enums.hyperParam.mutationPercentage, 0.05)

qap = QAPProblem()
qap.set_parameters(url='https://www.opt.math.tugraz.at/qaplib/data.d/chr12a.dat')

solver = Solver(ga, qap)
solver.with_objective_function_progress() \
    .with_convergence_report()

solver.solve()

print(solver.get_best_found_answer())
solver.show_plots()
