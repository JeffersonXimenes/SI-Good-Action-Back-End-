from flask_restful import Resource, reqparse
from models.doadorCesta_models import Doador_Cesta


class IdJaExiste (Exception):
    pass
class ErroInserir (Exception):
    pass
class DoadorNaoExiste (Exception):
    pass

class DoadoresCesta(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('id_doador_cesta', type=int)
    atributos.add_argument('nome', type=str)
    atributos.add_argument('cpf', type=str)
    atributos.add_argument('email', type=str)
    atributos.add_argument('celular', type=str)

    def get(self):
        return {'Doador_Cestas': [doadores_cestas.json() for doadores_cestas in Doador_Cesta.query.all()]} # SELECT * FROM clientes
    def post(self):
        dados = DoadoresCesta.atributos.parse_args()
        id = dados['id_doador_cesta']
        if Doador_Cesta.find_doador_cesta(id):
            raise IdJaExiste()
            #return {"menssagem": "Telefone id '{}' já existe.".format(id)}, 400 #Bad Request
        doador_cesta = Doador_Cesta(**dados)
        try:
            doador_cesta.save_doador_cesta()
        except:
            raise ErroInserir()
        return doador_cesta.json()


class DoadorCesta(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome', type=str)
    atributos.add_argument('cpf', type=str)
    atributos.add_argument('email', type=str)
    atributos.add_argument('celular', type=str)

    def get(self, id_doador_cesta):
        doador = Doador_Cesta.find_doador_cesta(id_doador_cesta)
        if doador:
            return doador.json()
        raise DoadorNaoExiste()


    def put(self, id_doador_cesta):
        dados = DoadorCesta.atributos.parse_args()
        doador = Doador_Cesta(id_doador_cesta, **dados)
        doador_encontrado = Doador_Cesta.find_doador_cesta(id_doador_cesta)

        try:
            if doador_encontrado:
                doador_encontrado.update_doador_cesta(**dados)
                doador_encontrado.save_doador_cesta()

                return doador_encontrado.json()
            doador.save_doador_cesta()
        except:
            raise ErroInserir()
        return doador.json()



    def delete(self, id_doador_cesta):
        doador = Doador_Cesta.find_doador_cesta(id_doador_cesta)
        if doador:
            doador.delete_doador_cesta()
            return {'messagem': 'Doador deletado.'}
        raise DoadorNaoExiste()
