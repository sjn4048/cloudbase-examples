import os

from flask import Flask, send_file

app = Flask(__name__)


@app.route('/')
def deep_thought_the_enormous_super_computer():
    return send_file("42.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
