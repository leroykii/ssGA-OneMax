import time
from ProblemOneMax import ProblemOneMax
from Individual import Individual
from Population import Population
from Algorithm import Algorithm
import numpy
import cProfile
import matplotlib.pyplot as plt

#############################################
#############################################

def main():
    #plt.plot([1, 2, 3, 4])
    #plt.ylabel('some numbers')
    #plt.show()
    #return

    # t = Timer(1.0, hello)
    # t.start()
    #time.sleep(2)


    gene_number = 200
    gene_length = 1
    population_size = 512
    crossover_probability = 0.8
    target_fitness = gene_number * gene_length
    mutation_probability = 1.0 / target_fitness
    MAX_ITERATION_STEPS = 3000

    # Define problem
    problem = ProblemOneMax(gene_number, gene_length, target_fitness)

    # Configure algorithm
    algorithm = Algorithm(problem, population_size, gene_number, gene_length, crossover_probability, mutation_probability)

    pr = cProfile.Profile()
    pr.enable()

    for iter in range(0, MAX_ITERATION_STEPS):

        algorithm.go_one_step()

       # print("[", iter, "] Best: ", algorithm.population.bestf, sep="")

        if ((problem.tf_known) and (algorithm.population.population[algorithm.population.bestp].fitness >= problem.target_fitness)):
            print("Solution found after", problem.fitness_counter, "evaluations!")
            break

      #  time.sleep(0.5)
       # algorithm.population.print_stats()
        #input()

    # Print solution
    solution_individual = algorithm.population.population[algorithm.population.bestp]
    solution_individual.print()

    pr.disable()
    # after your program ends
    pr.print_stats(sort="calls")

#############################################
#############################################
if __name__ == '__main__':
    main()

