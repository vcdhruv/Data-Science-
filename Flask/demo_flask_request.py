from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello1():
    return "Hello 1"

@app.route("/input")
def input():
    data = request.args.get("x")
    return "{} this is the value".format(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
