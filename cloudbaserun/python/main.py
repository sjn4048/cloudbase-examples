import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def deep_thought_the_enormous_supercomputer():
    return '42'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)