from Chromosome import Chromosome

class Individual:

    def __init__(self, chromosome_length):
        self.chromosome = Chromosome(chromosome_length)
        self.chromosome_length = chromosome_length
        self.fitness = 0.0

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



