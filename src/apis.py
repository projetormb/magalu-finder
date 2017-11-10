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

#INSERT INTO `mbcorporate01`.`Produtos` (`Descricao`, `ValorVenda`) VALUES ("TV Samsung 40 polegadas", 2299.99)

#INSERT INTO `mbcorporate01`.`Lojas` (`Descricao`, `CEP`) VALUES ('Loja Franca Centro', 14401216);
#INSERT INTO `mbcorporate01`.`Lojas` (`Descricao`, `CEP`) VALUES ('Loja Franca Estacao', 14405086);
#INSERT INTO `mbcorporate01`.`Lojas` (`Descricao`, `CEP`) VALUES ('Loja RP Ipiranga', 14055537);



#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 1, 1);
#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 2, 7);
#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 3, 13);




app.run()
