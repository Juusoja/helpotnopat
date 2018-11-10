class Dice(object):

    """ This object implements the dice used in the game.
    It has only one function. It return the result of n dice throws.

    """

    def __init__(self):
        """Return a Dice object whose name is *name*.
	"""

    def throw(self, n):
        """Return the result of throwing n dice.
        """
        return [random.randint(1,6) for i in range(1,n+1)]

