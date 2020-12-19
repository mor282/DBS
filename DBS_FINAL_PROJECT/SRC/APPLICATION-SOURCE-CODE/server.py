from flask import Flask, render_template, redirect, url_for, request, json
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home_page.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
