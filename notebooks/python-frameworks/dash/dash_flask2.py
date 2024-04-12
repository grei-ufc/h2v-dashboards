# DispatcherMiddleware

'''
Em resumo, este código cria uma aplicação Flask que hospeda dois aplicativos Dash em rotas diferentes,
permitindo que eles sejam acessados separadamente no navegador. Cada aplicativo Dash tem sua própria rota e layout definido,
e o Flask fornece uma rota principal com sua própria funcionalidade.
'''
from dash import Dash, html
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

server = Flask(__name__)

@server.route("/")
def home():
    return "Hello, Flask!"

app1 = Dash(requests_pathname_prefix="/app1/")
app1.layout = html.Div("Hello, Dash app 1!")

app2 = Dash(requests_pathname_prefix="/app2/")
app2.layout = html.Div("Hello, Dash app 2!")

application = DispatcherMiddleware(
    server,
    {"/app1": app1.server, "/app2": app2.server},
)

if __name__ == "__main__":
    run_simple("localhost", 8050, application)