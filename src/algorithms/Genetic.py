from abc import abstractmethod
from typing import final, Type

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
class GeneticEncodedSolutionBuilder(EncodedSolutionBuilder):
    def build(self, chromosome: any) -> GeneticEncodedSolution:
        encoded_solution = GeneticEncodedSolution()
        encoded_solution.set_chromosome(chromosome)
        decoded_solution = self.solutionBuilder.build(self.convertor.decode(chromosome))
        encoded_solution.set_cost_function_value(self.get_cost_function_value(decoded_solution))
        encoded_solution.set_decoded_solution(decoded_solution)
        return encoded_solution

    def get_cost_function_value(self, decoded_solution):
        return self.calculator.get_cost_function(decoded_solution.get_objective_function_value())


class GeneticOperators(Operators):
    @staticmethod
    @abstractmethod
    def crossover(parent1: any, parent2: any) -> tuple:
        pass

    @staticmethod
    @abstractmethod
    def mutation(parent: any) -> any:
        pass


class GeneticAlgorithm(PopulationBasedAlgorithm):
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
        n_pop = self.hyperParameter.get_hyper_parameter(Enums.hyperParam.numberOfPopulation)
        n_crossover = self.hyperParameter.get_hyper_parameter(Enums.hyperParam.numberOfCrossover)
        n_mutation = self.hyperParameter.get_hyper_parameter(Enums.hyperParam.numberOfMutation)
        n_generation = self.hyperParameter.get_hyper_parameter(Enums.hyperParam.numberOfIteration)

        self.population.insert_many(self.create_random_solutions(n_pop))

        for _ in n_generation:
            parents = self.population.get_top_individuals(n_crossover * 2)
            crossover_children = []

            for i in range(n_crossover):
                crossover_children += self.perform_crossover(parents[2 * i], parents[2 * i + 1])

            self.population.insert_many(crossover_children)

            parents = self.population.get_random_individuals(n_mutation)
            mutation_children = []

            for parent in parents:
                mutation_children.append(self.perform_mutation(parent))

            self.population.insert_many(crossover_children)
            self.population.insert_many(mutation_children)

            self.population.keep_top_individuals(n_pop)

        pass

    def create_random_solutions(self, count) -> list:
        self.operators: GeneticOperators

        chromosomes = []
        for _ in range(count):
            chromosomes.append(self.operators.random_generator(self.problem))

        self.algorithm_builder: GeneticEncodedSolutionBuilder
        return list(map(self.algorithm_builder.build, chromosomes))

    def perform_crossover(self, parent1: GeneticEncodedSolution, parent2: GeneticEncodedSolution) -> tuple:
        self.operators: GeneticOperators
        child1, child2 = self.operators.crossover(parent1.get_chromosome(), parent2.get_chromosome())
        self.algorithm_builder: GeneticEncodedSolutionBuilder
        return self.algorithm_builder.build(child1), self.algorithm_builder.build(child2)

    def perform_mutation(self, parent: GeneticEncodedSolution) -> GeneticEncodedSolution:
        self.operators: GeneticOperators
        child = self.operators.mutation(parent.get_chromosome())
        self.algorithm_builder: GeneticEncodedSolutionBuilder
        return self.algorithm_builder.build(child)
