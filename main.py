import pandas as pd
import numpy as np
import lib
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # create random solution 30 x 5
    # run PSO
    #
    random_solution = lib.create_random_solution()
    random_cost = lib.compute_total_cost(random_solution)
    print('\n------WYGENEROWANE ROZWIAZANIE POCZATKOWE------')
    print(random_solution)


    generation = 50
    solution, day_particle_change = lib.pso(20, 5, 10, 80, generation, 0.001, random_solution, hamming=1)
    print('\n------ROZWIAZANIE DLA 1 CZASTECZKI------')
    print(solution)

    print('\n------ZMIANA KOSZTOW W KOLEJNYCH ITERACJACH------')
    print(random_cost)
    # wyświetlenie kolejnych kosztów
    cost_changes = [random_cost]
    for gen in range(len(day_particle_change[0])):
        sort_iter = []
        for day in range(len(day_particle_change)):
            sort_iter.append(day_particle_change[day][gen])
        cost_changes.append(int(lib.compute_total_cost(sort_iter)))
        print(int(lib.compute_total_cost(sort_iter)))

    plt.plot(cost_changes, 'k.')
    plt.xlabel('Iterations')
    plt.ylabel('Total cost')
    plt.grid()
    plt.show()






