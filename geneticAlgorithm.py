from math import sin, cos
import random

# heuristic equation
def h(x,y) :
    hasil = (pow((cos(x) + sin(y)),2)) / pow(x,2)+pow(y,2)
    return hasil
#Creating a population
def generate_genome(genome_size):
    pass

def generate_population(population, genome_size) :
    return  [[random.choice([0,1]) for _ in range(genome_size)] for _ in range(population_size)]

#Decode Cromosome
def decode(genome) : # Cepet2an
    pass
    #domain function
    # d_function = lambda rmax,rmin, start_bit, end_bit :

#Fitness Function
def fitness(genome) : # Talitha
    pass

#Parent Picking
def elitism(population, k) :
    pass

#Crossover
def crossover(parent1, parent2, crossover_rate) :
    pass

#Mutation
def mutation(genome, mutation rate) : # Talitha
    pass
#New Generation

def main():
    x = 10
    y = 5
    print(h(x,y))

main()