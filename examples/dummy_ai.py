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

    def set_info(self, state):
        """Use this method to give the game state to the AI
        """
	try :
            self.game_state = json.loads(state)
	    return 0
	except ValueError:
	    return 1

	self.hand =
	self.previous_call =
	self.players = 
	

    def get_action(self, n):
        """Use this method to get action base on the given game info.
        """

	""" Options to return:
		1) Raise: return an integer with first number denoting the number
			of dices, the second their face.
			Example: 24 -> "There are atleast two fours"
		2) Doubt: return 0
		3) Exact: return 1
	"""

	

	if (previous action)

        return 0

    def get_dice_count(self):

	sum = 0
	for i in range(len(self.gamestate['player_status'])):
	    sum += self.gamestate['player_status'][i]['dice']
	return sum

