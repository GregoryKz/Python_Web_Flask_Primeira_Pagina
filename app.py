from flask import Flask
from flask import render_template
from flask import request
app= Flask (__name__)
#rota principal
@app.route("/")
def home():
    return render_template(
        "index.html",
        texto="O seu último dia fácil foi HOJE!!!!!",
        paragrafo="Meu parágrafo é esse aqui",
        h2="Meu H2 é esse aqui",
        H3python = "Teste do hg3"
    )

@app.route("/processar", methods=["POST"])
def processar():
    nome = request.form["nome"]
    idade = request.form["idade"]
    mensagem = f"Olá {nome}, você tem {idade} anos"
    return render_template("index.html", resultadoForm = mensagem)


if __name__ == '__main__':
    app.run(debug=True)

    