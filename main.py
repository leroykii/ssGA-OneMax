import time
from ProblemOneMax import ProblemOneMax
from Individual import Individual
from Population import Population
from Algorithm import Algorithm
from bitarray import bitarray

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


    population = Population(population_size, gene_number * gene_length)


    # population.print_stats()

    individual1 = Individual(gene_number * gene_length)
    individual2 = Individual(gene_number * gene_length)

    problem = ProblemOneMax(gene_number, gene_length, target_fitness)

    fitness = problem.evaluateStep(individual1)
    fitness = problem.evaluateStep(individual2)


    individual1.print()
    individual2.print()

    algorithm = Algorithm(problem, population_size, gene_number, gene_length, crossover_probability, mutation_probability)

    cross_individual = algorithm.single_point_crossover(individual1, individual2)
    cross_individual.print()

    mutated_individual = algorithm.mutate(cross_individual)
    mutated_individual.print()



    for iter in range(0, MAX_ITERATION_STEPS):

        algorithm.go_one_step()

        print("[", iter, "] Best: ", 1, sep="")

        # if (problem.tf_known) && (solution_individual.fitness >= problem.target_fitness):
            #print("Solution found after", problem.fitness_counter, "evaluations!")
            #break


    # Print solution
    #solution_individual.print()

#############################################
#############################################
if __name__ == '__main__':
    main()
