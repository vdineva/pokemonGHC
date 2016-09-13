from flask import Flask, jsonify, render_template

from starters import get_random_starter

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


if __name__ == "__main__":
    app.run(port=5000)
