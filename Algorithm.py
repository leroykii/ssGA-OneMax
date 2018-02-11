from Population import Population
from Individual import Individual
import numpy
import copy
from bitarray import bitarray

class Algorithm:
    def __init__(self, problem, population_size, gene_number, gene_length, crossover_probability, mutation_probability, max_evaluations):
        self.gene_number = gene_number
        self.gene_length = gene_length
        self.chromosome_length = gene_number * gene_length
        self.population_size = population_size
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.problem = problem
        self.population = Population(population_size, self.chromosome_length, max_evaluations)

        return

    # Binary tournament
    def select_tournament(self):

        # Get first random index
        random_index_1 = round(numpy.random.random() * (self.population_size - 1 + 0.5))
        if (random_index_1 > self.population_size - 1):
            random_index_1 = self.population_size - 1

        # Get second random index, different from first one
        while True:
            random_index_2 = round(numpy.random.random() * (self.population_size - 1 + 0.5))
            if (random_index_2 > self.population_size - 1):
                random_index_2 = self.population_size - 1

            if (random_index_1 != random_index_2):
                break

        # Return the fittest
        if (self.population.population[random_index_1].fitness > self.population.population[random_index_2].fitness):
            return self.population.population[random_index_1]
        else:
            return self.population.population[random_index_2]

    def single_point_crossover(self, p1, p2):

        # If no crossover then randomly return one parent
        if (numpy.random.random() > self.crossover_probability):
            return (p1 if (numpy.random.random() > 0.5) else p2)

        # Randomize cross_point
        cross_point = round(numpy.random.random() * (self.chromosome_length - 1 + 0.5))
        if (cross_point > self.chromosome_length - 1):
            cross_point = self.chromosome_value - 1
        # print("\nCross point:", cross_point)

        # Apply crossover
        crossed_individual = copy.deepcopy(p1)
        crossed_individual.chromosome.alleles[cross_point::] = p2.chromosome.alleles[cross_point::]

        return crossed_individual

    def mutate(self, individual):

        # Generate mutation bit array randomly
        mutation_bitarray = bitarray(self.chromosome_length)
        for bb in range(0, self.chromosome_length):
            #mutation_bitarray[bb] = (random.uniform(0, 1) <= self.mutation_probability)
            mutation_bitarray[bb] = (numpy.random.random() <= self.mutation_probability)

        # Mutation
        individual.chromosome.alleles ^= mutation_bitarray

        return individual

    def replace(self, new_individual):
        # Replace worst individual with new one
        self.population.replace(self.population.worstp, new_individual)
        return

    def go_one_step(self):
        offspring_individual = self.single_point_crossover(self.select_tournament(), self.select_tournament())
        self.mutate(offspring_individual)
        self.problem.evaluateStep(offspring_individual)
        self.replace(offspring_individual)
        return

    def get_solution(self):
        return self.population[self.population.bestp]
