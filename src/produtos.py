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


    def atualizar(self, produto_id, descricao, valor_venda):
        values = []
        values.append(descricao.encode('utf-8'))
        values.append(valor_venda)
        values.append(produto_id)

        q = """UPDATE `mbcorporate01`.`Produtos` SET """ 
        q += """`Descricao` = %s, """
        q += """`ValorVenda` = %s WHERE `Id` = %s;"""

        return self.execute_query(q, values)


    def deletar(self, produto_id):
        values = []
        values.append(produto_id)

        q = 'DELETE FROM ' + self.dbname + '.' + self.table_name + ' WHERE Id = %s;'

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
                descricao = row[1].encode('latin1')
                venda = str(row[2])
                ret.append({ 'id' : produto_id, 'descricao': descricao, 'venda' : venda })

        return ret
