from random import randint


def get_random_starter():
    starters = ["Charmander", "Squirtle", "Bulbasaur", "Pikachu"]
    return starters[randint(0, len(starters)-1)]
