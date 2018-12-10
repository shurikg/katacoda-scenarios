import datetime
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ping")
def pong():
    return "pong"

@app.route("/health")
def health():
    return jsonify({
        "alive": true,
        "timestamp": datetime.datetime.now()
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0")
