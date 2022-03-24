# MetaAlgoLib

## A Library For Metaheurisitc Algorithms

How it should work. (it's not working right now. in progress)

For running

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

For defining a new problem, create a `customProblemName.py` in the problem directory with the following structure:

```python
from abc import ABC

from src.algorithms.lib.EncodedSolutionBuilder import EncodedSolutionBuilder
from src.problems.lib.Problem import Problem
from src.problems.lib.Solution import Solution
from src.problems.lib.SolutionBuilder import SolutionBuilder


class CustomProblem(Problem, ABC):
    # implement the abstract methods in Problem class
    pass


class CustomSolution(Solution):
    # add and implement your required methods
    pass


class CustomSolutionBuilder(SolutionBuilder, ABC):
    # implement the abstract methods in SolutionBuilder class
    pass


# for each algorithm you want to use, you have to implement the following class
class CustomAlgorithmNameEncodedSolutionBuilder(EncodedSolutionBuilder, ABC):
    # implement the abstract methods in EncodedSolutionBuilder class
    pass
```