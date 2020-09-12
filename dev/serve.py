from bottle import Bottle, run, static_file
import os

parent = os.path.dirname(os.path.abspath(__file__))
parent += "/website"

app = Bottle()

@app.route("/")
def serve_home():
    return static_file("index.html", root = parent)

@app.route("<filename:re:.*\.css>")
def css(filename):
    return static_file(filename, root = parent)

@app.route("<filename:re:.*\.html>")
def static_html(filename):
    return static_file(filename, root = parent)

run(app, host = "localhost", port = 8080, debug = True)
