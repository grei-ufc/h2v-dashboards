# Importando bibliotecas e funcionalidades
from flask import Flask, render_template

# Criando uma instância do aplicativo Flask
app = Flask(__name__)

app.static_folder = 'static'

# Definindo a rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rodando o aplicativo
if __name__ == '__main__':
    app.run(debug=True)