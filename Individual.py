from Chromosome import Chromosome

class Individual:

    def __init__(self, allele_length):
        self.chromosome = Chromosome(allele_length)
        self.chromosome.print()
        self.fitness = 0.0
        self.allele_length = allele_length