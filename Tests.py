from ProblemOneMax import ProblemOneMax
from Algorithm import Algorithm
from Visualization import Visualization
import numpy as np
import matplotlib.pyplot as plt


class Tests:
    def __init__(self):
        return

    def test_max_min_avg(self, show_plot):
        gene_number = 64
        gene_length = 1
        population_size = 128
        crossover_probability = 1.0
        target_fitness = gene_number * gene_length
        mutation_probability = 0.01
        MAX_ITERATION_STEPS = 2500
        NUM_EXECUTIONS = 10000

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
        np.save('output/target_fitness', target_fitness)

        if (show_plot):
            print("Ploting...")
            visualization = Visualization()
            visualization.all_fitness_history(all_best_fitness_history, all_worst_fitness_history,
                                          all_average_fitness_history, all_evaluations_history, target_fitness)

    def test_mutation(self, show_plot, test_number):

        gene_length = 1
        population_size = 128

        if (test_number == 1):  # config 1
            gene_number = 64
            target_fitness = gene_number * gene_length
            MAX_ITERATION_STEPS = 1200
            NUM_EXECUTIONS = 5000
            start_mutation_value = 0
            end_mutation_value = 1
            num_mutation_values = 6
            mutation_probability = np.linspace(start_mutation_value, end_mutation_value, num_mutation_values)
            mutation_probability = np.around(mutation_probability, 5)
            crossover_probability = 0.0

        if (test_number == 2):  # config 2
            gene_number = 64
            target_fitness = gene_number * gene_length
            MAX_ITERATION_STEPS = 1200
            NUM_EXECUTIONS = 150
            start_mutation_value = 0.0
            end_mutation_value = 0.2
            num_mutation_values = 11 # min 2
            mutation_probability = np.linspace(start_mutation_value, end_mutation_value, num_mutation_values)
            mutation_probability = np.around(mutation_probability, 5)
            crossover_probability = 0.0

        if (test_number == 3):  # config 3 - safety ratio
            gene_number = 64
            target_fitness = gene_number * gene_length
            MAX_ITERATION_STEPS = 1200
            NUM_EXECUTIONS = 1000
            start_mutation_value = 0.1
            end_mutation_value = 1.0
            num_mutation_values = 10  # min 2
            mutation_probability = np.linspace(start_mutation_value, end_mutation_value, num_mutation_values)
            mutation_probability = np.around(mutation_probability, 5)
            crossover_probability = 0.0


        if (test_number == 3):  # config 3 - safety ratio
            gene_number = 64
            target_fitness = gene_number * gene_length
            MAX_ITERATION_STEPS = 1200
            NUM_EXECUTIONS = 1000
            start_mutation_value = 0.1
            end_mutation_value = 1.0
            num_mutation_values = 10  # min 2
            mutation_probability = np.linspace(start_mutation_value, end_mutation_value, num_mutation_values)
            mutation_probability = np.around(mutation_probability, 5)
            crossover_probability = 0.0

        if (test_number == 4):
            gene_number = 64
            target_fitness = gene_number * gene_length
            MAX_ITERATION_STEPS = 3000
            NUM_EXECUTIONS = 3000
            start_mutation_value = 0.0
            end_mutation_value = 0.1
            num_mutation_values = 11  # min 2
            mutation_probability = np.linspace(start_mutation_value, end_mutation_value, num_mutation_values)
            mutation_probability = np.around(mutation_probability, 5)
            crossover_probability = 1.0

        if (test_number == 5):
            gene_number = 64
            target_fitness = gene_number * gene_length
            MAX_ITERATION_STEPS = 2500
            NUM_EXECUTIONS = 5000
            start_mutation_value = 0.0
            end_mutation_value = 0.02
            num_mutation_values = 11  # min 2
            mutation_probability = np.linspace(start_mutation_value, end_mutation_value, num_mutation_values)
            mutation_probability = np.around(mutation_probability, 5)
            crossover_probability = 1.0

        all_best_fitness_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])
        all_worst_fitness_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])
        all_average_fitness_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])
        all_safety_ratio_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])
        all_evaluations_history = np.zeros(NUM_EXECUTIONS)

        #mutation_probability = np.linspace(0, 2/target_fitness, num_mutation_values)

        mean_mutation_best_history = np.zeros([MAX_ITERATION_STEPS + 1, mutation_probability.size])
        mean_safety_ratio_history = np.zeros([MAX_ITERATION_STEPS + 1, mutation_probability.size])

        for mutation_iter in range(mutation_probability.size):

            print("Computing mutation probability:", mutation_probability[mutation_iter])

            for iter in range(NUM_EXECUTIONS):
                algorithm, problem = test(MAX_ITERATION_STEPS, crossover_probability, gene_length, gene_number,
                                          mutation_probability[mutation_iter], population_size, target_fitness)

                all_best_fitness_history[:, iter] = algorithm.population.best_fitness_history
                all_worst_fitness_history[:, iter] = algorithm.population.worst_fitness_history
                all_average_fitness_history[:, iter] = algorithm.population.average_fitness_history
                all_safety_ratio_history[:, iter] = algorithm.population.safety_ratio_history
                all_evaluations_history[iter] = problem.fitness_counter

            mean_mutation_best_history[:, mutation_iter] = all_best_fitness_history.mean(1)

            mean_safety_ratio_history[:, mutation_iter] = all_safety_ratio_history.mean(1) / (1-all_safety_ratio_history.mean(1))
            mean_safety_ratio_history[mean_safety_ratio_history == np.inf] = -1
            mean_safety_ratio_history[:, mutation_iter] = mean_safety_ratio_history[:, mutation_iter] / np.amax(mean_safety_ratio_history[:, mutation_iter])
            mean_safety_ratio_history[mean_safety_ratio_history < 0] = 1


        np.savetxt('output/mean_mutation_best_history', mean_mutation_best_history)
        np.savetxt('output/mutation_probability', mutation_probability)
        np.savetxt('output/mutation_safety_ratio', mean_safety_ratio_history)
        np.save('output/target_fitness', target_fitness)

        if (show_plot):
            # Visualization
            print("Ploting...")
            visualization = Visualization()
            visualization.mutation(mean_mutation_best_history, mutation_probability, target_fitness, mean_safety_ratio_history)

        return

    def test_crossover(self, show_plot, test_number):

        gene_length = 1
        population_size = 128

        if (test_number == 1):  # config 1
            gene_number = 64
            target_fitness = gene_number * gene_length
            MAX_ITERATION_STEPS = 1800
            NUM_EXECUTIONS = 5000
            # mutation_probability = 1.0 / target_fitness
            mutation_probability = 0.0
            start_crossover_value = 0
            end_crossover_value = 1.0
            num_crossover_values = 11
            crossover_probability = np.linspace(start_crossover_value, end_crossover_value, num_crossover_values)
            crossover_probability = np.around(crossover_probability, 5)

        if (test_number == 2):  # config 2
            gene_number = 64
            population_size = 512
            target_fitness = gene_number * gene_length
            MAX_ITERATION_STEPS = 8000
            NUM_EXECUTIONS = 3000
            # mutation_probability = 1.0 / target_fitness
            mutation_probability = 0.0
            start_crossover_value = 0
            end_crossover_value = 1.0
            num_crossover_values = 11
            crossover_probability = np.linspace(start_crossover_value, end_crossover_value, num_crossover_values)
            crossover_probability = np.around(crossover_probability, 5)

        if (test_number == 3):  # config 3
            gene_number = 64
            population_size = 512
            target_fitness = gene_number * gene_length
            MAX_ITERATION_STEPS = 10000
            NUM_EXECUTIONS = 100
            # mutation_probability = 1.0 / target_fitness
            mutation_probability = 0.0
            start_crossover_value = 0.1
            end_crossover_value = 1.0
            num_crossover_values = 10
            crossover_probability = np.linspace(start_crossover_value, end_crossover_value, num_crossover_values)
            crossover_probability = np.around(crossover_probability, 5)


        if (test_number == 4):  # config 4
            gene_number = 64
            population_size = 128
            target_fitness = gene_number * gene_length
            MAX_ITERATION_STEPS = 10000
            NUM_EXECUTIONS = 8000
            mutation_probability = 1.0 / target_fitness
            #mutation_probability = 0.0
            start_crossover_value = 0.55
            end_crossover_value = 1.0
            num_crossover_values = 10
            crossover_probability = np.linspace(start_crossover_value, end_crossover_value, num_crossover_values)
            crossover_probability = np.around(crossover_probability, 5)


        all_best_fitness_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])
        all_worst_fitness_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])
        all_average_fitness_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])
        all_evaluations_history = np.zeros(NUM_EXECUTIONS)
        all_safety_ratio_history = np.zeros([MAX_ITERATION_STEPS + 1, NUM_EXECUTIONS])

        mean_crossover_best_history = np.zeros([MAX_ITERATION_STEPS + 1, crossover_probability.size])
        mean_safety_ratio_history = np.zeros([MAX_ITERATION_STEPS + 1, crossover_probability.size])

        for cross_iter in range (crossover_probability.size):

            print("Computing crossover probability:", crossover_probability[cross_iter])

            for iter in range(NUM_EXECUTIONS):
                algorithm, problem = test(MAX_ITERATION_STEPS, crossover_probability[cross_iter], gene_length, gene_number,
                                          mutation_probability, population_size, target_fitness)

                all_best_fitness_history[:, iter] = algorithm.population.best_fitness_history
                all_worst_fitness_history[:, iter] = algorithm.population.worst_fitness_history
                all_average_fitness_history[:, iter] = algorithm.population.average_fitness_history
                all_safety_ratio_history[:, iter] = algorithm.population.safety_ratio_history
                all_evaluations_history[iter] = problem.fitness_counter

            mean_crossover_best_history[:, cross_iter] = all_best_fitness_history.mean(1)

            mean_safety_ratio_history[:, cross_iter] = all_safety_ratio_history.mean(1) / (1-all_safety_ratio_history.mean(1))
            mean_safety_ratio_history[mean_safety_ratio_history == np.inf] = -1
            mean_safety_ratio_history[:, cross_iter] = mean_safety_ratio_history[:, cross_iter] / np.amax(mean_safety_ratio_history[:, cross_iter])
            mean_safety_ratio_history[mean_safety_ratio_history < 0] = 1
            print(mean_safety_ratio_history[:, cross_iter])

        np.savetxt('output/mean_crossover_best_history', mean_crossover_best_history)
        np.savetxt('output/crossover_probability', crossover_probability)
        np.savetxt('output/crossover_safety_ratio', mean_safety_ratio_history)
        np.save('output/target_fitness', target_fitness)

        if (show_plot):
            # Visualization
            print("Ploting...")
            visualization = Visualization()
            visualization.crossover(mean_crossover_best_history, crossover_probability, target_fitness, mean_safety_ratio_history)

        return

    def load_data_from_files(self, load_array):

        if (load_array[0]):
            all_best_fitness_history = np.loadtxt('/media/leroy/Windows USB/output/all_best_fitness_history')
            all_worst_fitness_history = np.loadtxt('/media/leroy/Windows USB/output/all_worst_fitness_history')
            all_average_fitness_history = np.loadtxt('/media/leroy/Windows USB/output/all_average_fitness_history')
            all_evaluations_history = np.loadtxt('/media/leroy/Windows USB/output/all_evaluations_history')
            target_fitness = np.load('/media/leroy/Windows USB/output/target_fitness.npy')

            visualization = Visualization()

            visualization.all_fitness_history(all_best_fitness_history, all_worst_fitness_history,
                                              all_average_fitness_history, all_evaluations_history, target_fitness)



        if (load_array[1]):
            mean_crossover_best_history = np.loadtxt('output/mean_crossover_best_history')
            crossover_probability = np.loadtxt('output/crossover_probability')
            mean_safety_ratio_history = np.loadtxt('output/crossover_safety_ratio')
            target_fitness = np.load('output/target_fitness.npy')

            # Visualization
            visualization = Visualization()
            visualization.crossover(mean_crossover_best_history, crossover_probability, target_fitness, mean_safety_ratio_history)


        if (load_array[2]):
            mean_mutation_best_history = np.loadtxt('output/mean_mutation_best_history')
            mutation_probability = np.loadtxt('output/mutation_probability')
            mean_safety_ratio_history = np.loadtxt('output/mutation_safety_ratio')
            target_fitness = np.load('output/target_fitness.npy')

            # Visualization
            visualization = Visualization()
            visualization.mutation(mean_mutation_best_history, mutation_probability, target_fitness, mean_safety_ratio_history)


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
