from Chromosome import Chromosome

class Individual:

    def __init__(self, allele_length):
        self.chromosome = Chromosome(allele_length)
        self.fitness = 0.0
        self.allele_length = allele_length

    def print(self):
        self.chromosome.print()
        print("Fitness:", self.fitness)

    # todo
    def copy(self, source, destination):
        return

    # todo
    def assign(self, individual):
        return

    # todo
    def set_chromosome(self, chromosome):
        return



