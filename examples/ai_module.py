import json

class Ai(object):

    """ This module is an AI used to make decision in the game.
	The only required interfaces are set info and get action.

    """

    def __init__(self, name):
        """Return an AI object whose name is *name*.
	"""
        self.name = name
	self.game_state = ""

    def set_info(self, n):
        """Use this method to give the game state to the AI
        """
        return [random.randint(1,6) for i in range(1,n+1)]

    def get_action(self, n):
        """Use this method to get action base on the given game info.
        """
        return [random.randint(1,6) for i in range(1,n+1)]
