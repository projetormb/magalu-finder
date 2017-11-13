# -*- coding: utf-8 -*-

import MySQLdb

from banco import Tabela


class Lojas(Tabela):

    def __init__(self):
        super(Lojas, self).__init__()
        self.table_name = 'Lojas'

    def inserir(self, descricao, cep):

        values = []
        values.append(descricao.decode('latin1').encode('utf8'))
        values.append(cep.decode('latin1').encode('utf8'))

        q = """INSERT INTO `mbcorporate01`.`Lojas` (`Descricao`, `CEP`) VALUES (%s, %s);"""

        return self.execute_query(q, values)





#INSERT INTO `mbcorporate01`.`Produtos` (`Descricao`, `ValorVenda`) VALUES ("TV Samsung 40 polegadas", 2299.99)

#INSERT INTO `mbcorporate01`.`Lojas` (`Descricao`, `CEP`) VALUES ('Loja Franca Centro', 14401216);
#INSERT INTO `mbcorporate01`.`Lojas` (`Descricao`, `CEP`) VALUES ('Loja Franca Estacao', 14405086);
#INSERT INTO `mbcorporate01`.`Lojas` (`Descricao`, `CEP`) VALUES ('Loja RP Ipiranga', 14055537);

#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 1, 1);
#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 2, 7);
#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 3, 13);