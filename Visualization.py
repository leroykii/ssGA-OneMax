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