from Individual import Individual
import sys

class Population:
    def __init__(self, population_size, chromosome_length):

        self.population_size = population_size
        self.chromosome_length = chromosome_length

        # Create population
        self.population = []
        for pp in range(population_size):
            self.population.append(Individual(chromosome_length))

        #for ind in population:
            #ind.print()

        # Initialize statistics
        self.bestp = 0
        self.worstp = 0
        self.bestf = 0
        self.average_fitness = 0
        self.worstf = 9999999999.0
        self.BESTF = 0
        self.population_fitness = 0
        self.best_population_fitness = 0

        self.compute_stats()

        return

    def replace(self, index, new_individual):

        # Check valid index
        if (index >= self.population_size):
            print("Error: index out of bounds")
            sys.exit(0)

        # Insert new individual and delete old one
        old_individual = self.population[index]
        self.population[index] = new_individual
        del old_individual

        # Compute stats every time a new individual is added
        self.compute_stats()

        return

    def compute_stats(self):

        # Initialize
        self.population_fitness = 0
        self.worstf = self.population[0].fitness
        self.worstp = 0
        self.bestf = self.population[0].fitness
        self.bestp = 0
        aux_fit = 0

        for ii in range(self.population_size):
            aux_fit = self.population[ii].fitness

            if (aux_fit <= self.worstf):
                self.worstf = aux_fit
                self.worstp = ii
            if (aux_fit >= self.bestf):
                self.bestf = aux_fit
                self.bestp = ii
            if (aux_fit >= self.BESTF):
                self.BESTF = aux_fit

            self.population_fitness += aux_fit

        if (self.population_fitness > self.best_population_fitness):
            self.best_population_fitness = self.population_fitness

        self.average_fitness = self.population_fitness / self.population_size

        return


    def print(self):
        for ii in range(self.population_size):
            print("[", ii, "] \tfitness: ", self.population[ii].fitness, "  \t", self.population[ii].chromosome.alleles, sep="")

    def print_stats(self):
        print("BESTF:", self.BESTF)
        print("bestp:", self.bestp)
        print("bestf:", self.bestf)
        print("worstp:", self.worstp)
        print("worstf:", self.worstf)
        print("avgf:", self.average_fitness)
