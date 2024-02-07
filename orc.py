import random

class Orc:
    def __init__(self):
        self.degat = random.choice([3, 5])  # Génère un nombre aléatoire entre 3 et 5
        self.loot = random.uniform(2, 2.5)  # Génère un nombre à virgule flottante aléatoire entre 2 et 2.5

