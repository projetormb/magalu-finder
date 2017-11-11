# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, jsonify

import requests

#from consumo import consumoTwitter

app = Flask(__name__, template_folder='./templates', static_url_path='/static')

@app.route('/')
def home():

    produtos = []
    produtos.append({ 'ID' : '1', 'Nome' : u'TV Samsung LED 40 polegadas'})
    produtos.append({ 'ID' : '2', 'Nome' : u'Aspirador de Pó Arno'})
    produtos.append({ 'ID' : '3', 'Nome' : u'Celular Moto G'})

    return render_template("pesquisar.html", produtos=produtos), 200

@app.route('/lojas/')
def lojas():
    dados = { 'Titulo' : u'Manutenção de Lojas'}

    return render_template("lojas.html", dados=dados), 200


@app.route('/teste/')
def teste():

    resp = requests.get('http://maps.googleapis.com/maps/api/distancematrix/json?origins=13201-031&destinations=14401-216&mode=CAR&language=PT&sensor=false')

    ret_json = resp.json()

    if 'status' in ret_json:

        if ret_json['status'] == 'OK':

            if 'rows' in ret_json:
                return str(ret_json['rows'])


            return str(ret_json)



        return j['status']





    




#@app.route('/api', methods=['POST'])
#def api():
#    maxTweets = int(request.form['maxTweets'])
#    userName = request.form['userName']
#    retorno = consumoTwitter(userName, maxTweets)
#    return jsonify(retorno)



#  https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyAN6xBKJz_4hP5BcLFSYQNQdF2D-GRDOJo&address=14401216

#  http://maps.googleapis.com/maps/api/distancematrix/json?origins=13201-031&destinations=14401-216&mode=CAR&language=PT&sensor=false

app.run()
