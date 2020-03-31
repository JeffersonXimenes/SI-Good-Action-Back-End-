from flask_restful import Resource, reqparse
from models.donatario_models import Donatario

class JaCadastrado(Exception):
    pass

class DoadorJaCadastrado(Exception):
    pass

class NaoEncontrado(Exception):
    pass
class ErroInserir(Exception):
    pass
class Donatarios(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('id', type=int)
    atributos.add_argument('razao_social', type=str)
    atributos.add_argument('cnpj', type=str)
    atributos.add_argument('agencia', type=str)
    atributos.add_argument('conta', type=str)
    atributos.add_argument('dv', type=str)
    atributos.add_argument('segmento', type=str)
    atributos.add_argument('codigo_banco', type=str)
    atributos.add_argument('endereco', type=str)
    atributos.add_argument('numero', type=str)
    atributos.add_argument('bairro', type=str)
    atributos.add_argument('municipio', type=str)
    atributos.add_argument('uf', type=str)
    atributos.add_argument('complemento', type=str)
    atributos.add_argument('cep', type=str)


    def getId(self, id):
        doador = Donatario.find_Donatario(id)
        if doador:
            return doador.json()
        raise NaoEncontrado()
    
    def get(self):
        return {'Donatarios': [Doadores.json() for Doadores in Donatario.query.all()]} # SELECT * FROM clientes
    
    def post(self):
        dados = Donatarios.atributos.parse_args()
        id = dados['id']
        if Donatario.find_Donatario(id):
            raise DoadorJaCadastrado()

        doador = Donatario(**dados)
        try:
            doador.save_donatario()
            return doador.json()
        except:
            raise JaCadastrado()



    def delete(self, id):
        doador = Donatario.find_Donatario(id)
        if doador:
            doador.delete_donatario()
            return {'messagem': 'Donatario deletado.'}
        return {'menssagem': 'Donatario não encontrado.'}

class Donatario_put(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('razao_social', type=str)
    atributos.add_argument('cnpj', type=str)
    atributos.add_argument('agencia', type=str)
    atributos.add_argument('conta', type=str)
    atributos.add_argument('dv', type=str)
    atributos.add_argument('segmento', type=str)
    atributos.add_argument('codigo_banco', type=str)
    atributos.add_argument('endereco', type=str)
    atributos.add_argument('numero', type=str)
    atributos.add_argument('bairro', type=str)
    atributos.add_argument('municipio', type=str)
    atributos.add_argument('uf', type=str)
    atributos.add_argument('complemento', type=str)
    atributos.add_argument('cep', type=str)



    def put(self, id_donatario):
        dados = Donatario_put.atributos.parse_args()
        doador = Donatario(id_donatario, **dados)
        doador_encontrado = Donatario.find_Donatario(id_donatario)

        try:
            if doador_encontrado:
                doador_encontrado.update_donatario(**dados)
                doador_encontrado.save_donatario()

                return doador_encontrado.json()
            doador.save_donatario()
        except:
            raise ErroInserir()
        return doador.json()
