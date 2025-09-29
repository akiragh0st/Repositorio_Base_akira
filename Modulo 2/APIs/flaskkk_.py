from flask import Flask

app = Flask(__name__)


@app.route('/')
def perfil():
    return '<h1> ABA DE PERFIL </h1>'

@app.route('/')
def home():
    return '<h1>Hello Flask</h>'

if __name__ == "__main__":
    app.run(debug=True)

