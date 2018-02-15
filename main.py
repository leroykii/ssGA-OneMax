import time
import cProfile
from Tests import Tests
from Visualization import Visualization
import numpy as np

#############################################
#############################################

def main():

    pr = cProfile.Profile()
    pr.enable()

    show_plot = 1

    tests = Tests()




    # tests.test_max_min_avg(show_plot)
    #tests.test_crossover(show_plot)
    #tests.test_mutation(show_plot)


    # Load:
    first_tests = 0
    crossover = 0
    mutation = 1
    load_array = np.array([first_tests, crossover, mutation, 0])

    tests.load_data_from_files(load_array)

    pr.disable()
    #pr.print_stats(sort="calls")


    print("Press ENTER to exit")
    input()

    return


#############################################
#############################################
if __name__ == '__main__':

    main()

