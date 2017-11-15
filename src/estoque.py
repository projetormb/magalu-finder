# -*- coding: utf-8 -*-

import MySQLdb

from banco import Tabela


class Estoque(Tabela):

    def __init__(self):
        super(Estoque, self).__init__()
        self.table_name = 'Estoque'

    def inserir(self, produto_id, loja_id, quantidade):
        values = []

        values.append(produto_id)
        values.append(loja_id)
        values.append(quantidade)

        q = 'INSERT INTO ' + self.dbname + '.' + self.table_name + ' (ProdutoID, LojaID, Quantidade) VALUES (%s, %s, %s);'

        ret = self.execute_query(q, values)
        self.Id = self.cursor.lastrowid
        return ret


    def add_quantidade(self, produto_id, loja_id, quantidade):

    def atualizar_quantidade(self, produto_id, loja_id, nova_quantidade):
        values = []
        values.append(produto_id)
        values.append(loja_id)
        values.append(quantidade)

        q = 'UPDATE ' + self.dbname + '.' + self.table_name + ' SET Quantidade = %s + 1 WHERE ProdutoID = %s AND LojaID = %s;'

        ret = self.execute_query(q, values)

        if self.cursor.rowcount == 0:
            # insert

        return ret


    def deletar(self, produto_id):
        values = []
        values.append(produto_id)

        q = 'DELETE FROM ' + self.dbname + '.' + self.table_name + ' WHERE Id = %s;'

        return self.execute_query(q, values)


    def select_all(self):
        ret = []

        q = 'SELECT Id, Descricao, ValorVenda FROM ' + self.dbname + '.' + self.table_name + ' ORDER BY Id'

        ok = self.execute_query(q, [])

        if ok is True:
            result = self.cursor.fetchall()

            for row in result:
                produto_id = int(row[0])
                descricao = row[1]
                venda = str(row[2])
                ret.append({ 'id' : produto_id, 'descricao': descricao, 'venda' : venda })

        return ret
