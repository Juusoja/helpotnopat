import json
""" YOUR CODE HERE """

class Ai(object):

    """ This module is an AI used to make decision in the game.
	The only required interfaces are set info and get action.

    """

    def __init__(self, name):
        """Return an AI object whose name is *name*.
	"""
        self.name = name
	self.game_state = ""

	""" YOUR CODE HERE """

    def get_action(self, state):
        """Use this method to give the game state to the AI
        """
	try :
            self.game_state = json.loads(state)
	except ValueError:
	    return 1

        """Use this method to get action base on the given game info.
        """

	""" Options to return:
		1) Raise: return an integer with first number denoting the number
			of dices, the second their face.
			Example: 24 -> "There are atleast two fours"
		2) Doubt: return 0
		3) Exact: return 1


	""" YOUR CODE HERE """

        return 0
