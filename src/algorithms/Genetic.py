from abc import ABC, abstractmethod
from typing import final, Callable, Type

from src.Enums import Enums
from src.algorithms.lib.EncodedSolution import EncodedSolution
from src.algorithms.lib.EncodedSolutionBuilder import EncodedSolutionBuilder
from src.algorithms.lib.Operators import Operators
from src.algorithms.lib.PopulationBasedAlgorithm import PopulationBasedAlgorithm


@final
class GeneticEncodedSolution(EncodedSolution):
    def __init__(self):
        super().__init__()
        self.chromosome = None

    def set_chromosome(self, chromosome: list):
        self.chromosome = chromosome
        return self

    def get_chromosome(self):
        return self.chromosome


@final
class GeneticEncodedSolutionBuilder(EncodedSolutionBuilder, ABC):
    def build(self, chromosome: any) -> GeneticEncodedSolution:
        encoded_solution = GeneticEncodedSolution()
        encoded_solution.set_chromosome(chromosome)
        decoded_solution = self.solutionBuilder.build(self.convertor.decode(chromosome))
        encoded_solution.set_cost_function_value(self.get_cost_function_value(decoded_solution))
        encoded_solution.set_decoded_solution(decoded_solution)
        return encoded_solution

    def get_cost_function_value(self, decoded_solution):
        return self.calculator.get_cost_function(decoded_solution.get_objective_function_value())


class GeneticOperators(Operators, ABC):
    @classmethod
    @abstractmethod
    def get_crossover_operator(cls) -> Callable:
        pass

    @classmethod
    @abstractmethod
    def get_mutation_operator(cls) -> Callable:
        pass


class GeneticAlgorithm(PopulationBasedAlgorithm, ABC):
    def get_algorithm_name(self) -> str:
        return Enums.algo.ga

    def get_algorithm_operator_type(self) -> Type[Operators]:
        return GeneticOperators

    def get_algorithm_builder_type(self) -> Type[EncodedSolutionBuilder]:
        return GeneticEncodedSolutionBuilder

    def init_hyper_parameters(self):
        n_pop = self.hyperParameter.get_hyper_parameter(Enums.hyperParam.numberOfPopulation)
        p_crossover = self.hyperParameter.get_hyper_parameter(Enums.hyperParam.crossoverPercentage)
        p_mutation = self.hyperParameter.get_hyper_parameter(Enums.hyperParam.mutationPercentage)
        self.set_hyper_parameter(Enums.hyperParam.numberOfCrossover, 2 * int(n_pop * p_crossover / 2))
        self.set_hyper_parameter(Enums.hyperParam.numberOfMutation, int(n_pop * p_mutation))

    def execute(self):
        pass  # todo

    def create_random_solutions(self, count) -> list:
        self.operators: GeneticOperators

        chromosomes = []
        for _ in range(count):
            chromosomes.append(self.operators.get_random_generator()(self.problem))

        self.algorithm_builder: GeneticEncodedSolutionBuilder
        return list(map(self.algorithm_builder.build, chromosomes))

    def perform_crossover(self, parent1: GeneticEncodedSolution, parent2: GeneticEncodedSolution) -> tuple:
        self.operators: GeneticOperators
        child1, child2 = self.operators.get_crossover_operator()(parent1.get_chromosome(), parent2.get_chromosome())
        self.algorithm_builder: GeneticEncodedSolutionBuilder
        return self.algorithm_builder.build(child1), self.algorithm_builder.build(child2)

    def perform_mutation(self, parent: GeneticEncodedSolution) -> GeneticEncodedSolution:
        self.operators: GeneticOperators
        child = self.operators.get_mutation_operator()(parent.get_chromosome())
        self.algorithm_builder: GeneticEncodedSolutionBuilder
        return self.algorithm_builder.build(child)
