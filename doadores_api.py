from flask import Blueprint, jsonify, request
from flask_login import login_required
from resources.Doador_Cadastro_resources import Doador, Doadores, DoadorNaoExiste,IdJaExiste, ErroInserir
from infraestrutura.to_dict import to_dict, to_dict_list


doador_app = Blueprint('doador_app', __name__, template_folder='templates')


@doador_app.route('/doadores', methods=['GET'])
def listar():
    listar = Doador.get(Doador)
    return jsonify (listar)

@doador_app.route('/doadores/<int:id>', methods=['GET'])
def localizar(id):
    try:
        return jsonify(Doadores.get(Doadores,id)), 200
    except DoadorNaoExiste:
        return 'menssagem: O cargo não foi encontrado.', 404
'''
@clientes_app.route('/clientes/<int:id>', methods=['GET'])
def localizar(id):
    verificaCliente = Cliente.get(Cliente,id)
    if verificaCliente == 0:
        return 'menssagem: Cliente não foi encontrado.', 404
    return jsonify(to_dict(Cliente.get(Cliente,id))), 200
'''

@doador_app.route('/doadores', methods=['POST'])
def criar():
    try:
        criado = Doador.post(Doador)
        return jsonify (criado), 201
    except IdJaExiste:
        return  "mensagem:Id do cargo já existe", 500
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o cargo.", 500

@doador_app.route('/doadores/<int:id>', methods=['PUT'])
def atualizar(id):
    try:
        atualizado = Doadores.put(Doadores,id)
        return jsonify(atualizado), 201
    except IdJaExiste:
        return "mensagem:Id do cargo já existe", 500
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o cargo.", 500



@doador_app.route('/doadores/<int:id>', methods=['DELETE'])
def remover(id):
    try:
        removido = Doadores.delete(Doadores,id)
        return jsonify(removido)
    except DoadorNaoExiste:
        return 'menssagem: cargo não encontrado.'


