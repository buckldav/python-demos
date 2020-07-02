# server.py
from flask import Flask, render_template
import random

def get_hello():
  greeting_list = ['Ciao', 'Hei', 'Salut', 'Hola', 'Hallo', 'Hej']
  return random.choice(greeting_list)

app = Flask(__name__)

@app.route("/")
def index():
    return "<a href='/hello'>Hello</a>"

@app.route("/hello")
def hello():
    return get_hello()

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == "__main__":
    app.run()