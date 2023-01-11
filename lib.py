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

# minimalne makroskladniki potrzebne dziennie

macro_need_per_day = 0
for i in animals:
    macro_need_per_day = np.add(macro_need_per_day, i.get_macro_need())

protein_need_per_day = macro_need_per_day[0]
fat_need_per_day = macro_need_per_day[1]
carbo_need_per_day = macro_need_per_day[2]


# tworzenie nowego rodzaju karmy
def create_new_fodder(protein, fat, carbo, p_min, p_max):
    price = {}
    for day in range(1, 31):
        price[day] = np.random.randint(p_min, p_max)
    fodd = Fodder(protein, fat, carbo, price)
    fodders.append(fodd)


# generowanie losowego rozwiązania
def create_random_solution(fodders):
    random_solution = []

    for i in range(1, 31):
        temp = []
        f_len = len(fodders)
        for f in fodders:
            fod = random.randint(f_len*6, f_len*12)
            temp.append(fod)
        random_solution.append(temp)

    return random_solution


# sprawdzanie czy w każdym dniu zapewniliśmy minimum zapotrzebowania - jeśli nie nakładamy karę do kosztu całkowitego
# gdy przepuścimy rozwiazanie niedopuszczalne to nakładamy bardzo dużą karę
def check_solution_penalty(solution):
    penalty_price = 1000
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


def cost_changes_format(random_cost, day_particle_change, generations):
    cost_changes = [random_cost]
    for gen in range(len(day_particle_change[0])):
        sort_iter = []
        for day in range(len(day_particle_change)):
            sort_iter.append(day_particle_change[day][gen])
        cost_changes.append(int(lib.compute_total_cost(sort_iter)))
    for idx, elem in enumerate(cost_changes):
        if elem > cost_changes[0]:
            cost_changes[idx] = cost_changes[0] + elem / generations * 20
    return cost_changes
#def compute_cost_changes()


# obliczenie całkowitego kosztu na bazie rozwiazania
def compute_total_cost(solution):
    total_cost = 0
    penalty = check_solution_penalty(solution)
    for eidx, elem in enumerate(solution):
        daily_cost = 0
        day = eidx + 1
        for inx, fodder in enumerate(elem):
            daily_cost += fodders[inx].price[day] * fodder
        total_cost += daily_cost
    return total_cost + penalty


# kara za jeden dzien
def check_macro_penalty(fodds):
    penalty_price = 100000

    protein = 0
    fat = 0
    carbo = 0
    for idx, fodd in enumerate(fodds):
        protein += fodders[idx].protein * fodds[idx]
        fat += fodders[idx].fat * fodds[idx]
        carbo += fodders[idx].carbohydrates * fodds[idx]

    if protein < protein_need_per_day:
        penalty_price *= 5
    if fat < fat_need_per_day:
        penalty_price *= 2
    if carbo < carbo_need_per_day:
        penalty_price *= 3
    if protein < protein_need_per_day or fat < fat_need_per_day or carbo < carbo_need_per_day:
        return penalty_price

    return 0


# funkcja celu dla kazdego dnia
def daily_cost(fodds, day):
    total_cost = 0
    for idx, fodd in enumerate(fodders):
        total_cost += fodd.price[day] * fodds[idx]
    total_cost += check_macro_penalty(fodds)
    return total_cost


# PSO - bedziemy minimalizowac ilosc kupionej karmy w kazdym dniu po kolei
def update_velocity(particle, velocity, pbest, gbest, w_min=0.5, w_max=1.0, c=1):
    # Initialise new velocity array
    num_particle = len(particle)
    new_velocity = np.array([0.0 for i in range(num_particle)])
    # Randomly generate r1, r2 and inertia weight from normal distribution
    r1 = random.uniform(0.1, w_max)
    r2 = random.uniform(0.1, w_max)
    # przy zmianie na 1 dostaje cos madrego
    w = 1
    c1 = c
    c2 = c
    # Calculate new velocity
    for i in range(num_particle):
        new_velocity[i] = w * velocity[i] + c1 * r1 * (pbest[i] - particle[i]) + c2 * r2 * (gbest[i] - particle[i])

    temp_new_particle = (particle + velocity)
    for idx, p in enumerate(temp_new_particle):
        if p < 0:
            x = random.uniform(0.1, 1.0)
            new_velocity[idx] = x
    return new_velocity


