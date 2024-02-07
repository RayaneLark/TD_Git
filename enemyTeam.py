from team import Team

class EnemyTeam(Team):
    def __init__(self, unit: str, damage: int, loot: int):
        super().__init__()
        self.__unit = unit  # Type d'unité (zombie, goblin, orc)
        self.__damage = damage  # Dégâts totaux de l'équipe
        self.__loot = loot  # Valeur de butin de l'équipe

    # Méthode pour accéder au type d'unité
    def get_unit_type(self) -> str:
        return self.__unit

    # Méthode pour accéder aux dégâts de l'équipe
    def get_damage(self) -> int:
        return self.__damage

    # Méthode pour accéder à la valeur de butin de l'équipe
    def get_loot(self) -> int:
        return self.__loot
