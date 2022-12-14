from fodder import *
import pandas as pd
import random
import numpy as np

# ilość zwierząt
rabbits = Animal(number=8, protein_need=30, fat_need=20, carbohydrates_need=40)
dogs = Animal(number=10, protein_need=120, fat_need=100, carbohydrates_need=110)
cats = Animal(number=12, protein_need=60, fat_need=90, carbohydrates_need=110)
frogs = Animal(number=6, protein_need=20, fat_need=10, carbohydrates_need=35)
gecko = Animal(number=9, protein_need=10, fat_need=5, carbohydrates_need=20)

animals = [rabbits, dogs, cats, frogs, gecko]

# koszty karmy w zależności od dnia
price1 = {1: 20, 2: 15, 3: 22, 4: 26, 5: 26, 6: 25, 7: 18, 8: 21,
          9: 22, 10: 17, 11: 19, 12: 22, 13: 18, 14: 16, 15: 29,
          16: 22, 17: 22, 18: 22, 19: 23, 20: 29, 21: 19, 22: 28,
          23: 15, 24: 22, 25: 23, 26: 21, 27: 22, 28: 29, 29: 15, 30: 25}

price2 = {1: 29, 2: 20, 3: 22, 4: 21, 5: 28, 6: 18, 7: 19, 8: 26,
          9: 19, 10: 28, 11: 25, 12: 20, 13: 20, 14: 25, 15: 24,
          16: 20, 17: 28, 18: 15, 19: 18, 20: 29, 21: 21, 22: 24,
          23: 28, 24: 18, 25: 17, 26: 19, 27: 22, 28: 23, 29: 18, 30: 24}

price3 = {1: 18, 2: 16, 3: 17, 4: 26, 5: 26, 6: 27, 7: 20, 8: 28,
          9: 15, 10: 19, 11: 16, 12: 20, 13: 23, 14: 25, 15: 17,
          16: 21, 17: 25, 18: 23, 19: 22, 20: 22, 21: 16, 22: 29,
          23: 21, 24: 16, 25: 19, 26: 18, 27: 19, 28: 25, 29: 29, 30: 19}

price4 = {1: 11, 2: 12, 3: 13, 4: 14, 5: 19, 6: 17, 7: 10, 8: 17,
          9: 20, 10: 10, 11: 17, 12: 13, 13: 15, 14: 19, 15: 10,
          16: 18, 17: 17, 18: 15, 19: 14, 20: 18, 21: 16, 22: 16,
          23: 16, 24: 12, 25: 13, 26: 14, 27: 10, 28: 20, 29: 13, 30: 11}

price5 = {1: 10, 2: 15, 3: 10, 4: 15, 5: 12, 6: 11, 7: 15, 8: 11,
          9: 14, 10: 17, 11: 16, 12: 18, 13: 12, 14: 14, 15: 12,
          16: 18, 17: 17, 18: 12, 19: 10, 20: 18, 21: 12, 22: 16,
          23: 15, 24: 13, 25: 18, 26: 19, 27: 10, 28: 11, 29: 11, 30: 16}

# rodzaje karmy
fodder1 = Fodder(protein=15, fat=10, carbohydrates=30, price=price1)
fodder2 = Fodder(protein=40, fat=20, carbohydrates=15, price=price2)
fodder3 = Fodder(protein=25, fat=45, carbohydrates=20, price=price3)
fodder4 = Fodder(protein=20, fat=15, carbohydrates=25, price=price4)
fodder5 = Fodder(protein=10, fat=20, carbohydrates=15, price=price5)

fodders = [fodder1, fodder2, fodder3, fodder4, fodder5]

# pojemność magazynu do składowania karmy, ogólna pojemność to 30kg i następnie po 10kg na rodzaj karmy
space = Warehouse(space=30, fodder1_space=10, fodder2_space=10, fodder3_space=10)

# minimalne makroskladniki potrzebne ndziennie

macro_need_per_day = 0
for i in animals:
    macro_need_per_day = np.add(macro_need_per_day, i.get_macro_need())

protein_need_per_day = macro_need_per_day[0]
fat_need_per_day = macro_need_per_day[1]
carbo_need_per_day = macro_need_per_day[2]

#print(macro_need_per_day)
# generowanie losowego rozwiązania


'''def create_random_solution():
    random_solution = []

    for i in range(1, 31):
        protein, fat, carb = 0, 0, 0
        fod1, fod2, fod3 = 0, 0, 0
        while protein < protein_need_per_day or fat < fat_need_per_day or carb < carbo_need_per_day:
            rand = random.randint(0, 2)
            if rand == 0:
                fod1 += 1
            if rand == 1:
                fod2 += 1
            if rand == 2:
                fod3 += 1

            protein += fodders[rand].protein
            fat += fodders[rand].fat
            carb += fodders[rand].carbohydrates

        random_solution.append([fod1, fod2, fod3])
    return random_solution'''


def create_random_solution():
    random_solution = []

    for i in range(1, 31):
        fod1 = random.randint(10, 60)
        fod2 = random.randint(10, 60)
        fod3 = random.randint(10, 60)
        fod4 = random.randint(10, 60)
        fod5 = random.randint(10, 60)
        random_solution.append([fod1, fod2, fod3, fod4, fod5])

    return random_solution


random_solution = create_random_solution()
#print(random_solution)
#print(len(random_solution))


# funkcja celu - argumentem jest rozwiązanie
# sumaryczna wartość zakupionych karm na przestrzeni miesiąca


