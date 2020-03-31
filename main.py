from flask import render_template, request, redirect, url_for,jsonify, jsonify, make_response
from app import app


@app.before_first_request
def cria_banco():
    db.create_all()



if __name__ == '__main__':
    from infraestrutura.sql_alchemy import db
    db.init_app(app)
    app.run(host='localhost', port=5000)