import random
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

    def get_encoded_representation(self):
        return self.get_chromosome()

    def set_encoded_representation(self, encoded_representation: any):
        return self.set_chromosome(encoded_representation)


# todo crossover and mutation don't know about problem and parameters, they may need them
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

    def get_algorithm_operator(self) -> Type[Operators]:
        return GeneticOperators

    def get_algorithm_encoded_solution(self) -> Type[EncodedSolution]:
        return GeneticEncodedSolution

    def init_hyper_parameters(self):
        n_pop = self.hyperParameter.get_hyper_parameter(Enums.hyperParam.numberOfPopulation)
        p_crossover = self.hyperParameter.get_hyper_parameter(Enums.hyperParam.geneticCrossoverPercentage)
        p_mutation = self.hyperParameter.get_hyper_parameter(Enums.hyperParam.geneticMutationPercentage)
        self.set_hyper_parameter(Enums.hyperParam.geneticNumberOfCrossover, 2 * int(n_pop * p_crossover / 2))
        self.set_hyper_parameter(Enums.hyperParam.geneticNumberOfMutation, int(n_pop * p_mutation))

    def run(self):
        n_pop = self.hyperParameter.get_hyper_parameter(Enums.hyperParam.numberOfPopulation)
        n_crossover = self.hyperParameter.get_hyper_parameter(Enums.hyperParam.geneticNumberOfCrossover)
        n_mutation = self.hyperParameter.get_hyper_parameter(Enums.hyperParam.geneticNumberOfMutation)
        n_generation = self.hyperParameter.get_hyper_parameter(Enums.hyperParam.numberOfIteration)

        self.population.insert_many(self.create_random_solutions(n_pop))  # todo initial selection

        while not self.reached_stop_criteria(n_generation):  # todo stop condition
            self._run_per_generation(n_crossover, n_mutation, n_pop)

        self.result.set_best_answer(self.population.get_best_answer())

    def run_per_generation(self, n_crossover, n_mutation, n_pop):
        parents = self.population.get_top_individuals(n_crossover * 2)  # todo parent selection
        random.shuffle(parents)
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
        self.population.keep_top_individuals(n_pop)  # todo generation selection

    def create_random_solutions(self, count) -> list:
        self.operators: GeneticOperators

        chromosomes = []
        for _ in range(count):
            chromosomes.append(self.operators.random_generator(self.problem))

        self.algorithm_builder: EncodedSolutionBuilder
        return list(map(self.algorithm_builder.build, chromosomes))

    def perform_crossover(self, parent1: GeneticEncodedSolution, parent2: GeneticEncodedSolution) -> tuple:
        self.operators: GeneticOperators
        child1, child2 = self.operators.crossover(parent1.get_chromosome(), parent2.get_chromosome())
        self.algorithm_builder: EncodedSolutionBuilder
        return self.algorithm_builder.build(child1), self.algorithm_builder.build(child2)

    def perform_mutation(self, parent: GeneticEncodedSolution) -> EncodedSolution:
        self.operators: GeneticOperators
        child = self.operators.mutation(parent.get_chromosome())
        self.algorithm_builder: EncodedSolutionBuilder
        return self.algorithm_builder.build(child)
