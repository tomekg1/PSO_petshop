from fodder import *
import pandas as pd
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

# rodzaje karmy
fodder1 = Fodder(protein=15, fat=10, carbohydrates=30, price=price1)
fodder2 = Fodder(protein=40, fat=20, carbohydrates=15, price=price2)
fodder3 = Fodder(protein=25, fat=45, carbohydrates=20, price=price3)

# pojemność magazynu do składowania karmy, ogólna pojemność to 30kg i następnie po 10kg na rodzaj karmy
space = Warehouse(space=30, fodder1_space=10, fodder2_space=10, fodder3_space=10)

# minimalne makroskladniki potrzebne ndziennie

macro_need_per_day = 0
for i in animals:
    macro_need_per_day = np.add(macro_need_per_day, i.get_macro_need())

# funkcja celu
# wszystkie możliwości, żeby x * f1 + y * f2 + z * f3 >= macro_need_per_day

def f_c(f1, f2, f3, day):
    return f1.price[day], f2.price[day],  f3.price[day]





