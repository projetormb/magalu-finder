# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, jsonify

from apis import api_distancia_google


app = Flask(__name__, template_folder='./templates', static_url_path='/static')


@app.route('/')
def home():
    return render_template("principal.html"), 200


@app.route('/lojas/')
def view_lojas():
    return render_template("lojas.html"), 200


@app.route('/produtos/')
def view_produtos():
    return render_template("produtos.html"), 200


@app.route('/pesquisar/')
def view_pesquisar():
    produtos = []
    produtos.append({ 'ID' : '1', 'Nome' : u'TV Samsung LED 40 polegadas'})
    produtos.append({ 'ID' : '2', 'Nome' : u'Aspirador de Pó Arno'})
    produtos.append({ 'ID' : '3', 'Nome' : u'Celular Moto G'})
    return render_template("pesquisar.html", produtos=produtos), 200


@app.route('/distancia/')
def distancia():

    invalid_parameters = { 'success' : False }

    if len(request.args) == 0:
        invalid_parameters['error'] = 'Parâmetros cep_origem e cep_destino não foram informados'
        return jsonify(invalid_parameters), 400

    if 'cep_origem' not in request.args:
        invalid_parameters['error'] = 'Parâmetro cep_origem não foi informado'
        return jsonify(invalid_parameters), 400

    if 'cep_destino' not in request.args:
        invalid_parameters['error'] = 'Parâmetro cep_destino não foi informado'
        return jsonify(invalid_parameters), 400


    cep_origem = request.args['cep_origem']
    cep_destino = request.args['cep_destino']

    ret = api_distancia_google(cep_origem, cep_destino)

    if ret['success'] is True:
        return jsonify(ret), 200

    return jsonify(ret), 400 


app.run()
