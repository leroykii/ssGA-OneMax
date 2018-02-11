import time
from ProblemOneMax import ProblemOneMax
from Algorithm import Algorithm
from Visualization import Visualization
import numpy as np
import cProfile
import matplotlib.pyplot as plt

#############################################
#############################################

def main():

    pr = cProfile.Profile()
    pr.enable()

    gene_number = 128
    gene_length = 1
    population_size = 128
    crossover_probability = 0.8
    target_fitness = gene_number * gene_length
    mutation_probability = 1.0 / target_fitness
    MAX_ITERATION_STEPS = 5000

    NUM_EXECUTIONS = 50

    all_best_fitness_history = np.empty([MAX_ITERATION_STEPS+1, NUM_EXECUTIONS])

    for iter in range(NUM_EXECUTIONS):
        algorithm, problem = test(MAX_ITERATION_STEPS, crossover_probability, gene_length, gene_number,
                                     mutation_probability, population_size, target_fitness)

        # todo, meter a visualización, pasándole población
        all_best_fitness_history[:,iter] = algorithm.population.best_fitness_history


    #print(all_best_fitness_history)
    #print(all_best_fitness_history.mean(0))

    #return
    visualization = Visualization()
    # visualization.fitness_history(algorithm.population, problem.fitness_counter)

    visualization.all_fitness_history(all_best_fitness_history)



    pr.disable()
    #pr.print_stats(sort="calls")


def test(MAX_ITERATION_STEPS, crossover_probability, gene_length, gene_number, mutation_probability,
                population_size, target_fitness):

    # Define problem
    problem = ProblemOneMax(gene_number, gene_length, target_fitness)
    # Configure algorithm
    algorithm = Algorithm(problem, population_size, gene_number, gene_length, crossover_probability,
                          mutation_probability, MAX_ITERATION_STEPS)
    for iter in range(0, MAX_ITERATION_STEPS):

        algorithm.go_one_step()

        # print("[", iter, "] Best: ", algorithm.population.bestf, sep="")

        if ((problem.tf_known) and (
                algorithm.population.population[algorithm.population.bestp].fitness >= problem.target_fitness)):
            print("Solution found after", problem.fitness_counter, "evaluations!")
            break

        #  time.sleep(0.5)
        # algorithm.population.print_stats()
        # input()

        if (iter % 1000 == 0):
            print("Iteration:", iter)

    # Print solution
    solution_individual = algorithm.population.population[algorithm.population.bestp]
    solution_individual.print()

    return algorithm, problem


#############################################
#############################################
if __name__ == '__main__':

    main()

