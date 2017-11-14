# -*- coding: utf-8 -*-

import json

from flask import Flask, request, render_template, jsonify

from apis import api_distancia_google

from produtos import Produtos
from lojas import Lojas


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
def view_home():
    return render_template("view_home.html"), 200


@app.route('/view/lojas/')
def view_lojas():
    return render_template("view_lojas.html"), 200


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
            ret['message'] = 'Erro ao atualizar produto'
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





@app.route('/Stores/', methods=['GET', 'POST', 'PUT'])
def stores():

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
        loja = Lojas()
        ret = loja.select_all()
        return jsonify(ret), 200


    if request.method == 'POST':
        descricao = dataDict['descricao']
        cep = dataDict['cep']

        loja = Lojas()
        insert_ok = loja.inserir(descricao, cep)

        if insert_ok is True:
            ret['success'] = True
            ret['message'] = 'Loja inserida com sucesso'
            ret['id'] = loja.Id

            return jsonify(ret), 200
        else:
            ret['message'] = 'Erro ao inserir loja'
            return jsonify(ret), 400

    if request.method == 'PUT':
        loja_id = dataDict['id'] 
        descricao = dataDict['descricao']
        cep = dataDict['cep']

        loja = Lojas()
        update_ok = loja.atualizar(loja_id, descricao, cep)

        if update_ok is True:
            ret['success'] = True
            ret['message'] = 'Loja atualizada com sucesso'
            return jsonify(ret), 200
        else:
            ret['message'] = 'Erro ao atualizar loja'
            return jsonify(ret), 400

    return jsonify(ret), 405



@app.route('/Stores/Delete/<id>/', methods=['DELETE'])
def stores_delete_id(id):

    ret = { 'success' : False }

    loja = Lojas()
    delete_ok = loja.deletar(id)

    if delete_ok is True:
        ret['success'] = True
        ret['message'] = 'Loja excluida com sucesso'
        return jsonify(ret), 200
    else:
        ret['message'] = 'Erro ao excluir loja'
        return jsonify(ret), 400


    return jsonify(ret), 405




app.run()
