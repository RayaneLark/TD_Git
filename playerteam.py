from team import Team

class PlayerTeam(Team):
    def __init__(self, nb_warriors, nb_hunters, nb_wizards, damage, loot, flee):
        super().__init__()
        self.__nb_warriors = nb_warriors
        self.__nb_hunters = nb_hunters
        self.__nb_wizards = nb_wizards
        self.__damage = damage
        self.__loot = loot
        self.__flee = flee

    def get_damage(self):
        return self.__damage

    def get_chance_value(self):
        return self.__loot

    def get_flee_value(self):
        return self.__flee

    def get_nb_warriors(self):
        return self.__nb_warriors

    def get_nb_hunters(self):
        return self.__nb_hunters

    def get_nb_wizards(self):
        return self.__nb_wizards

