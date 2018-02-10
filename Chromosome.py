from bitarray import bitarray
import random

class Chromosome:

    def __init__(self, allele_length):
        self.alleles = bitarray(allele_length)
        self.alleles.setall(False)
        self.allele_length = allele_length

        # Initialize vector randomly
        for ii in range(0, allele_length):
            if (random.uniform(0, 1) > 0.5):
                self.alleles[ii] = 1
            else:
                self.alleles[ii] = 0

    def print(self):
        print("Bit array:", self.alleles)
        print("Number of ones:", self.alleles.count(True))
        return

