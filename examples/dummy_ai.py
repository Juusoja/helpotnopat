import json
import random

class Ai(object):

    """ This module is an AI used to make decision in the game.
	The only required interfaces are set info and get action.

    """

    def __init__(self, name):

        """Return an AI object whose name is *name*.
	"""

        self.name = name
	self.game_state = ""

    def get_action(self, state):

	try :
            self.game_state = json.loads(state)
	    return 0
	except ValueError:
	    return 1

	self.hand = self.gamestate['hand']
	self.previous_call = self.gamestate['previous_call']
	self.players = len(self.gamestate['player_status'])
	self.dice_sum = self.dice_count()
	self.mininc = self.calculate_minimum_increment()

        """Use this method to get action base on the given game info.
        """

	""" Options to return:
		1) Raise: return an integer with first number denoting the number
			of dices, the second their face.
			Example: 24 -> "There are atleast two fours"
		2) Doubt: return 0
		3) Exact: return 1
	"""

	if (self.call_falsehood_probability() > 0.6):
	    return 0

        return self.compressed(self.mininc)

    def dice_count(self):

	sum = 0
	for i in range(self.players):
	    sum += self.gamestate['player_status'][i]['dice']
	return sum

    def call_falsehood_probability(self):

	return self.previous_call[0]*self.previous_call[1]/face_probability()*1.0

    def face_probabililty(self):

	return self.dice_sum/6.0

    def compressed(self, tobecomp):

	return 10*tobecomp[0]+tobecomp[1]

    def calculate_min_increment(self):

	self.placeholder = [0,0]

	if (self.previous_call[1] == 6):
	    self.placeholder[0] = self.previous_call[0] + 1
	    self.placeholder[1] = 1
	else:
	    self.placeholder[0] = self.previous_call[0]
	    self.placeholder[1] = self.previous_call[1] + 1

	return self.placeholder
