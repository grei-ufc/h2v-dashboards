# Nesse exemplo, os dois aplicativos rodam no mesmo servidor e o aplicativo Dash está embutido no HTML do app Flask.

from dash import Dash, html
from flask import Flask, render_template

server = Flask(__name__)

@server.route("/")
def home():
    return render_template('index.html')

app = Dash(__name__, server=server, routes_pathname_prefix="/dash/")

app.layout = html.Div("This is the Dash app.")

if __name__ == "__main__":
    app.run_server(debug=True)