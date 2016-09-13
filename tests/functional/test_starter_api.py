import json
import requests
import unittest

class TestPokemon(unittest.TestCase):

    def test_get_starter_api(self):
        response = requests.get("http://localhost:5000/api")
        self.assertEquals(response.status_code, 200)
        json_data = json.loads(response.content)

        starter = json_data.get("pokemon")
        self.assertIsNotNone(starter)

        starters = ["Charmander", "Squirtle", "Bulbasaur"]
        self.assertIn(starter, starters)
