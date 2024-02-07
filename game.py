class Game:
    history_file = "game_history.txt"  # Attribut de classe pour le fichier d'historique
    __game_status = "not started"  # Attribut privé pour l'état de la partie

    @classmethod
    def config(cls):
        """Configure la partie et sauvegarde dans le fichier texte."""
        # Ici, vous configurerez la partie et sauvegarderez les configurations dans history_file
        cls.__game_status = "configured"
        with open(cls.history_file, "w") as file:
            file.write("Game configured\n")

    @classmethod
    def status(cls):
        """Affiche l'état courant de la partie."""
        print(f"Current game status: {cls.__game_status}")

    @classmethod
    def __load_player_team(cls):
        """Retourne une instance de PlayerTeam à partir du fichier texte."""
        # Lire le fichier et créer une instance de PlayerTeam basée sur le contenu
        return None  # Exemple simplifié

    @classmethod
    def __load_enemy_team(cls):
        """Retourne une instance de EnemyTeam à partir du fichier texte."""
        # Lire le fichier et créer une instance de EnemyTeam basée sur le contenu
        return None  # Exemple simplifié

    @classmethod
    def player_damage(cls):
        """Retourne la somme des dégâts des unités de l'équipe du joueur."""
        # Calculer et retourner la somme des dégâts
        return 0  # Exemple simplifié

    @classmethod
    def enemy_damage(cls):
        """Retourne la somme des dégâts des unités de l'équipe ennemie."""
        # Calculer et retourner la somme des dégâts
        return 0  # Exemple simplifié

    @classmethod
    def load_game(cls):
        """Charge l'état de la partie à partir du fichier texte."""
        # Lire le fichier et charger l'état de la partie
        cls.__game_status = "loaded"
        print("Game loaded from file")

    @classmethod
    def start_game(cls):
        """Redémarre la partie en écrasant les données du fichier texte."""
        cls.__game_status = "started"
        # Écraser les données du fichier pour démarrer une nouvelle partie
        with open(cls.history_file, "w") as file:
            file.write("Game started\n")

    @classmethod
    def buy(cls, unit):
        """Achète l'unité choisie et met à jour les données du fichier texte."""
        # Mettre à jour le fichier avec l'unité achetée
        with open(cls.history_file, "a") as file:
            file.write(f"{unit} bought\n")

    @classmethod
    def move(cls):
        """Charge le fichier texte et calcule le résultat de l'action de mouvement."""
        # Lire le fichier, calculer le mouvement, et mettre à jour le fichier
        print("Movement action processed")

    @classmethod
    def fight(cls):
        """Simule le combat et met à jour le fichier texte."""
        # Lire le fichier, simuler le combat, et mettre à jour le fichier
        print("Fight action processed")

    @classmethod
    def flee(cls):
        """Simule la fuite et met à jour le fichier texte."""
        # Lire le fichier, simuler la fuite, et mettre à jour le fichier
        print("Flee action processed")
