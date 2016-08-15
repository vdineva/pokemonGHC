from pokestarter.app import get_random_starter
import unittest

class TestPokemon(unittest.TestCase):

    def test_get_random_starters(self):
        starters = ["Charmander", "Squirtle", "Bulbasaur", "Pikachu"]
        starter = get_random_starter()
        self.assertIn(starter, starters)
