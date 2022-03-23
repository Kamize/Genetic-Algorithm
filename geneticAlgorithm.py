from math import sin, cos
import random

# heuristic equation
def h(x,y) :
    hasil = (pow((cos(x) + sin(y)),2)) / pow(x,2)+pow(y,2)
    return hasil
#Creating a population
def generate_population(population, chromosome) :
    return  [[random.choice([0,1]) for _ in range(chromosome_size)] for _ in range(population_size)]

#Decode Cromosome
def decode(chromosome) :
    x_max = 5
    x_min = -5

    y_max = 5
    y_min = -5

    #domain function
    # d_function = lambda rmax,rmin, start_bit, end_bit :

#Fitness Function
def fitness(chromosome) :
    x,y = decode(chromosome)
    return(x,y)

#Parent Picking
def tournament_selection(population, k) :
    candidate = [population[random.randrange(0,len(population))] for _ in range(k)]

#Crossover
def crossover(parent1, parent2, crossover_rate) :
    
#Mutation
def mutation(chromosome, mutation rate) :
    
#New Generation


def main():
    x = 10
    y = 5
    print(h(x,y))

main()