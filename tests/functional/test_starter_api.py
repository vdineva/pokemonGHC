import json
import os
import requests
import time
import unittest


class TestPokemon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = os.environ.get("TEST_URL") or "http://localhost:5000/api"

    def test_get_starter_api(self):
        for i in range(30):
            response = requests.get(self.url)
            self.assertEquals(response.status_code, 200)
            json_data = json.loads(response.content)

            starter = json_data.get("pokemon")
            self.assertIsNotNone(starter)

            starters = ["Charmander", "Squirtle", "Bulbasaur"]
            self.assertIn(starter, starters)
            time.sleep(.5)

    def test_invalid_method_starter_api(self):
        response = requests.post(self.url)
        self.assertEquals(response.status_code, 405)

        response = requests.delete(self.url)
        self.assertEquals(response.status_code, 405)

        response = requests.put(self.url)
        self.assertEquals(response.status_code, 405)

    @unittest.skip("Skipping test for demonstration purposes")
    def test_skipped_test(self):
        pass
