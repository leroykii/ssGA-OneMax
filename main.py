import time
from ProblemOneMax import ProblemOneMax
from Algorithm import Algorithm
from Visualization import Visualization
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


    gene_number = 128
    gene_length = 1
    population_size = 128
    crossover_probability = 0.8
    target_fitness = gene_number * gene_length
    mutation_probability = 1.0 / target_fitness
    MAX_ITERATION_STEPS = 10000

    # Define problem
    problem = ProblemOneMax(gene_number, gene_length, target_fitness)

    # Configure algorithm
    algorithm = Algorithm(problem, population_size, gene_number, gene_length, crossover_probability, mutation_probability, MAX_ITERATION_STEPS)

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

        if (iter % 1000 == 0):
            print("Iteration:", iter)

    # Print solution
    solution_individual = algorithm.population.population[algorithm.population.bestp]
    solution_individual.print()

    pr.disable()
    #pr.print_stats(sort="calls")

    visualization = Visualization()
    visualization.fitness_history(algorithm.population, problem.fitness_counter)

#############################################
#############################################
if __name__ == '__main__':
    main()

