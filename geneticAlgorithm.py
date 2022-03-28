from math import sin, cos
import random

MUTATION_RATE = 0.1

def main():
    x = 10
    y = 5
    print(h(x,y))

class Solution:
    def __init__(self, genome=None):
        '''
            Initialization. Generate random genome if not given.
        '''
        self.genome_length = 32
        if genome is None:
            genome = "".join([random.choice(("0", "1")) for _ in range(self.genome_length)])
        self.genome = genome

    def decode(self):
        '''
            returns a tuple of x and y value calculated from genome.
        '''
        def bin_range(binary):
            return int(binary, 2)/int("1"*len(binary), 2)
        x_range = (-5, 5)
        y_range = (-5, 5)
        x = x_range[0]+(x_range[1]-x_range[0])*bin_range(self.genome[:self.genome_length//2])
        y = y_range[0]+(y_range[1]-y_range[0])*bin_range(self.genome[self.genome_length//2:])
        return x, y

    def fitness(self):
        '''
            returns a fitness value based on its genome.
        '''
        x, y = self.decode()
        return ((cos(x)+sin(y))**2)/(x**2+y**2)


def population(population_size) :
    return  [Solution() for _ in range(population_size)]

# Parent Picking
def crossover_parent(population):
    pass

# Crossover
def crossover(parent1, parent2, crossover_rate) :
    pass


# Mutation
def mutation(Solution) :
    '''
        returns a mutated genome randomly based on mutation rate.
    '''
    m = list(Solution.genome)
    if random.uniform(0,1) <= MUTATION_RATE :
        for digit in range(len(m)) : 
            if m[digit] == '0' :
                m[digit] = '1'
            else :
                m[digit] = '0'
    Solution.genome = "".join(m)

# New Generation

# Generate next generation
def generate_next_generation():
    pass



if __name__ == "__main":
    main()