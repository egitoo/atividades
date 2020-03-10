from app import db
from app.models.tables import Atividade
from datetime import date

a1 = Atividade(nome='Oficina GIT', tipo='Oficina', data=date(2020,11,20), carga_horaria=8, arquivo='/1/348384.pdf', usuario_id=1)
a2 = Atividade(nome='Palestra BigDATA', tipo='Palestra', data=date(2020, 3, 10), carga_horaria=1, arquivo='/1/4749789.pdf', usuario_id=1)
a3 = Atividade(nome='Oficina Vue', tipo='Oficina', data=date(2020, 4, 15), carga_horaria=10, arquivo='/1/4324.pdf', usuario_id=1)

db.session.add(a1)
db.session.add(a2)
db.session.add(a3)

db.session.commit()
