import random


MAX_CAPACITY = 30
POPULATION = 10
GENERATIONS = 50
CROSSOVER_PROBABILITY = 0.85
MUTATION_PROBABILITY = 0.1
UNIFORM_CROSSOVER  =0.5
MIN_LOVE_POTIONS = 3
MIN_SKIDIVING_SNACKBOXES = 2

PRODUCTS = {
    "Decoy Detonators": {"weight": 4, "value": 10},
    "Love Potion": {"weight": 2, "value": 8},
    "Extendable Ears": {"weight": 5, "value": 12},
    "Skidivinf Snackbox": {"weight": 5, "value": 6},
    "Fever Fudge": {"weight": 2, "value": 3},
    "Puking Pastilles": {"weight": 1.5, "value": 2},
    "Nosebleed Nougat": {"weight": 1, "value": 2}
}


def generate_chromosomes():
    chromosomes = [[random.choice('01') for i in range(POPULATION) for e in range(len(PRODUCTS))]]
    # for i in range(POPULATION):
    #     for e in range(len(PRODUCTS)):
    #         chromosomes.append(random.choice('01'))
    print(chromosomes)

generate_chromosomes()