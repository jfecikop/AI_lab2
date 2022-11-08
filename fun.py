import math
from operator import itemgetter
import copy
from numpy import random


def function(x, y, a, b, c):
    return a * (x**2 - b * math.cos(c * math.pi * x)) - y


def calculate(x, y, a, b, c):
    rank = abs(1/function(x, y, a, b, c))
    return rank


def Average(list):

    return sum(list)/len(list)

def Mutate_uniform(list, multiplier):
    new_generation = copy.copy(list)
    for i in range(multiplier):
        for individual in range(len(list)):
            new_generation.append(copy.copy(list[individual]))
    for new_individual in range(len(list), len(new_generation)):
        new_generation[new_individual][0] = new_generation[new_individual][0] + random.uniform(0.0, 1.0)
        new_generation[new_individual][1] = new_generation[new_individual][1] + random.uniform(0.0, 1.0)
        new_generation[new_individual][2] = new_generation[new_individual][2] + random.uniform(0.0, 1.0)

    return new_generation

def Mutate_normal(list, multiplier):
    new_generation = copy.copy(list)
    for i in range(multiplier):
        for individual in range(len(list)):
            new_generation.append(copy.copy(list[individual]))
    for new_individual in range(len(list), len(new_generation)):
        new_generation[new_individual][0] = new_generation[new_individual][0] + random.random()
        new_generation[new_individual][1] = new_generation[new_individual][1] + random.random()
        new_generation[new_individual][2] = new_generation[new_individual][2] + random.random()

    return new_generation


def Sort(list):
    return sorted(list, key=itemgetter(3), reverse=True)