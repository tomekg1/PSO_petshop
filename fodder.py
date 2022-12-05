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

    