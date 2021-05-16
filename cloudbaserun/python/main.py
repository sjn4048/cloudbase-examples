import os

from flask import Flask

app = Flask(__name__)


@app.route('answer_to_the_ultimate_question_of_life_the_universe_and_everything')
def deep_thought_the_enormous_supercomputer():
    return '<h1>42</h1>'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)