import time
from ProblemOneMax import ProblemOneMax
from Individual import Individual




#############################################
#############################################

def main():

    # t = Timer(1.0, hello)
    # t.start()
    #time.sleep(2)



    gene_number = 128
    gene_length = 1
    population_size = 128
    crossover_probability = 0.8
    target_fitness = gene_number * gene_length
    mutation_probability = 1.0 / target_fitness
    MAX_ITERATION_STEPS = 5000




    individual = Individual(population_size)


    problem = ProblemOneMax(gene_number, gene_length, target_fitness)

    fitness = problem.evaluateStep(individual)


    individual.print()

#############################################
#############################################
if __name__ == '__main__':
    main()
