from flask import Flask, render_template, redirect, url_for, request, json
import datetime

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('home_page.html')

@app.route("/index")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
