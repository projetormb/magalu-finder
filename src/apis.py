# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, jsonify

#from consumo import consumoTwitter

app = Flask(__name__, template_folder='./templates', static_url_path='/static')

@app.route('/')
def home():

    produtos = []
    produtos.append({ 'ID' : '1', 'Nome' : u'TV Samsung LED 40 polegadas'})
    produtos.append({ 'ID' : '2', 'Nome' : u'Aspirador de Pó Arno'})
    produtos.append({ 'ID' : '3', 'Nome' : u'Celular Moto G'})

    return render_template("pesquisar.html", produtos=produtos), 200

#@app.route('/api', methods=['POST'])
#def api():
#    maxTweets = int(request.form['maxTweets'])
#    userName = request.form['userName']
#    retorno = consumoTwitter(userName, maxTweets)
#    return jsonify(retorno)

app.run()
