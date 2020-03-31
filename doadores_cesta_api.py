from flask import Blueprint, jsonify, request
from resources.Doador_Cesta_recources import DoadoresCesta, DoadorCesta, DoadorNaoExiste,IdJaExiste, ErroInserir
from infraestrutura.to_dict import to_dict, to_dict_list

doador_cesta_app = Blueprint('doador_cesta_app', __name__, template_folder='templates')


@doador_cesta_app.route('/doadoresCestas', methods=['GET'])
def listar():
    listar = DoadoresCesta.get(DoadoresCesta)
    return jsonify (listar)

@doador_cesta_app.route('/doadoresCestas/<int:id>', methods=['GET'])
def localizar(id):
    try:
        return jsonify(DoadorCesta.get(DoadorCesta,id)), 200
    except DoadorNaoExiste:
        return 'menssagem: O cargo não foi encontrado.', 404

@doador_cesta_app.route('/doadoresCestas', methods=['POST'])
def criar():
    try:
        criado = DoadoresCesta.post(DoadoresCesta)
        return jsonify (criado), 201
    except IdJaExiste:
        return  "mensagem:Id do cargo já existe", 500
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o cargo.", 500

@doador_cesta_app.route('/doadoresCestas/<int:id>', methods=['PUT'])
def atualizar(id):
    try:
        atualizado = DoadorCesta.put(DoadorCesta,id)
        return jsonify(atualizado), 201
    except IdJaExiste:
        return "mensagem:Id do cargo já existe", 500
    except ErroInserir:
        return "mensagem: Ocorreu um erro ao inserir o cargo.", 500



@doador_cesta_app.route('/doadoresCestas/<int:id>', methods=['DELETE'])
def remover(id):
    try:
        removido = DoadorCesta.delete(DoadorCesta,id)
        return jsonify(removido)
    except DoadorNaoExiste:
        return 'menssagem: cargo não encontrado.'