def update_position_hamming(particle, velocity, gbest_position):
    # Move particles by adding velocity
    new_particle = (particle + velocity)
    distance = [0, 0, 0, 0, 0]
    for i in range(len(new_particle)):
        if new_particle[i] != gbest_position[i]:
            distance[i] = np.abs(new_particle[i] - gbest_position[i])
    return new_particle, distance


def update_position(particle, velocity):
    # Move particles by adding velocity
    new_particle = (particle + velocity)
    for idx, np in enumerate(new_particle):
        if np < 0:
            new_particle[idx] = 0

    return new_particle


# population - ilosc cząstek
# dimension - wymiar problemu tutaj 5
# position_min, position_max - pozycja startowa cząsteczek
# generation - liczba updateów
def pso(population, fodds, position_min, position_max, generation, fitness_criterion, random_solution, hamming=0):
    day = 1
    solution = []
    dimension = len(fodds)
    # przechodzenie czastek w dniach
    day_particle_change = []
    for i in range(len(random_solution)):
        particles = [[random.randint(position_min, position_max) for j in range(dimension)] for w in
                     range(population)]
        particles[0] = random_solution[i]
        # Particle's best position - najlepsze polozenia czasteczek
        pbest_position = particles
        # Fitness - najlepszy koszt polozenia danej czasteczki
        pbest_fitness = [daily_cost(p, day) for p in particles]
        # Index of the best particle
        gbest_index = np.argmin(pbest_fitness)
        # Global best particle position
        gbest_position = pbest_position[gbest_index]
        # Velocity (starting from 0 speed)
        velocity = [[0 for j in range(dimension)] for i in range(population)]
        # Loop for the number of generation

        # przechodzenie czastek w iteracjach
        iter_particle = []
        for t in range(generation):
            # Stop if the average fitness value reached a predefined success criterion
            if np.average(pbest_fitness) <= fitness_criterion:
                iter_particle.append(particles[0])
                pass

            else:
                if hamming == 1:
                    dist_list = []
                    for n in range(population):
                        # Update the velocity of each particle
                        velocity[n] = update_velocity(particles[n], velocity[n], pbest_position[n], gbest_position)
                        # Move the particles to new position
                        particles[n], distance = update_position_hamming(particles[n], velocity[n], gbest_position)

                        dist_list.append(distance)

                    # indeks czasteczki o najmniejszym dystansie do gbest
                    min_dist_indx = 0
                    for n in range(population):
                        if sum(dist_list[n]) < min_dist_indx:
                            min_dist_indx = n

                    # Calculate the fitness value
                    pbest_fitness = [daily_cost(p, day) for p in particles]
                    # Find the index of the best particle
                    # gbest_index = np.argmin(pbest_fitness)
                    # Update the position of the best particle
                    gbest_position = particles[min_dist_indx]

                    # zapamietuje wszystkie ruchy czasteczki pochodzacej od rozwiazania losowego
                    iter_particle.append(particles[0])
                if hamming == 0:
                    for n in range(population):
                        # Update the velocity of each particle
                        velocity[n] = update_velocity(particles[n], velocity[n], pbest_position[n], gbest_position)
                        # Move the particles to new position
                        particles[n] = update_position(particles[n], velocity[n])
                        # Calculate the fitness value
                    pbest_fitness = [daily_cost(p, day) for p in particles]
                    # Find the index of the best particle
                    gbest_index = np.argmin(pbest_fitness)
                    # Update the position of the best particle
                    gbest_position = pbest_position[gbest_index]

                    # zapamietuje wszystkie ruchy czasteczki pochodzacej od rozwiazania losowego
                    iter_particle.append(particles[0])

        day_particle_change.append(iter_particle)
        ceil_particles = (np.ceil(particles)).astype(int)
        # print(ceil_particles[-1])  # ostateczne rozwiazanie (ilosc karmy zakupionej w danych dniach)
        solution.append(ceil_particles[-1])
        day += 1
    return solution, day_particle_change

