# -*- coding: utf-8 -*-

import json

from flask import Flask, request, render_template, jsonify
from apis import api_distancia_google
from produtos import Produtos


app = Flask(__name__, template_folder='./templates', static_url_path='/static')

# trocar prefixos e sufixos do jinja para não confundir com o AngularJS.

jinja_options = app.jinja_options.copy()

jinja_options.update(dict(
    block_start_string='<%',
    block_end_string='%>',
    variable_start_string='%%',
    variable_end_string='%%',
    comment_start_string='<#',
    comment_end_string='#>'
))
app.jinja_options = jinja_options




@app.route('/')
def home():
    return render_template("principal.html"), 200


@app.route('/lojas/')
def view_lojas():
    return render_template("lojas.html"), 200


@app.route('/produtos/')
def view_produtos():
    return render_template("produtos.html"), 200


@app.route('/view/produtos/')
def view_produtos2():
    return render_template("view_produtos.html")













@app.route('/Products/', methods=['GET', 'POST', 'PUT'])
def products():

    ret = { 'success' : False }

    if request.method in ['POST', 'PUT']:
        if request.is_json is False:
            ret['message'] = 'Request não é um JSON'
            return jsonify(ret), 400

        dataDict = request.get_json()

        if dataDict is None:
            ret['message'] = 'JSON inválido'
            return jsonify(ret), 400

        if len(dataDict) == 0:
            ret['message'] = 'Nenhuma informação encontrada no JSON'
            return jsonify(ret), 400


    if request.method == 'GET':
        produto = Produtos()
        ret = produto.select_all()
        return jsonify(ret), 200


    if request.method == 'POST':
        descricao = dataDict['descricao']
        valor_venda = dataDict['venda']

        produto = Produtos()
        insert_ok = produto.inserir(descricao, valor_venda)

        if insert_ok is True:
            ret['success'] = True
            ret['message'] = 'Produto inserido com sucesso'
            ret['id'] = produto.Id

            return jsonify(ret), 200
        else:
            ret['message'] = 'Erro ao inserir produto'
            return jsonify(ret), 400

    if request.method == 'PUT':
        produto_id = dataDict['id'] 
        descricao = dataDict['descricao']
        valor_venda = dataDict['venda']

        produto = Produtos()
        update_ok = produto.atualizar(produto_id, descricao, valor_venda)

        if update_ok is True:
            ret['success'] = True
            ret['message'] = 'Produto atualizado com sucesso'
            return jsonify(ret), 200
        else:
            ret['message'] = 'Erro ao inserir produto'
            return jsonify(ret), 400

    return jsonify(ret), 405



@app.route('/Products/Delete/<id>/', methods=['DELETE'])
def products_delete_id(id):

    ret = { 'success' : False }

    produto = Produtos()
    delete_ok = produto.deletar(id)

    if delete_ok is True:
        ret['success'] = True
        ret['message'] = 'Produto excluido com sucesso'
        return jsonify(ret), 200
    else:
        ret['message'] = 'Erro ao excluir produto'
        return jsonify(ret), 400


    return jsonify(ret), 405





"""
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
"""


app.run()
