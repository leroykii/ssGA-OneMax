class ProblemOneMax:
    def __init__(self, gene_number, gene_length, target_fitness):
        self.gene_number = gene_number
        self.gene_length = gene_length
        self.chromosome_length = gene_number * gene_length
        self.target_fitness = target_fitness
        self.tf_known = True
        self.fitness_counter = 0

    def evaluateStep(self, individual):
        self.fitness_counter += 1

        individual.fitness = individual.chromosome.alleles.count(True)

        return individual.fitness


