from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! Dit is de tweede versie</p>"

@app.route("/andereurl")
def hello_world2():
    return "<p>Hello, World2!</p>"