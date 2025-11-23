import random

Cities = 5
Population_Size = 6
Generations = int(46) # Increasing The Value Will Increase The Accuracy Of The Result
Distance_Matrix = [
    [0,42,14,50,78],
    [24,0,27,60,71],
    [71,28,0,39,44],
    [29,10,95,0,62],
    [51,20,17,76,0]
]

def initial_population():
    Population = []

    for i in range(Population_Size):
        current = random.sample(range(Cities), 5)
        current.append(current[0])
        Population.append(current)

    return Population

def fitness_calculation(Population):
    Fitness = []

    for individual in Population:
        distance = 0
        
        for i in range(len(individual)-1):
            row = individual[i]
            column = individual[i+1]
            distance += Distance_Matrix[row][column]
            
        current_fitness = 1/distance
        Fitness.append(current_fitness)
    
    return Fitness

def selection_roulette_wheel(Fitness):
    Selected_Ancestor = []
    Cumulative_Range = []
    cumulative_sum = 0

    for value in Fitness:
        cumulative_sum += value
        Cumulative_Range.append(cumulative_sum)

    Total_Fitness = cumulative_sum
    Total_Ancestors = 1

    while Total_Ancestors <= 2:
        spin_roulette_wheel = random.uniform(0, Total_Fitness)
        selected = -1

        for j in range(len(Cumulative_Range)):
            if spin_roulette_wheel <= Cumulative_Range[j]:
                selected = j
                break
        
        if Total_Ancestors == 2:
            if Selected_Ancestor[0] == selected:
                 Total_Ancestors -= 1
            else:
                Selected_Ancestor.append(selected)
        else:
            Selected_Ancestor.append(selected)
        
        Total_Ancestors += 1
        
    return Selected_Ancestor

def crossover(Ancestor_1, Ancestor_2):
    first = list(Ancestor_1)
    second = list(Ancestor_2)
    third = []
    first.pop()
    second.pop()
    length = len(first)
    start_point = random.randint(0, length-1)
    available = length-start_point
    segment_length = random.randint(1, min(available, length-1))
    end_point = start_point+segment_length; 
    segment = first[start_point:end_point]

    for element in second:
        if element not in segment:
            third.append(element)

    third[start_point:start_point] = segment
    third.append(third[0])

    print(f'Ancestor Segment {start_point+1}-{end_point}:\t {segment}')

    return third

def mutation(Descendant):
    Mutated_Descendant = list(Descendant)

    if random.randint(0,1):
        point_1, point_2 = random.sample(range(1, len(Mutated_Descendant)-2), 2)
        temp = Mutated_Descendant[point_1]
        Mutated_Descendant[point_1] = Mutated_Descendant[point_2]
        Mutated_Descendant[point_2] = temp
    
    return Mutated_Descendant

def new_generation(Population, Fitness, Mutated_Descendant):    
    Population.append(Mutated_Descendant)
    Descendants = []
    Descendants.append(Mutated_Descendant)
    Descendants_Fitness = fitness_calculation(Descendants)

    print(f'Mutated Descendant:\t {Mutated_Descendant} --> Fitness: {Descendants_Fitness}\n')

    Fitness.append(Descendants_Fitness[0])
    Adaptability = 1e9
    Natural_Selection = None

    for i in range(len(Population)):
        if Fitness[i] < Adaptability:
            Adaptability = Fitness[i]
            Natural_Selection = i

    if Natural_Selection == len(Population)-1:
        print(f'Natural Selection: Descendant --> {Descendant}')
    else:
        print(f'Natural Selection: Population {Natural_Selection+1} --> {Population[Natural_Selection]}')

    Population.pop(Natural_Selection)

    return Population

def calculate_result(Population):
    minimum = 1e9
    shortest_path = []

    for individual in Population:
        distance = 0
        
        for i in range(len(individual)-1):
            row = individual[i]
            column = individual[i+1]
            distance += Distance_Matrix[row][column]

        if distance < minimum:
            minimum = distance
            shortest_path = individual
    
    return shortest_path, minimum

Population = initial_population()

for gen in range(Generations):
    print(f'\nGeneration: {gen+1}\n')

    Fitness = fitness_calculation(Population)

    for i in range(len(Population)):
        print(f'Population {i+1}: {Population[i]} --> Fitness: {Fitness[i]}')

    Ancestor_1_Index, Ancestor_2_Index = selection_roulette_wheel(Fitness)

    print(f'\nAncestor {Ancestor_1_Index+1}:\t\t {Population[Ancestor_1_Index]}')
    print(f'Ancestor {Ancestor_2_Index+1}:\t\t {Population[Ancestor_2_Index]}')

    Descendant = crossover(Population[Ancestor_1_Index], Population[Ancestor_2_Index])
    Mutated_Descendant = mutation(Descendant)

    print(f'Descendant:\t\t {Descendant}')

    New_Generation = new_generation(Population, Fitness, Mutated_Descendant)
    Population = list(New_Generation)
    Current_Best_Result = calculate_result(Population)

    print(f'\nCurrent Generation Result\nShortest Circular Tour: {Current_Best_Result[0]}')
    print(f'Total Travel Cost: {Current_Best_Result[1]}\n')