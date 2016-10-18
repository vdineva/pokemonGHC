from pokestarter.starters import get_random_starter
import unittest


class TestPokemon(unittest.TestCase):

    def test_get_random_starters(self):
        starters = ["Charmander", "Squirtle", "Bulbasaur"]

        for i in range(0, 50):
            starter = get_random_starter()
            self.assertIn(starter, starters)

    def test_name_formatting(self):
        for i in range(0, 50):
            starter = get_random_starter()
            first_letter = starter[0]
            remaining_letters = starter[1:]
            self.assertTrue(first_letter.isupper())
            self.assertTrue(remaining_letters.islower())

    @unittest.skip("Skipping test for demonstration purposes")
    def test_skipped_test(self):
        pass
