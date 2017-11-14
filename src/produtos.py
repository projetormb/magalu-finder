# -*- coding: latin-1 -*-

import MySQLdb

from banco import Tabela


class Produtos(Tabela):

    def __init__(self):
        super(Produtos, self).__init__()
        self.table_name = 'Produtos'

    def inserir(self, descricao, valor_venda):
        values = []
        #values.append(descricao.decode('latin1').encode('utf-8'))
        values.append(descricao)
        values.append(valor_venda)

        q = 'INSERT INTO ' + self.dbname + '.' + self.table_name + ' (Descricao, ValorVenda) VALUES (%s, %s);'

        ret = self.execute_query(q, values)
        self.Id = self.cursor.lastrowid
        return ret


    def atualizar(self, produto_id, descricao, valor_venda):

        values = []
        values.append(descricao)
        values.append(valor_venda)
        values.append(produto_id)

        q = 'UPDATE ' + self.dbname + '.' + self.table_name + ' SET Descricao = %s, ValorVenda = %s WHERE `Id` = %s;'

        return self.execute_query(q, values)


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
                #descricao = row[1].encode('latin1')
                #descricao = row[1].decode('utf-8').encode('latin1')

                if isinstance(row[1], str):
                    descricao = "ordinary string"
                elif isinstance(row[1], unicode):
                    descricao = "unicode string"
                else:
                    descricao = "not a string"

                #descricao = row[1].decode('utf-8').encode('latin1')



                venda = str(row[2])
                ret.append({ 'id' : produto_id, 'descricao': descricao, 'venda' : venda })

        return ret
