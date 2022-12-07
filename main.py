import pandas as pd
import numpy as np

import lib

if __name__ == '__main__':

    fc = []
    for day in range(1, 31):
        fc.append(lib.f_c(lib.fodder1, lib.fodder2, lib.fodder3, day))

    for i in fc:
        print(i)
