from flask_restful import Resource, reqparse
from models.Doador_Cadastro import Doador_Cadastro


class IdJaExiste (Exception):
    pass
class ErroInserir (Exception):
    pass
class DoadorNaoExiste (Exception):
    pass

class Doador(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('id_doador', type=int)
    atributos.add_argument('nome', type=str)
    atributos.add_argument('cpf', type=str)
    atributos.add_argument('email', type=str)
    atributos.add_argument('celular', type=str)
    atributos.add_argument('latitude', type=str)
    atributos.add_argument('longitude', type=str)


    def get(self):
        return {'Doadores': [doador.json() for doador in Doador_Cadastro.query.all()]} # SELECT * FROM clientes
    def post(self):
        dados = Doador.atributos.parse_args()
        id = dados['id_doador']
        if Doador_Cadastro.find_doador(id):
            raise IdJaExiste()
            #return {"menssagem": "Telefone id '{}' já existe.".format(id)}, 400 #Bad Request
        doador = Doador_Cadastro(**dados)
        try:
            doador.save_doador()
        except:
            raise ErroInserir()
        return doador.json()
                #return {"mensagem": "Ocorreu um erro ao inserir o telefone."}, 500 #Internal Server Error

class Doadores(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome', type=str)
    atributos.add_argument('cpf', type=str)
    atributos.add_argument('email', type=str)
    atributos.add_argument('celular', type=str)
    atributos.add_argument('latitude', type=str)
    atributos.add_argument('longitude', type=str)

    def get(self, id_doador):
        doador = Doador_Cadastro.find_doador(id_doador)
        if doador:
            return doador.json()
        raise DoadorNaoExiste()
        #return {'menssagem': 'Telefone não foi encontrado.'}, 404

    def put(self, id_doador):
        dados = Doadores.atributos.parse_args()
        doador = Doador_Cadastro(id_doador, **dados)
        doador_encontrado = Doador_Cadastro.find_doador(id_doador)

        try:
            if doador_encontrado:
                doador_encontrado.update_doador(**dados)
                doador_encontrado.save_doador()

                return doador_encontrado.json()
            doador.save_doador()
        except:
            raise ErroInserir()
            #return {"mensagem": "Ocorreu um erro ao inserir o telefone. Verique a integridade"}, 500 #Internal Server Error
        return doador.json()



    def delete(self, id_doador):
        doador = Doador_Cadastro.find_doador(id_doador)
        if doador:
            doador.delete_doador()
            return {'messagem': 'cargo deletado.'}
        raise DoadorNaoExiste()
        #return {'menssagem': 'telefone não encontrado.'}, 404
