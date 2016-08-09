from get_pykemon import get_pokemon_details

import unittest

class TestPokemon(unittest.TestCase):

    def test_pikachu(self):
        poke_details = get_pokemon_details('pikachu')
        self.assertEqual(poke_details.id, 25)
        self.assertEqual(poke_details.name, 'Pikachu')

    def test_Pikachu(self):
        poke_details = get_pokemon_details('Pikachu')

    def test_sabeen(self):
        poke_details = get_pokemon_details('sabeen')

if __name__ == '__main__':
    unittest.main()
