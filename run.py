import random
import fun


"""
In list first generation: 
    [0] = a
    [1] = b
    [2] = c
    [3] = rank of individual 
"""

number_of_initial_population = 100
first_generation = [[random.random()] * 3 for _ in range(number_of_initial_population)]
x = []
y = []
ranks = []
multiplier = 5
with open('ES_data_7.dat', encoding='utf-8') as data:
    for line in data:
        x.append(float(line[:line.rfind(" ")]))
        y.append(float(line[line.rfind(" "):]))

for i in range(len(x)):
    ranks.append(i)

for individual in range(len(first_generation)):
    for index in range(len(x)):
        ranks[index] = fun.calculate(x[index], y[index], first_generation[individual][0], first_generation[individual][1], first_generation[individual][2])
    first_generation[individual].append(fun.Average(ranks))



print(fun.Mutate_uniform(first_generation, multiplier))

print("ok")
