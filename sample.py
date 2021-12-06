import datetime
from random import choice
from string import ascii_uppercase

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
    str = ''.join(choice(ascii_uppercase) for i in range(12))
    return render_template("random.html", str=str)


@app.route('/')
def index():
    return 'Hello World'


if __name__ == "__main__":
    app.run()
