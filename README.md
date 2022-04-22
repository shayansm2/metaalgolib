# MetaAlgoLib

## A Library For Metaheurisitc Algorithms

**A python library for solving optimization problems using metaheuristic algorithms.**\
This document will illustrate how to use this code and how you can add new problems and algorithms to it.


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
qap.set_parameters(url='https://www.opt.math.tugraz.at/qaplib/data.d/bur26b.dat')

solver = Solver(ga, qap)
solver.with_objective_function_progress() \
    .with_convergence_report()
solver.solve()

print(solver.get_best_found_answer())
solver.show_plots()

```

For defining a new problem,  make a copy of `customProblem.py` in the problem directory and change it.\
For defining a new algorithm,  make a copy of `customAlgorithm.py` in the algorithm directory and change it.

--- 
## Roadmap
### core
- [x] initiate the project
- [x] SEO
- [x] solver plots
- [x] problem based plots
- [ ] operators dictionary
- [ ] algorithm setting
- [ ] algorithm penalty function
- [ ] problem feasibility metrics
- [ ] populations
- [ ] hyper parameter optimizer
### algorithms
- [x] genetic algorithm
- [ ] particle swarm optimization algorithm
- [ ] differential evolution algorithm
- [ ] multi objective algorithm
- [ ] NSGA-II
- [ ] MOPSO
### problems
- [x] quadratic assignment problem
- [x] nlp mathematical optimization problem 
- [ ] bin packing problem
- [ ] location-inventory-routing problem