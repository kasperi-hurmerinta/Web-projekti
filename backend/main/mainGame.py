import sys
import os
from flask import Flask, render_template
from functions.newGame import new_game

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

if src_path not in sys.path:
    sys.path.insert(0, src_path)

app = Flask(__name__, template_folder=src_path)

@app.route("/etusivu")
def etusivu():
    return render_template("index.html")

@app.route("/uusi-peli", methods=["POST"])
def uusi_peli():
    new_game()

    return render_template("uusi_peli.html")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)