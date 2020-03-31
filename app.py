from flask import Flask, jsonify
from flask_restful import Api
from doadores_api import doador_app
from doadores_cesta_api import doador_cesta_app
from donatarios_api import donatario_app


app = Flask(__name__)
app.register_blueprint(doador_app)
app.register_blueprint(doador_cesta_app)
app.register_blueprint(donatario_app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'segredo'
api = Api(app)




