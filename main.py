from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def homepage():
    return render_template("homepage.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
