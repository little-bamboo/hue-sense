from flask import Flask, Response, render_template
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title='HueSLiS')

if __name__ == "__main__":
    app.run()
