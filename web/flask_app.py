from flask import Flask, Response, render_template, request, jsonify
import os

app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def index():
    return render_template("index.html", title='HueSLiS')

@app.route("/_toggle_soundcapture")
def toggle_soundcapture():
    return jsonify({'stream':'on/off'})



@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


if __name__ == "__main__":
    app.run()
