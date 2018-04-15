from bitarray import bitarray
import numpy

class Chromosome:

    def __init__(self, chromosome_length):
        self.alleles = bitarray(chromosome_length)
        self.alleles.setall(False)
        self.chromosome_length = chromosome_length

        # Initialize vector randomly
        for ii in range(0, chromosome_length):
            if (numpy.random.random() > 0.5):
                self.alleles[ii] = 1
            else:
                self.alleles[ii] = 0

    def print(self):
        print("Bit array:", self.alleles)
        # print("Number of ones:", self.alleles.count(True))
        return

