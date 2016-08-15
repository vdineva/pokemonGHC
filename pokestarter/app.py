from random import randint
from flask import Flask, jsonify, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", pokemon=get_random_starter())


@app.route('/api')
def starter_api():
    starter = get_random_starter()
    data = {
        "pokemon": starter
    }
    response = jsonify(data)
    response.status_code = 200
    return response


def get_random_starter():
    starters = ["Charmander", "Squirtle", "Bulbasaur", "Pikachu"]
    return starters[randint(0, len(starters)-1)]


if __name__ == "__main__":
    app.run(port=5000)
