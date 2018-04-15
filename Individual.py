from Chromosome import Chromosome

class Individual:

    def __init__(self, chromosome_length):
        self.chromosome = Chromosome(chromosome_length)
        self.chromosome_length = chromosome_length
        self.fitness = self.chromosome.alleles.count(True)

    def print(self):
        self.chromosome.print()
        print("Fitness:", self.fitness)