
from flask import Flask, render_template, jsonify
from connect import record

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/browse")
def browse_entries():
    return render_template('browse.html')


@app.route('/browse/entries', methods=['GET'])
def get_tasks():
    return jsonify({'entries': record})


if __name__ == '__main__':
    app.run()
