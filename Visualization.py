import matplotlib.pyplot as plt
import numpy as np

class Visualization:
    def __init__(self):
        return

    def fitness_history(self, population, num_evaluations):

        max_possible_fitness = population.chromosome_length
        ymin = population.average_fitness_history[0] - max_possible_fitness/10

        plt.figure()
        axes = plt.gca()
        axes.set_ylim([ymin, max_possible_fitness+2])

        population.average_fitness_history[num_evaluations+1::] = population.average_fitness_history[num_evaluations]
        population.best_fitness_history[num_evaluations+1::] = population.best_fitness_history[num_evaluations]
        population.worst_fitness_history[num_evaluations+1::] = population.worst_fitness_history[num_evaluations]

        plt.plot(population.average_fitness_history)
        plt.plot(population.best_fitness_history)
        plt.plot(population.worst_fitness_history)

        plt.axvline(x=num_evaluations, color='r', linestyle='--')
        plt.show()

        return


    def all_fitness_history(self, all_best_fitness_history, all_worst_fitness_history,
                            all_average_fitness_history, all_evaluations_history):

        # https: // matplotlib.org / api / _as_gen / matplotlib.axes.Axes.fill_between.html

        y_fit = all_average_fitness_history.mean(1)
        ymin_fit = all_worst_fitness_history.mean(1)
        ymax_fit = all_best_fitness_history.mean(1)

        x = np.linspace(0, len(y_fit), len(y_fit))

        plt.plot(ymax_fit, '--', label='Best')
        plt.plot(x, y_fit, 'k-', label='Average')
        plt.plot(ymin_fit, '--', label='Worst')
        plt.fill_between(x, ymin_fit, ymax_fit, alpha=0.1, color='r')

        plt.axvline(x=min(all_evaluations_history), color='r', linestyle='--')

        plt.legend()
        plt.show()

        # savefig('foo.png')
        # savefig('foo.png', bbox_inches='tight')
        input()


        if (False):
            plt.figure(1)
            plt.plot(all_best_fitness_history.mean(1))
            plt.plot(all_average_fitness_history.mean(1))
            plt.plot(all_worst_fitness_history.mean(1))
           # plt.show()

        #axes = plt.gca()
        #axes.set_ylim([0, 30])
        #plt.plot(all_best_fitness_history)
#       print(max(max(all_best_fitness_history)))

        return


    def crossover(self, mean_crossover_best_history, crossover_probability, target_fitness):
        plt.figure(1)
        plt.plot(mean_crossover_best_history)
        plt.legend(crossover_probability, title='Crossover probability:').draggable(True)

        plt.axhline(y=target_fitness, color='r', linestyle='--', alpha=0.7)

        plt.show()
        return

    def mutation(self, mean_mutation_best_history, mutation_probability, target_fitness):
        plt.figure(2)
        plt.plot(mean_mutation_best_history)
        plt.legend(mutation_probability, title='Mutation probability:').draggable(True)

        plt.axhline(y=target_fitness, color='r', linestyle='--', alpha=0.7)

        plt.show()
        return