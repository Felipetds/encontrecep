from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def teste(name):
    p1 = '00000000'
    if len(p1) == len(name):
        teste = 'corrreto'
        return teste
    else:
        teste = 'erro'
        return teste

@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = ''


    return render_template("homepage.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
