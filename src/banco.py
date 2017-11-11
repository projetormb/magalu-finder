# -*- coding: utf-8 -*-

import MySQLdb

class Database(object):

    def __init__(self):
        pass
        self.host = 'mysql.mbcorporate.com.br'
        self.user = 'mbcorporate01'
        self.dbname = 'mbcorporate01'
        self.passwd = 'MagaluFinder'

    def Inserir(self, usuario, texto):

        values = []
        values.append(usuario.decode('latin1').encode('utf8'))
        values.append(texto.decode('latin1').encode('utf8'))

        q = """INSERT INTO `mbcorporate01`.`UltimosTw` (`Usuario`, `Texto`) VALUES (%s, %s);"""

        connection = MySQLdb.connect(host = self.host, user = self.user, passwd = self.passwd, db = self.dbname, charset='utf8', init_command='SET NAMES UTF8')
        cursor = connection.cursor()
        try:
            cursor.execute(q, values)
            connection.commit()
        except:
            connection.rollback()
        connection.close()

#INSERT INTO `mbcorporate01`.`Produtos` (`Descricao`, `ValorVenda`) VALUES ("TV Samsung 40 polegadas", 2299.99)

#INSERT INTO `mbcorporate01`.`Lojas` (`Descricao`, `CEP`) VALUES ('Loja Franca Centro', 14401216);
#INSERT INTO `mbcorporate01`.`Lojas` (`Descricao`, `CEP`) VALUES ('Loja Franca Estacao', 14405086);
#INSERT INTO `mbcorporate01`.`Lojas` (`Descricao`, `CEP`) VALUES ('Loja RP Ipiranga', 14055537);



#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 1, 1);
#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 2, 7);
#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 3, 13);
