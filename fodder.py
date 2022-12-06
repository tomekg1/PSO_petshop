class Fodder:
    def __init__(self, protein: int, fat: int, carbohydrates: int, price: dict):
        self.protein = protein
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.price = price


class Animal:
    def __init__(self, number: int, protein_need: int, fat_need: int, carbohydrates_need: int):
        self.number = number
        self.protein_need = protein_need * number
        self.fat_need = fat_need * number
        self.carbohydrates_need = carbohydrates_need * number


# ilość miejsca w magazynie
class Warehouse:
    def __init__(self, space: float, fodder1_space: float, fodder2_space: float, fodder3_space: float):
        self.space = space
        self.fodder1_space = fodder1_space
        self.fodder2_space = fodder2_space
        self.fodder3_space = fodder3_space

    def compute_space_used(self):
        space_used = self.fodder1_space + self.fodder2_space + self.fodder3_space
        return space_used

    def compute_space_free(self):
        space_free = self.space - self.space_used
        return space_free


# koszt przechowywania
class StorageCost:
    def __init__(self, cost: float, days: int, day_cost: int):
        self.cost = cost
        self.days = days
        self.day_cost = day_cost

    def compute_storage_cost(self):
        cost = self.day_cost * self.days
        return cost


# ilość kupionej karmy
class FodderPurchaseAmount:
    def __int__(self, fodder1_amount: int, fodder2_amount: int, fodder3_amount):
        self.fodder1_amount = fodder1_amount
        self.fodder2_amount = fodder2_amount
        self.fodder3_amount = fodder3_amount


# koszt kupienia karmy
class FodderPurchaseCost:
    def __int__(self, fodder1_cost: float, fodder2_cost: float, fodder3_cost: float):
        self.fodder1_cost = fodder1_cost
        self.fodder2_cost = fodder2_cost
        self.fodder3_cost = fodder3_cost

    def compute_fodder_purchase_cost(self):
        purchase_cost = self.fodder1_cost * self.fodder1_amount + self.fodder2_cost * self.fodder2_amount + self.fodder3_cost * self.fodder3_amount
        return purchase_cost
