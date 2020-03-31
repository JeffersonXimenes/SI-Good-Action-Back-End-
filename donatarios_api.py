from flask import Blueprint, jsonify, request, render_template

from infraestrutura.to_dict import to_dict, to_dict_list
from resources.Donatarios_resource import Donatarios, JaCadastrado, DoadorJaCadastrado, NaoEncontrado,Donatario_put, ErroInserir



donatario_app = Blueprint('donatario_app', __name__, template_folder='templates')


@donatario_app.route('/donatario', methods=['GET'])
def listar():
    data = Donatarios.get(Donatarios)
    return jsonify(data)


@donatario_app.route('/donatario/<int:id>', methods=['GET'])
def localizar(id):
    try:
        return jsonify(Donatarios.getId(Donatarios, id)), 200
    except JaCadastrado:
        return 'menssagem: Donatarios não foi encontrado.', 404
    except NaoEncontrado:
        return 'menssagem: Donatarios não foi encontrado.', 404


@donatario_app.route('/donatario', methods=['POST'])
def criar():
    dados = request.get_json()
    try:
        Donatarios.post(Donatarios)
        return ("Doador cadastrado com sucesso"), 202
    except DoadorJaCadastrado:
        return 'menssagem: Doador ja cadastrado.', 404
    except JaCadastrado:
        return 'menssagem: Erro ao inserir.', 404

@donatario_app.route('/donatario/<int:id>', methods=['DELETE'])
def remover(id):
    try:
        Donatarios.delete(Donatarios,id)
        return " removido ",  200
    except:
        return " erro " , 404

@donatario_app.route('/donatario/<int:id>', methods=['PUT'])
def atualizar(id):
    try:
        atualizado = Donatario_put.put(Donatario_put,id)
        return jsonify(atualizado), 201
    except DoadorJaCadastrado:
        return "mensagem:Id do cargo já existe", 500
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o cargo.", 500