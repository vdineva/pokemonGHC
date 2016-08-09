import pykemon

def get_pokemon_details(pokemon_name):
    client = pykemon.V1Client()
    pokemon = pykemon.get(pokemon=pokemon_name)
    return pokemon
