from infraestrutura.sql_alchemy import db

class Doador_Cesta(db.Model):
    __tablename__ = 'Doador_Cesta'

    id_doador_cesta = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    celular = db.Column(db.String(20))

    def __init__(self, id_doador_cesta, nome, cpf, email, celular):
        self.id_doador_cesta = id_doador_cesta
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.celular = celular

    def json(self):
        return {
            "id_doador_cesta": self.id_doador_cesta,
            "nome": self.nome,
            "cpf": self.cpf,
            "email": self.email,
            "celular": self.celular
            
        }

    @classmethod
    def find_doador_cesta(cls, id_doador_cesta):
        doadorCesta = cls.query.filter_by(id_doador_cesta=id_doador_cesta).first()
        if doadorCesta:
            return doadorCesta
        return None
    
    def save_doador_cesta(self):
        db.session.add(self)
        db.session.commit()


    def update_doador_cesta(self, nome, cpf, email, celular):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.celular = celular


    def delete_doador_cesta(self):
        db.session.delete(self)
        db.session.commit()