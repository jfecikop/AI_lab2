import random
import fun
import copy

"""
In list first generation: 
    [0] = a
    [1] = b
    [2] = c
    [3] = rank of individual 
"""

number_of_initial_population = 3
first_generation = [[random.random()] * 3 for _ in range(number_of_initial_population)]
x = []
y = []
ranks = []
multiplier = 5
number_of_best_results = 3

with open('ES_data_7.dat', encoding='utf-8') as data:
    for line in data:
        x.append(float(line[:line.rfind(" ")]))
        y.append(float(line[line.rfind(" "):]))

generation = copy.copy(fun.get_first_generation_with_ranks(x, y, first_generation))
print(fun.get_sorted_generation_by_rank(generation, number_of_best_results))

generation = fun.get_mutated_by_uniform(x, y, generation, multiplier)
print(fun.get_sorted_generation_by_rank(generation, number_of_best_results))

while fun.get_sorted_generation_by_rank(generation, number_of_best_results)[1] != 1.0:
    generation = fun.get_mutated_by_normal(x, y, generation, multiplier)
    print(fun.get_sorted_generation_by_rank(generation, number_of_best_results))

print("Program ended")
