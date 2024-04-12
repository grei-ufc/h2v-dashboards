# Host on a route of existing Flask app
# Nesse exemplo, os dois aplicativos rodam no mesmo servidor, mas não coexistem na mesma rota.

from dash import Dash, html
from flask import Flask

server = Flask(__name__)

@server.route("/")
def home():
    return "Hello, Flask!"

app = Dash(__name__, server=server, routes_pathname_prefix="/dash/")

app.layout = html.Div("This is the Dash app.")

if __name__ == "__main__":
    app.run_server(debug=True)