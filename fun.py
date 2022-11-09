import math
from operator import itemgetter
import copy
from numpy import random


def function(x, y, a, b, c):
    return a * (x**2 - b * math.cos(c * math.pi * x)) - y


def calculate_rank(x, y, a, b, c):
    rank = abs(1/function(x, y, a, b, c))
    return rank


def get_average_rank(ranks):

    return sum(ranks) / len(ranks)


def get_mutated_by_uniform(x, y, generation, multiplier):
    new_generation = copy.copy(generation)
    for i in range(multiplier - 1):
        for individual in range(len(generation)):
            new_generation.append(copy.copy(generation[individual]))
    for new_individual in range(len(generation), len(new_generation)):
        new_generation[new_individual][0] = new_generation[new_individual][0] + random.uniform(0.0, 1.0)
        new_generation[new_individual][1] = new_generation[new_individual][1] + random.uniform(0.0, 1.0)
        new_generation[new_individual][2] = new_generation[new_individual][2] + random.uniform(0.0, 1.0)

    return get_generation_with_ranks(x, y, new_generation)


def get_mutated_by_normal(x, y, generation, multiplier):
    new_generation = copy.copy(generation)
    for i in range(multiplier-1):
        for individual in range(len(generation)):
            new_generation.append(copy.copy(generation[individual]))
    for new_individual in range(len(generation), len(new_generation)):
        new_generation[new_individual][0] = new_generation[new_individual][0] + random.random()
        new_generation[new_individual][1] = new_generation[new_individual][1] + random.random()
        new_generation[new_individual][2] = new_generation[new_individual][2] + random.random()

    return get_generation_with_ranks(x, y, new_generation)


def get_first_generation_with_ranks(x, y, generation):
    ranks = []
    for i in range(len(x)):
        ranks.append(i)

    for individual in range(len(generation)):
        for index in range(len(x)):
            ranks[index] = calculate_rank(x[index], y[index], generation[individual][0], generation[individual][1],
                                          generation[individual][2])
        generation[individual].append(abs(get_average_rank(ranks)))
    return generation


def get_generation_with_ranks(x, y, generation):
    ranks = []
    for i in range(len(x)):
        ranks.append(i)

    for individual in range(len(generation)):
        for index in range(len(x)):
            ranks[index] = calculate_rank(x[index], y[index], generation[individual][0], generation[individual][1],
                                          generation[individual][2])
        generation[individual][3] = abs(get_average_rank(ranks))
    return generation


def get_sorted_generation_by_rank(generation):
    return sorted(generation, key=itemgetter(3), reverse=True)

#zrobić sortowanie do libczy najbliższej 1
"""def get_sorted_generation_by_rank(generation, number_of_best_results):
    best_results = [0] * number_of_best_results
    individual = 0
    while individual < len(generation):
        if generation[individual][3] <= 1.0:
            best_results.sort()
            for rank in range(len(best_results)):
                if generation[individual][3] > best_results[rank]:
                    best_results[rank] = generation[individual][3]
                    break
        individual = individual + 1
    return best_results"""


def print_3_best_individuals(generation):
    for x in range(0, 3):
        print(get_sorted_generation_by_rank(generation)[x][3])
    print('\n')
