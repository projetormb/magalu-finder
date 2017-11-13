# -*- coding: utf-8 -*-

import MySQLdb

from banco import Tabela


class Produtos(Tabela):

    def __init__(self):
        super(Produtos, self).__init__()
        self.table_name = 'Produtos'

    def inserir(self, descricao, valor_venda):

        values = []
        values.append(descricao.decode('latin1').encode('utf-8'))
        values.append(valor_venda)

        q = """INSERT INTO `mbcorporate01`.`Produtos` (`Descricao`, `ValorVenda`) VALUES (%s, %s);"""

        return self.execute_query(q, values)


    def select_all(self):
        ret = []

        q = """SELECT Id, Descricao, ValorVenda FROM `mbcorporate01`.`""" + self.table_name + """`"""
        q += ' order by Id'

        ok = self.execute_query(q, [])

        if ok is True:
            result = self.cursor.fetchall()

            for row in result:
                produto_id = row[0]

                #if isinstance(row[1], str):
                #    descricao = "ordinary string"
                #elif isinstance(row[1], unicode):
                #    #descricao = "unicode string"
                #    #descricao = row[1].encode('utf-8')
                #    descricao = row[1].encode('latin1')
                #else:
                #    descricao = "not a string"
                
                descricao = row[1].encode('latin1')
                venda = str(row[2])
                ret.append({ 'id' : produto_id, 'descricao': descricao, 'venda' : venda })

        return ret




#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 1, 1);
#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 2, 7);
#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 3, 13);
