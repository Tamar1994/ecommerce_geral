from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def index():
    return "Home page"

@app.route("/cadastro")
def cadastro():
    return "Página de Cadastro"

@app.route("/login")
def login():
    return "Página para Login"

@app.route("/carrinho")
def carrinho():
    return "Página do carrinho"

@app.route("/departamento/<categoria>")
def categoriaPage(categoria):
    return render_template("teste.html", categoria=categoria)

@app.route("/produtos")
def produtos():
    lista = ["camiseta", "bermuda", "short", "oculosdesol", "microondas"]
    return render_template("produtos.html", produtos=lista)

@app.route("/produto/<idproduto>")
def pageProduto(idproduto):
    return render_template("produto.html", produto=idproduto)

app.run()