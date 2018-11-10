from dice import Dice
from player import Player
from random import shuffle
from random import choice

class GameSession:
    def __init__(self, ids, dice_count):
        self.players = []
        dice = Dice("Sami lupas tuoda nopat")

        # Create list of player objects
        for id in ids:
            new_player = Player(id, dice, dice_count)
            self.players.append(new_player)
        shuffle(self.players)
        self.round_count = 0

    def run(self):
        while (len(self.players) > 1):
            self.round_count += 1
            print("Round " + str(self.round_count))
            self.throw_dice()

            # Random player loses the round
            loser = choice(self.players)
            loser.lose_round()
            print("The loser of the round was " + loser.get_name())

            # Player is removed from the list, if he runs out of dice.
            if loser.get_dice_count() == 0:
                print("Player " + loser.get_name() + " lost the game.")
                self.players.remove(loser)
        print("The winner of the game is " +  self.players[0].get_name())

    def throw_dice(self):
        for player in self.players:
            player.throw_dice()
