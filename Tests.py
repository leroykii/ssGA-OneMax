from ProblemOneMax import ProblemOneMax
from Algorithm import Algorithm
from Visualization import Visualization
import numpy as np
import matplotlib.pyplot as plt


class Tests:
    def __init__(self):
        return

    def test_max_min_avg(self, show_plot):
        gene_number = 32
        gene_length = 1
        population_size = 128
        crossover_probability = 0.8
        target_fitness = gene_number * gene_length
        mutation_probability = 1.0 / target_fitness
        MAX_ITERATION_STEPS = 4000
        NUM_EXECUTIONS = 5

        all_best_fitness_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])
        all_worst_fitness_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])
        all_average_fitness_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])
        all_evaluations_history = np.zeros(NUM_EXECUTIONS)

        for iter in range(NUM_EXECUTIONS):
            algorithm, problem = test(MAX_ITERATION_STEPS, crossover_probability, gene_length, gene_number,
                                      mutation_probability, population_size, target_fitness)

            all_best_fitness_history[:, iter] = algorithm.population.best_fitness_history
            all_worst_fitness_history[:, iter] = algorithm.population.worst_fitness_history
            all_average_fitness_history[:, iter] = algorithm.population.average_fitness_history
            all_evaluations_history[iter] = problem.fitness_counter

        np.savetxt('output/all_best_fitness_history', all_best_fitness_history)
        np.savetxt('output/all_worst_fitness_history', all_worst_fitness_history)
        np.savetxt('output/all_average_fitness_history', all_average_fitness_history)
        np.savetxt('output/all_evaluations_history', all_evaluations_history)

        if (show_plot):
            visualization = Visualization()
            visualization.all_fitness_history(all_best_fitness_history, all_worst_fitness_history,
                                          all_average_fitness_history, all_evaluations_history)

    def test_mutation(self, show_plot):

        gene_number = 128
        gene_length = 1
        population_size = 128
        target_fitness = gene_number * gene_length
        MAX_ITERATION_STEPS = 10000
        NUM_EXECUTIONS = 10
        num_mutation_values = 10
        crossover_probability = 0.8

        all_best_fitness_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])
        all_worst_fitness_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])
        all_average_fitness_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])
        all_evaluations_history = np.zeros(NUM_EXECUTIONS)

        mutation_probability = np.linspace(0, 2/target_fitness, num_mutation_values)
        mutation_probability = np.around(mutation_probability, 5)

        mean_mutation_best_history = np.zeros([MAX_ITERATION_STEPS + 1, mutation_probability.size])

        for mutation_iter in range(mutation_probability.size):

            print("Computing mutation probability:", mutation_probability[mutation_iter])

            for iter in range(NUM_EXECUTIONS):
                algorithm, problem = test(MAX_ITERATION_STEPS, crossover_probability, gene_length, gene_number,
                                          mutation_probability[mutation_iter], population_size, target_fitness)

                all_best_fitness_history[:, iter] = algorithm.population.best_fitness_history
                all_worst_fitness_history[:, iter] = algorithm.population.worst_fitness_history
                all_average_fitness_history[:, iter] = algorithm.population.average_fitness_history
                all_evaluations_history[iter] = problem.fitness_counter

            mean_mutation_best_history[:, mutation_iter] = all_best_fitness_history.mean(1)

        np.savetxt('output/mean_mutation_best_history', mean_mutation_best_history)
        np.savetxt('output/mutation_probability', mutation_probability)
        np.save('output/target_fitness', target_fitness)


        if (show_plot):
            # Visualization
            visualization = Visualization()
            visualization.mutation(mean_mutation_best_history, mutation_probability, target_fitness)

        return

    def test_crossover(self, show_plot):
        gene_number = 32
        gene_length = 1
        population_size = 128
        target_fitness = gene_number * gene_length
        MAX_ITERATION_STEPS = 2000
        NUM_EXECUTIONS = 1
        mutation_probability = 1.0 / target_fitness
        num_crossover_values = 5

        all_best_fitness_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])
        all_worst_fitness_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])
        all_average_fitness_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])
        all_evaluations_history = np.zeros(NUM_EXECUTIONS)

        crossover_probability = np.linspace(0, 1, num_crossover_values)
        crossover_probability = np.around(crossover_probability, 2)

        mean_crossover_best_history = np.zeros([MAX_ITERATION_STEPS + 1, crossover_probability.size])

        for cross_iter in range (crossover_probability.size):

            print("Computing crossover probability:", crossover_probability[cross_iter])

            for iter in range(NUM_EXECUTIONS):
                algorithm, problem = test(MAX_ITERATION_STEPS, crossover_probability[cross_iter], gene_length, gene_number,
                                          mutation_probability, population_size, target_fitness)

                all_best_fitness_history[:, iter] = algorithm.population.best_fitness_history
                all_worst_fitness_history[:, iter] = algorithm.population.worst_fitness_history
                all_average_fitness_history[:, iter] = algorithm.population.average_fitness_history
                all_evaluations_history[iter] = problem.fitness_counter

            mean_crossover_best_history[:, cross_iter] = all_best_fitness_history.mean(1)

        np.savetxt('output/mean_crossover_best_history', mean_crossover_best_history)
        np.savetxt('output/crossover_probability', crossover_probability)
        np.save('output/target_fitness', target_fitness)

        if (show_plot):
            # Visualization
            visualization = Visualization()
            visualization.crossover(mean_crossover_best_history, crossover_probability, target_fitness)

        return

    def load_data_from_files(self, load_array):

        if (load_array[0]):
            all_best_fitness_history = np.loadtxt('output/all_best_fitness_history')
            all_worst_fitness_history = np.loadtxt('output/all_worst_fitness_history')
            all_average_fitness_history = np.loadtxt('output/all_average_fitness_history')
            all_evaluations_history = np.loadtxt('output/all_evaluations_history')

            visualization = Visualization()

            visualization.all_fitness_history(all_best_fitness_history, all_worst_fitness_history,
                                              all_average_fitness_history, all_evaluations_history)



        if (load_array[1]):
            mean_crossover_best_history = np.loadtxt('output/mean_crossover_best_history')
            crossover_probability = np.loadtxt('output/crossover_probability')
            target_fitness = np.load('output/target_fitness.npy')

            # Visualization
            visualization = Visualization()
            visualization.crossover(mean_crossover_best_history, crossover_probability, target_fitness)


        if (load_array[2]):
            mean_mutation_best_history = np.loadtxt('output/mean_mutation_best_history')
            mutation_probability = np.loadtxt('output/mutation_probability')
            target_fitness = np.load('output/target_fitness.npy')

            # Visualization
            visualization = Visualization()
            visualization.crossover(mean_mutation_best_history, mutation_probability, target_fitness)


        #if (load_array[3]):


        return

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

        if ((problem.tf_known) and (algorithm.population.population[algorithm.population.bestp].fitness >= problem.target_fitness)):
            print("Solution found after", problem.fitness_counter, "evaluations!")

            # Extend value until the end
            algorithm.population.best_fitness_history[problem.fitness_counter+1:] = algorithm.population.best_fitness_history[problem.fitness_counter]
            algorithm.population.average_fitness_history[problem.fitness_counter + 1:] = algorithm.population.average_fitness_history[problem.fitness_counter]
            algorithm.population.worst_fitness_history[problem.fitness_counter + 1:] = algorithm.population.worst_fitness_history[problem.fitness_counter]
            break

        #  time.sleep(0.5)
        # algorithm.population.print_stats()
        # input()

        #if (iter % 1000 == 0):
            #print("Iteration:", iter)

    # Print solution
    solution_individual = algorithm.population.population[algorithm.population.bestp]
    #solution_individual.print()

    return algorithm, problem
