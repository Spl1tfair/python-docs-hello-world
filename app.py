from flask import Flask # ПРИВЕТ, Я IVAN
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
