class ProblemOneMax:
    def __init__(self, gene_number, gene_length, target_fitness):
        self.gene_number = gene_number
        self.gene_length = gene_length
        self.chromosome_length = gene_number * gene_length
        self.target_fitness = target_fitness
        self.tf_known = True
        self.fitness_counter = 0

        # TODO need rnadom uniform variable
        #random r = new Random()



    def evaluateStep(self): # TODO pass individual as argumetn
        self.fitness_counter += 1

        f = 0.0

        #for ii in range(1, self.chromosome_length):
            # if idinv.getallele
                #f = f + 1.0
         #indiv set_fitness
        #return f

      #  for (int i=0; i < CL; i++)
       #     if (indiv.get_allele(i) == 1)
        #        f = f + 1.0;
        # indiv.set_fitness(f);
        # return f;

        return


