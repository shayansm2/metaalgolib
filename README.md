# MetaAlgoLib

## A Library For Metaheurisitc Algorithms

How it should work. (it's not working right now. in progress)


```python
from src.AlgorithmFactory import AlgorithmFactory
from src.problems.QAPProblem import QAPProblem
from src.solver.Solver import Solver

ga = AlgorithmFactory.get('genetic')

ga.set_hyper_parameter('number_of_iteration', 100)
ga.set_hyper_parameter('number_of_population', 10)
ga.set_hyper_parameter('crossover_percentage', 0.6)
ga.set_hyper_parameter('mutation_percentage', 0.1)

qap = QAPProblem()
qap.set_parameter_from_url(url='https://www.opt.math.tugraz.at/qaplib/data.d/bur26b.dat')

solver = Solver(ga, qap)
solver.with_plot()
solver.solve()

print(solver.get_best_found_answer())
solver.show_plot()

```