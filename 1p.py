import random

# Constants
POPULATION_SIZE = 10
GENERATIONS = 50
CROSSOVER_PROBABILITY = 0.85
MUTATION_PROBABILITY = 0.1
UNIFORM_CROSSOVER_RATE = 0.5
MIN_LOVE_POTIONS = 3
MIN_SKIVING_SNACKBOXES = 2
MAX_WEIGHT = 30

# Product weights and values
PRODUCTS = {
    "Decoy Detonators": {"weight": 4, "value": 10},
    "Love Potion": {"weight": 2, "value": 8},
    "Extendable Ears": {"weight": 5, "value": 12},
    "Skidivinf Snackbox": {"weight": 5, "value": 6},
    "Fever Fudge": {"weight": 2, "value": 3},
    "Puking Pastilles": {"weight": 1.5, "value": 2},
    "Nosebleed Nougat": {"weight": 1, "value": 2}
}


# Chromosome representation: binary string indicating whether each product is included or not
# Example: "1001000100" means Love Potion 1, Love Potion 4, Skiving Snackbox 9 are selected
def generate_chromosome():
    return ''.join(random.choice('01') for _ in range(len(PRODUCTS)))

#Calcularmos el fitness de cada chromosoma, para esto debo crear un diccionario para guardar chromosoma, peso y valor
def fitness(chromosome):
    total_value = 0
    total_weight = 0
    love_potions_count = 0
    skiving_snackboxes_count = 0
    chromosome_data = {}
    for i, gene in enumerate(chromosome):
        if gene == '1':
            product = list(PRODUCTS.keys())[i]
            total_value += PRODUCTS[product]["value"]
            total_weight += PRODUCTS[product]["weight"]
            if product == "Love Potion":
                love_potions_count += 1
            elif product == "Skiving Snackbox":
                skiving_snackboxes_count += 1
    
    #Aqui vamos a generar un diccionario que almacene como key el chromosoma y su informacion respectiva, peso y valor
    chromosome_data[chromosome] = {"weight": total_weight,"value": total_value, "Love Potions Count": love_potions_count, "Skidiving Snackbox": skiving_snackboxes_count}

    
    print(chromosome_data)
                
    # Apply additional constraints
    if love_potions_count < MIN_LOVE_POTIONS or skiving_snackboxes_count < MIN_SKIVING_SNACKBOXES or total_weight > MAX_WEIGHT:
        return 0
    return total_value

# Roulette wheel selection
def select_parent(population, fitnesses):
    total_fitness = sum(fitnesses)
    if total_fitness == 0:
        # If total_fitness is 0, no valid chromosomes are present, so return a random chromosome
        return random.choice(population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, chromosome in enumerate(population):
        current += fitnesses[i]
        if current > pick:
            return chromosome

# Uniform crossover
def crossover(parent1, parent2):
    child1 = ""
    child2 = ""
    for i in range(len(parent1)):
        if random.random() < UNIFORM_CROSSOVER_RATE:
            child1 += parent1[i]
            child2 += parent2[i]
        else:
            child1 += parent2[i]
            child2 += parent1[i]
    return child1, child2

# Mutation
def mutate(chromosome):
    mutated_chromosome = ""
    for gene in chromosome:
        if random.random() < MUTATION_PROBABILITY:
            mutated_chromosome += '1' if gene == '0' else '0'
        else:
            mutated_chromosome += gene
    return mutated_chromosome







# Generamos la poblacion inicial
population = [generate_chromosome() for _ in range(POPULATION_SIZE)]
print(population)

#Comenzamos con las generaciones
for generation in range(GENERATIONS):
    #Calculamos el Fitness de cada chromosoma
    print(f'GENERATION: {generation} \n')
    fitnesses = [fitness(chromosome) for chromosome in population]
    
    print("====================")

    # Select parents and perform crossover
    new_population = []
    for _ in range(POPULATION_SIZE // 2):
        parent1 = select_parent(population, fitnesses)
        parent2 = select_parent(population, fitnesses)
        child1, child2 = crossover(parent1, parent2)
        new_population.extend([mutate(child1), mutate(child2)])

    population = new_population
    
print(" ******************************************* ")

print("NEW POPULATION: ")
print(population)

# Find the best solution
best_chromosome = max(population, key=fitness)
best_fitness = fitness(best_chromosome)

print("Best solution found:")
print("Chromosome:", best_chromosome)
print("Fitness:", best_fitness)
