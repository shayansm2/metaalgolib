# MetaAlgoLib

## A Library For Metaheurisitc Algorithms

**A python library for solving optimization problems using metaheuristic algorithms.**\
This document will illustrate how to use it and how you can add new problems and algorithms to it.\
*Have in mind that the first version of this project is not completed yet and is in progress.*

For solving a pre-defined problem with a pre-writen algorithm, write the below script and change configs based on your requirements:

```python
from src.AlgorithmFactory import AlgorithmFactory
from src.lib.Solver import Solver
from src.problems.QAP import QAPProblem

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