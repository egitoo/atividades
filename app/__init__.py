from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home():
    title = "Presunto viado"
    lista = ['curso do gordo bixa', 'curso do leitao baitola']
    return render_template('index.html', titulo=title, eventos=lista)


