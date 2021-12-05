import datetime
import random

from flask import Flask, render_template

app = Flask(__name__)


now = datetime.datetime.now()


@app.route('/about')
def get_info():

    aboutInfo = "Roman Krentovskyi. KND-22"
    beginning = "<html><body><h1>"
    ending = "</h1></body></html>"
    return beginning + aboutInfo + ending


@app.route('/time')
def get_time():

    timestring = now.strftime("%d-%m-%Y %H:%M")
    return render_template("time.html", timestring=timestring)


@app.route("/random")
def pick_number():
    n = int(random.uniform(1, 10))
    return render_template("random.html", number=n)


@app.route('/')
def index():
    return 'Hello World'


if __name__ == "__main__":
    app.run()
