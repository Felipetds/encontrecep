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

    name = str(name)

    if teste(name) == 'corrreto':
        link = f"https://cep.awesomeapi.com.br/json/{str(name)}"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        if 404 in dic_requisicao.values():
            name = "Informe um cep valido!"
            return render_template("homepage.html", name=name)
        elif 400 in dic_requisicao.values():
            name = "Informe um cep valido!"
            return render_template("homepage.html", name=name)
        else:
            um = dic_requisicao["address"]
            dois = dic_requisicao["district"]
            tres = dic_requisicao["city"]
            a = (str(um) + ', ' + str(dois) + ', ' + str(tres))
            name = f"{a}"
            return render_template("homepage.html", name=name)
    else:
        name = "Informe um cep valido!"
        return render_template("homepage.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