def compute_total_cost(solution):
    total_cost = 0
    for eidx, elem in enumerate(solution):
        daily_cost = 0
        day = eidx + 1
        for inx, fodder in enumerate(elem):
            daily_cost += fodders[inx].price[day] * fodder
        total_cost += daily_cost
    return total_cost


total_cost = compute_total_cost(random_solution)
#print(total_cost)


# sprawdzanie czy w każdym dniu zapewniliśmy minimum zapotrzebowania - jeśli nie nakładamy karę do kosztu całkowitego
# gdy przepuścimy rozwiazanie niedopuszczalne to nakładamy bardzo dużą karę
def check_penalty(solution):
    penalty_price = 10000
    for elem in solution:
        protein, fat, carbo = 0, 0, 0
        for inx, fodder in enumerate(elem):
            protein += fodders[inx].protein * fodder
            fat += fodders[inx].fat * fodder
            carbo += fodders[inx].carbohydrates * fodder
        if protein < protein_need_per_day or fat < fat_need_per_day or carbo < carbo_need_per_day:
            # można też dodać ewentualny warunek na zbyt duże przekroczenie zapotrzebowania
            return penalty_price

    return 0


# kara za jeden dzien
def check_macro_penalty(f1, f2, f3, f4, f5):
    penalty_price = float('inf')
    if f1 < 0 or f2 < 0 or f3 < 0 or f4 < 0 or f5 < 0:
        return penalty_price
    protein = fodders[0].protein * f1 + fodders[1].protein * f2 + fodders[2].protein * f3 + fodders[3].protein * f4 + \
              fodders[4].protein * f5
    fat = fodders[0].fat * f1 + fodders[1].fat * f2 + fodders[2].fat * f3 + fodders[3].fat * f4 + \
          fodders[4].fat * f5
    carbo = fodders[0].carbohydrates * f1 + fodders[1].carbohydrates * f2 + fodders[2].carbohydrates * f3 + \
            fodders[3].carbohydrates * f4 + fodders[4].carbohydrates * f5
    if protein < protein_need_per_day or fat < fat_need_per_day or carbo < carbo_need_per_day:
        return penalty_price
    return 0


# jako sąsiedztwo przyjmiemy


# funkcja celu dla kazdego dnia


def daily_cost(f1, f2, f3, f4, f5, day):
    return fodder1.price[day] * f1 + fodder2.price[day] * f2 + fodder3.price[day] * f3 + fodder4.price[day] * f4 + \
           fodder5.price[day] * f5 + check_macro_penalty(f1, f2, f3, f4, f5)


#print(daily_cost(1, 1, 1, 1, 1, 1))


# PSO - bedziemy minimalizowac ilosc kupionej karmy w kazdym dniu po kolei

def update_velocity(particle, velocity, pbest, gbest, w_min=0.5, w_max=1.0, c=0.9):
    # Initialise new velocity array
    num_particle = len(particle)
    new_velocity = np.array([0.0 for i in range(num_particle)])
    # Randomly generate r1, r2 and inertia weight from normal distribution
    r1 = random.uniform(0.1, w_max)
    r2 = random.uniform(0.1, w_max)
    w = random.uniform(w_min, 0.1)
    c1 = c
    c2 = c
    # Calculate new velocity
    for i in range(num_particle):
        new_velocity[i] = w * velocity[i] + c1 * r1 * (pbest[i] - particle[i]) + c2 * r2 * (gbest[i] - particle[i])
    return new_velocity


def update_position(particle, velocity):
    # Move particles by adding velocity
    new_particle = (particle + velocity)
    return new_particle


# population - ilosc cząstek
# dimension - wymiar problemu tutaj 5
# position_min, position_max - pozycja startowa cząsteczek
# generation - liczba updateów
def pso(population, dimension, position_min, position_max, generation, fitness_criterion, random_solution):
    day = 1
    solution = []
    for i in range(len(random_solution)):
        particles = [[random.randint(position_min, position_max) for j in range(dimension)] for w in
                     range(population)]
        # Particle's best position
        pbest_position = particles
        # Fitness
        pbest_fitness = [daily_cost(p[0], p[1], p[2], p[3], p[4], day) for p in particles]
        # Index of the best particle
        gbest_index = np.argmin(pbest_fitness)
        # Global best particle position
        gbest_position = pbest_position[gbest_index]
        # Velocity (starting from 0 speed)
        velocity = [[0 for j in range(dimension)] for i in range(population)]
        # Loop for the number of generation
        for t in range(generation):
            # Stop if the average fitness value reached a predefined success criterion
            if np.average(pbest_fitness) <= fitness_criterion:
                break
            else:
                for n in range(population):
                    # Update the velocity of each particle
                    velocity[n] = update_velocity(particles[n], velocity[n], pbest_position[n], gbest_position)
                    # Move the particles to new position
                    particles[n] = update_position(particles[n], velocity[n])
            # Calculate the fitness value
            pbest_fitness = [daily_cost(p[0], p[1], p[2], p[3], p[4], day) for p in particles]
            # Find the index of the best particle
            gbest_index = np.argmin(pbest_fitness)
            # Update the position of the best particle
            gbest_position = pbest_position[gbest_index]
        ceil_particles = (np.ceil(particles)).astype(int)
        # print(ceil_particles[-1])  # ostateczne rozwiazanie (ilosc karmy zakupionej w danych dniach)
        solution.append(ceil_particles[-1])
        day += 1
    return solution




total_cost += check_penalty(random_solution)
#print(total_cost)

#pso(20, 5, 10, 80, 200, 0.001, random_solution)
