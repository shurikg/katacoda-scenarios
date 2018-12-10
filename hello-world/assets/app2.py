import datetime
from flask import Flask, jsonify, render_template
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
        "alive": True,
        "timestamp": datetime.datetime.now()
    })

@app.route("/hi")
@app.route('/hi/<name>')
def hi(name=None):
    return render_template('hi.html', name=name)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
