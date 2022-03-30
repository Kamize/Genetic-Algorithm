from math import sin, cos
from numpy import random

MUTATION_RATE = 0.1
ELITISM = 2
POPULATION_SIZE = 10
GENERATION_LIMIT = 700
SHOW_NUM = 20

def main():
    # Generate population
    population = []
    populate(population, Solution, POPULATION_SIZE)

    # Show gen 0 top solution
    show_top(population, 0)

    # Show top solutions for a number of generation
    for generation in range(1, GENERATION_LIMIT+1):
        generate_next_generation(population)
        if generation%(GENERATION_LIMIT//SHOW_NUM) == 0:
            show_top(population, generation)

class Solution:
    def __init__(self, genome=None):
        '''
            Initialization. Generate random genome if not given.
        '''
        self.genome_length = 32     # The higher the value, the more accurate the solution can be.
        if genome is None:
            genome = "".join([random.choice(("0", "1")) for _ in range(self.genome_length)])
        self.genome = genome

    def decode(self):
        '''
            Returns a tuple of x and y value calculated from genome.
        '''
        def bin_range(binary):
            '''
                Returns a real number of range 0 to 1 from binary representation
            '''
            return int(binary, 2)/int("1"*len(binary), 2)

        x_range = (-5, 5)
        y_range = (-5, 5)

        # Calculates x and y by adding their minimum value with the difference of their maximum and minimum value multiplied by the real number representation of each half of genome.
        x = x_range[0]+(x_range[1]-x_range[0])*bin_range(self.genome[:self.genome_length//2])
        y = y_range[0]+(y_range[1]-y_range[0])*bin_range(self.genome[self.genome_length//2:])

        return x, y

    def fitness(self):
        '''
            Returns a fitness value based on its genome.
        '''
        x, y = self.decode()
        return ((cos(x)+sin(y))**2)/(x**2+y**2)


def populate(population, Organism, num) :
    '''
        Populates a population with a number of organisms
    '''
    population.extend([Organism() for _ in range(num)])
    population.sort(key=Organism.fitness, reverse=True)
    

# Parent Picking
def crossover_parents(population):
    '''
        Returns 2 parents for crossover purpose. Selected randomly with fitness value as weight
    '''
    # Calculating weight
    fitness_values = [entity.fitness() for entity in population]
    fitness_sum = sum(fitness_values)
    weight = [value/fitness_sum for value in fitness_values]

    # Choosing parents
    parent1, parent2 = random.choice(population, size=2, replace=False, p=weight)
    return parent1, parent2

# Crossover
def crossover(genome1, genome2):
    '''
        Returns 2 genomes from the crossover of genome1 and genome2
    '''
    # Determining crossover point
    div = random.randint(len(genome1))

    # Crossing
    genome1 = genome1[:div]+genome2[div:]
    genome2 = genome2[:div]+genome1[div:]
    return genome1, genome2

def crossover_children(Organism, parent1, parent2) :
    '''
        Returns 2 children from the corssover of parent1 and parent2
    '''
    # Getting genomes for crossover
    genome1, genome2 = crossover(parent1.genome, parent2.genome)

    # Making an instance of Organism
    child1 = Organism(genome1)
    child2 = Organism(genome2)
    return child1, child2

# Mutation
def mutated(genome) :
    '''
        Returns a mutated genome randomly based on mutation rate.
    '''
    # Creating list from a genome string. List is mutable, string is not.
    genome = list(genome)

    # Mutating nucleotides based on mutation rate
    for idx, nucleotide in enumerate(genome):
        if random.uniform()<=MUTATION_RATE:
            if nucleotide=="0":
                genome[idx] = "1"
            else:
                genome[idx] = "0"

    # Rejoining list to become a string
    genome = "".join(genome)
    return genome

def mutate_population(population):
    '''
        Mutates a population except for the elites.
    '''
    for entity in population[ELITISM:]:
        entity.genome = mutated(entity.genome)

# Generate next generation
def generate_next_generation(population):
    '''
        Replaces current population with its next generation.
    '''
    # Initialization of next generation
    Organism = type(population[0])
    population_size = len(population)
    next_generation = []

    # Elitism
    next_generation.extend(population[:ELITISM])
    
    # Adding children to next generation
    while len(next_generation) < population_size:
        parent1, parent2 = crossover_parents(population)
        child1, child2 = crossover_children(Organism, parent1, parent2)
        next_generation.extend((child1,child2))

    # Mutating next generation
    mutate_population(next_generation)
    # Sorting next generation based on its fitness value
    next_generation.sort(key=Organism.fitness, reverse=True)

    # Replacing current population with its next generation
    population[:] = next_generation

def show_top(population, generation):
    '''
        Prints information about top solution of a population
    '''
    top = population[0]
    print(f"top solution of generation {generation}:")
    print(f"{'genome':<30}= {top.genome}")
    print(f"{'(x,y)':<30}= {top.decode()}")
    print(f"{'h(x,y)':<30}= {top.fitness()}")
    print()

if __name__ == "__main__":
    main()