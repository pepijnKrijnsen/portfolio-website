from bottle import Bottle, run, static_file
import os

parent = os.path.dirname(os.path.abspath(__file__))
parent += "/website"

print(parent)

app = Bottle()

@app.route("/")
def serve_home():
    parent = os.path.dirname(os.path.abspath(__file__))
    parent += "/website"
    return static_file("index.html", root = parent)

run(app, host = "localhost", port = 8080, debug = True)
