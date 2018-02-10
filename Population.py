from Individual import Individual

class Population:
    def __init__(self, population_size, chromosome_length):

        self.population_size = population_size
        # todo array de individuals en python
        # population = Individual[3]
        self.chromosome_length = chromosome_length

        for ii in range(0, population_size):
            aa = 1
            # arraypop[ii] = Individual(chromosome_length)

        self.bestp = 0
        self.worstp = 0
        self.bestf = 0
        self.avgf = 0
        self.worstf = 9999999999.0
        self.BESTF = 0

        return

    #todo
    #set_ith/get_ith


    #todo
    def compute_stats(self):
        return

    # todo
    # def print(self):
        # for pp in range(0, self.population_size):

    def print_stats(self):
        print("BESTF:", self.BESTF)
        print("bestp:", self.bestp)
        print("bestf:", self.bestf)
        print("worstp:", self.worstp)
        print("worstf:", self.worstf)
        print("avgf:", self.avgf)
