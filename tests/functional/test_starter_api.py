import json
import os
import requests
import unittest


class TestPokemon(unittest.TestCase):

    def test_get_starter_api(self):
        url = os.environ.get("TEST_URL") or "http://localhost:5000/api"
        response = requests.get(url)
        self.assertEquals(response.status_code, 200)
        json_data = json.loads(response.content)

        starter = json_data.get("pokemon")
        self.assertIsNotNone(starter)

        starters = ["Charmander", "Squirtle", "Bulbasaur"]
        self.assertIn(starter, starters)
