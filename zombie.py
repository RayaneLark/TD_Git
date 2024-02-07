import random

class Zombie:
    def __init__(self):
        self.degat = random.uniform(1, 2)  # Définit les dégâts aléatoires entre 1 et 2
        self.loot = random.uniform(0.5, 1)  # Définit le butin aléatoire entre 0.5 et 1


