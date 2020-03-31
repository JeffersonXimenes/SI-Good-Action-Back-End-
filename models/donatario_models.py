from infraestrutura.sql_alchemy import db
from infraestrutura.validacoes import getData

class Donatario(db.Model):
    __tablename__ = 'Donatario'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    razao_social = db.Column(db.String(200), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    agencia = db.Column(db.String(4), nullable=False)
    conta = db.Column(db.String(5), nullable=False)
    dv = db.Column(db.String(1), nullable=False)
    segmento = db.Column(db.String(20))
    codigo_banco = db.Column(db.String(5), nullable=False)
    endereco = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.Integer)
    bairro = db.Column(db.String(50), nullable=False)
    municipio = db.Column(db.String(50), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    complemento = db.Column(db.String(50))
    cep = db.Column(db.String(8), nullable=False)

    def __init__(self, id, razao_social, cnpj, agencia, conta, dv, segmento,codigo_banco,endereco,numero,bairro,municipio,uf,complemento,cep):
        self.id = id
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.agencia = agencia
        self.conta = conta
        self.dv = dv
        self.segmento = segmento
        self.codigo_banco = codigo_banco
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.municipio = municipio
        self.uf = uf
        self.complemento = complemento
        self.cep = cep

    def json(self):
        return {
            "razao_social": self.razao_social,
            "cnpj": self.cnpj,
            "agencia": self.agencia,
            "conta":self.conta,
            "dv": self.dv,
            "segmento": self.segmento,
            "codigo_banco": self.codigo_banco,
            "endereco": self.endereco,
            "numero": self.numero,
            "bairro": self.bairro,
            "municipio": self.municipio,
            "uf": self.uf,
            "complemento": self.complemento,
            "cep": self.cep
        }

    @classmethod
    def find_Donatario(cls, id):
        doador = cls.query.filter_by(id=id).first()
        if doador:
            return doador
        return None
    @classmethod
    def find_ID(cls, cnpj):
        cpf = cls.query.filter_by(cnpj=cnpj).first()
        if cpf:
            return cpf.id
        return None

    def save_donatario(self):
        db.session.add(self)
        db.session.commit()

    def update_donatario(self, razao_social, cnpj, agencia, conta, dv, segmento,codigo_banco,endereco,numero,bairro,municipio,uf,complemento,cep):
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.agencia = agencia
        self.conta = conta
        self.dv = dv
        self.segmento = segmento
        self.codigo_banco = codigo_banco
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.municipio = municipio
        self.uf = uf
        self.complemento = complemento
        self.cep = cep

    def delete_donatario(self):
        db.session.delete(self)
        db.session.commit()
