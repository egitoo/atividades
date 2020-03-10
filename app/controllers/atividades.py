from app import app
from flask import render_template
from app.models.tables import Atividade


# Listando todas as atividades
@app.route('/atividades')
def listar_atividades():
    a = Atividade.query.all()
    for x in range(len(a)):
        a[x].data = a[x].data.strftime('%d/%m/%Y')
    return render_template("atividades_listar.html", atividades=a)
