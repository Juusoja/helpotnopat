class Player:
    def __init__(self, name, dice, dice_count):
        self.name = name
        self.dice_count = dice_count
        self.dice = dice
        self.hand = []

    def get_hand(self):
        return self.hand

    def get_name(self):
        return self.name

    def lose_round(self):
        self.dice_count -= 1

    def throw_dice(self):
        self.hand = self.dice.throw(self.dice_count)

    def get_dice_count(self):
        return self.dice_count
