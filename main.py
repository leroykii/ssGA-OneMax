import time
import cProfile
from Tests import Tests
from Visualization import Visualization

import numpy as np

#############################################
#############################################

def main():

    tests = Tests()

    print("beacon 2.087")

    if (0):
        print("Executing algorithm...")
        show_plot = 0

        tests.test_max_min_avg(show_plot)
        tests.test_crossover(show_plot, 4)
        tests.test_mutation(show_plot, 5)

        return
    else:
        print("Plotting previous executions...")
        # Load:
        first_tests = 0
        crossover = 0
        mutation = 0
        cross_and_mutation = 1;
        load_array = np.array([first_tests, crossover, mutation, cross_and_mutation])

        tests.load_data_from_files(load_array)

    print("Press ENTER to exit")
    
    return


#############################################
#############################################
if __name__ == '__main__':

    main()

