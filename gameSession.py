from dice import Dice
from player import Player
from random import shuffle
from random import choice

class GameSession:
    def __init__(self, ids, dice_count):
        self.players = []
        self.latest_count = 0
        self.latest_face = 0
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

            while True:
                active_player = players[1]
                action = active_player.get_action()
                losers = self.handle_action(action)
            # Random player loses the round
            loser = choice(self.players)
            loser.lose_round()
            print("The loser of the round was " + loser.get_name())

            # Player is removed from the list, if he runs out of dice.
            if loser.get_dice_count() == 0:
                print("Player " + loser.get_name() + " lost the game.")
                self.players.remove(loser)
        print("The winner of the game is " +  self.players[0].get_name())

    def handle_action(self, player, action):
        # Player raises the bet
        if action > 0:
            raise_attempts = 1
            while not self.validate_raise(action):
                print("Invalid raise, try again")
                if raise_attempts > 2:
                    print(
                        "Maximum amount of invalid raises reached. Player " + player.get_name() + " has lost the game")
                    self.player_loses_the_game()
                    break
                action = player.get_action()
                raise_attempts += 1
            count, face = self.convert_action_to_count_and_face(action)
            self.latest_count = count
            self.latest_face = face
            return []
        # Player doubts
        elif action == 0:
            if self.compare_dice_count(self.latest_count, self.latest_face) > 0:
                self.previous_player_loses_round()
            else:
                return [player]
        # Player chooses same
        else:
            if self.compare_dice_count(self.latest_count, self.latest_face) == 0:
                # return all other players except the current player as losers
                return [self.players.copy().remove(player)]
            else:
                return [player]

    def throw_dice(self):
        for player in self.players:
            player.throw_dice()

    def count_dice_with_face(self, face):
        face_count = 0
        for player in self.players:
            face_count += player.count_dice_with_face(face)
        return face_count

    def compare_dice_count(self, count, face):
        face_count = self.count_dice_with_face(face)
        if face_count > count:
            return 1
        elif face_count == count:
            return 0
        else:
            return -1

    def convert_action_to_count_and_face(self, action):
        count = action % 10
        face = action / 10
        return count, face
