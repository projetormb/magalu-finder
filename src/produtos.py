# -*- coding: utf-8 -*-

import MySQLdb

from banco import Tabela


class Produtos(Tabela):

    def __init__(self):
        super(Produtos, self).__init__()
        self.table_name = 'Produtos'

    def inserir(self, descricao, valor_venda):

        values = []
        values.append(descricao.decode('latin1').encode('utf8'))
        #values.append(valor_venda.decode('latin1').encode('utf8'))
        values.append(valor_venda)

        q = """INSERT INTO `mbcorporate01`.`Produtos` (`Descricao`, `ValorVenda`) VALUES (%s, %s);"""

        return self.execute_query(q, values)






#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 1, 1);
#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 2, 7);
#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 3, 13);
