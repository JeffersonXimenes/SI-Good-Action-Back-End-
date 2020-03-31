from infraestrutura.sql_alchemy import db


class Doador_Cadastro(db.Model):
    __tablename__ = 'Doador_Cadastro'

    id_doador= db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    celular = db.Column(db.String(20),nullable=False)
    latitude = db.Column(db.String(100), nullable=False)
    longitude = db.Column(db.String(100), nullable=False)

    def __init__(self, id_doador, nome,cpf,email,celular,latitude,longitude):
        self.id_doador = id_doador
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.celular = celular
        self.latitude = latitude
        self.longitude = longitude



    def json(self):
        return {
            "id_doador": self.id_doador,
            "nome": self.nome,
            "cpf": self.cpf,
            "email":self.email,
            "celular":self.celular,
            "latitude":self.latitude,
            "longitude":self.longitude
        }

    @classmethod
    def find_doador(cls, id_doador):
        doador = cls.query.filter_by(id_doador=id_doador).first()
        if doador:
            return doador
        return None

    def save_doador(self):
        db.session.add(self)
        db.session.commit()

    def update_doador(self, nome,cpf,email,celular,latitude,longitude):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.celular = celular
        self.latitude = latitude
        self.longitude = longitude


    def delete_doador(self):
        db.session.delete(self)
        db.session.commit()



