'''
Name: Jonayed Kader Nabil
ID: 22101100
Section: 17
'''

import random
from typing import List


class GeneticAlgo:
    def __init__(self, n: int, t: int, mutation_rate: int = 70, epoch: int = 100, crossover_type: str = 'one-point' ) -> None:
        self.n = n # number of courses
        self.t = t # number of time slots
        self.epoch = epoch
        self.mutation_rate = mutation_rate
        self.crossover_type = crossover_type
        self.initial_population = []
        self.penalized_population = []
        
    def create_population(self):
        n = self.n
        t = self.t 
        for _ in range(200):
            chromosome = [''.join(str(random.randint(0, 1)) for _ in range(n*t))]
            self.initial_population.append(chromosome)
        # print(self.initial_population)

    def penalty_calculation(self, population: List[list]):
        n = self.n
        t = self.t
        for chromosome in population:
            #overlap stuff
            total_overlap = 0
            overlap_ck = 0

            #consistency stuff
            consistency_arr = [0]*t # it should be [0]*n

            for i in range(n*t):
                gene =int(chromosome[0][i])

                #consistency                
                consistency_arr[i%n]+= gene
                
                #overlap
                overlap_ck+=gene
                if ((i+1)%n) == 0:
                    extra_course = overlap_ck - 1
                    total_overlap+= extra_course if extra_course > 0 else 0
                    overlap_ck = 0

            consistency_penalty = 0
            for repeat in consistency_arr:
                consistency_penalty+=abs(repeat-1)

            chromosome.append(-1*(total_overlap+consistency_penalty))

        # print(population)
        return population

    def one_point_crossover(self, p1: list, p2: list):
        p1 = p1[0]
        p2 = p2[0]
        #print(p1)
        #print(p2)

        length = len(p1)
        crossover_idx = random.randint(0,length-1)
        #print(crossover_idx)
        o1 = p1[:crossover_idx+1]+p2[crossover_idx+1:]
        o2 = p2[:crossover_idx+1]+p1[crossover_idx+1:]

        #print(o1)
        #print(o2)
        self.mutation(o1, o2)
    
    def two_point_crossover(self, p1: list, p2: list):
        p1 = p1[0]
        p2 = p2[0]
        n = len(p1)-1
        i1 = random.randint(0, n-1)
        i2 = random.randint(i1+1, n)

        tmp1 = p1[i1:i2]
        tmp2 = p2[i1:i2]

        o1 = p1[:i1]+tmp2+p1[i2:]
        o2 = p2[:i1]+tmp1+p2[i2:]

        self.mutation(o1, o2)

    def mutator(self, o: list):
        mutation_rate = self.mutation_rate
        length = len(o)
        nof_gene_to_mutate = random.choices([0,1,2,3], weights=[100-mutation_rate, mutation_rate, mutation_rate, mutation_rate], k=1)[0]
        gene_to_mutate = random.choices(list(range(length)), k=nof_gene_to_mutate)
        if nof_gene_to_mutate != 0:
            for idx in gene_to_mutate:
                cng_val = random.randint(0,1)
                o[idx] = str(cng_val)
                # o[idx] = 'x'

        return o

    def mutation(self, o1: str, o2: str):
        o1 =''.join(self.mutator(list(o1)))
        o2 =''.join(self.mutator(list(o2)))

        #print(o1)
        #print(o2)
        o = self.penalty_calculation([[o1],[o2]])
        self.penalized_population+=o


    def run(self):
        self.create_population()
        self.penalized_population = self.penalty_calculation(self.initial_population) # Calculate fitness for all population
        res = None
        not_the_best_res = float('-inf')
        loss = []
        for i in range(self.epoch):
            self.penalized_population = sorted(self.penalized_population, reverse=True, key=lambda gene: gene[1])[:50]
            if self.penalized_population[0][1] == 0:
                res = self.penalized_population[0]
                loss.append(i)
                break
            elif self.penalized_population[0][1] < 0 and self.penalized_population[0][1] > not_the_best_res :
                not_the_best_res = self.penalized_population[0][1]
                res = self.penalized_population[0]
    
    
            loss.append(self.penalized_population[0][1])
            if self.crossover_type == 'one-point':
                self.one_point_crossover(self.penalized_population[random.randint(0,49)], self.penalized_population[random.randint(0,49)])
            elif self.crossover_type == 'two-point':
                self.two_point_crossover(self.penalized_population[random.randint(0,49)], self.penalized_population[random.randint(0,49)])
        # print(loss)
        return res

    
if __name__ == "__main__":
    while True:
        print("n t (n<=t)")
        n, t = input().strip().split(" ")
        n, t = int(n), int(t)
        if t>=n:
            break
        else:
             print("n should be less or equal to t")
             
    mutation_rate = 70
    epoch = 100
    crossover_type = ["one-point", "two-point"]

    schedule = GeneticAlgo(n, t, mutation_rate, epoch, crossover_type[0]).run()
    print(f'{schedule[0]}\n{schedule[1]}')



