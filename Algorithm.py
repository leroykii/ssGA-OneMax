from Population import Population
from Individual import Individual
import random
import copy
from bitarray import bitarray

class Algorithm:
    def __init__(self, problem, population_size, gene_number, gene_length, crossover_probability, mutation_probability):
        self.gene_number = gene_number
        self.gene_length = gene_length
        self.chromosome_length = gene_number * gene_length
        self.population_size = population_size
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.problem = problem
        #self.population = Population(population_size, self.chromosome_length)
        #self.aux_individual = Individual(self.chromosome_length)

        #todo last loop

        return

    # todo
    def select_tournament(self):
        return

    def single_point_crossover(self, p1, p2):

        # If no crossover then randomly return one parent
        if (random.uniform(0, 1) > self.crossover_probability):
            return (p1 if (random.uniform(0, 1) > 0.5) else p2)

        # Randomize cross_point
        cross_point = round(random.uniform(0, 1) * (self.chromosome_length - 1 + 0.5))
        if (cross_point > self.chromosome_length - 1):
            cross_point = self.chromosome_value - 1

        print("\nCross point:", cross_point)
        # Apply crossover
        crossed_individual = copy.deepcopy(p1)
        crossed_individual.chromosome.alleles[cross_point::] = p2.chromosome.alleles[cross_point::]

        return crossed_individual

    def mutate(self, individual):

        # Generate mutation bit array randomly
        mutation_bitarray = bitarray(self.chromosome_length)
        for bb in range(0, self.chromosome_length):
            mutation_bitarray[bb] = (random.uniform(0, 1) <= self.mutation_probability)

        # Mutation
        individual.chromosome.alleles ^= mutation_bitarray

        return individual

    # todo
    def replace(self, new_individual):
        return

    #todo
    def go_one_step(self):
        return

    # todo
    def get_solution(self):
        return

    #def get/set ith