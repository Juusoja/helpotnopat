import pkgutil
import modules
from gameSession import GameSession

class Game:
    def __init__(self, dice_count):
        self.playerIds = []
        self.dice_count = dice_count
        self.game_count = 0
        self.read_players()

    def read_players(self):
        self.playerIds = []
        package = modules
        for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
            self.playerIds.append(modname)

    def run(self):
        while self.playerIds:
            self.game_count += 1
            print("Game " + str(self.game_count))
            game_session = GameSession(self.playerIds, self.dice_count)
            game_session.run()
            self.read_players()
