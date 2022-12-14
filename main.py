import pandas as pd
import numpy as np
import lib

if __name__ == '__main__':

    # create random solution 30 x 5
    # run PSO
    #
    random_solution = lib.create_random_solution()
    random_cost = lib.compute_total_cost(random_solution)
    print(random_solution)
    print(random_cost)

    solution = lib.pso(20, 5, 10, 80, 200, 0.001, random_solution)
    final_cost = lib.compute_total_cost(solution)
    print(solution)
    print(final_cost)

    pass
