## Class Hierarchies
# Task 2 (Game Museum)


class ComputerGame:
    def __init__(self, game, name, year):
        self.game = game
        self.name = name
        self.year = year


class GameWarehouse:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def list_games(self):
        return list(self.games)


class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def list_games(self):
        old_games = []
        for game in self.games:
            if game.year < 1990:
                old_games.append(game)
        return old_games


museum = GameMuseum()
museum.add_game(ComputerGame("Pacman", "Namco", 1980))
museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))
for game in museum.list_games():
    print(game.name)
