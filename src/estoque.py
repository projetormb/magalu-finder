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




    def atualizar_quantidade(self, produto_id, loja_id, nova_quantidade):
        values = []
        values.append(produto_id)
        values.append(loja_id)
        values.append(quantidade)

        q = 'UPDATE ' + self.dbname + '.' + self.table_name + ' SET Quantidade = %s + 1 WHERE ProdutoID = %s AND LojaID = %s;'

        ret = self.execute_query(q, values)

        if self.cursor.rowcount == 0:
            pass

        return ret


    def deletar(self, produto_id):
        values = []
        values.append(produto_id)

        q = 'DELETE FROM ' + self.dbname + '.' + self.table_name + ' WHERE Id = %s;'

        return self.execute_query(q, values)


    def select_all(self):
        ret = []

        q = 'SELECT Id, Descricao, ValorVenda FROM ' + self.dbname + '.' + self.table_name + ' ORDER BY Id;'

        ok = self.execute_query(q, [])

        if ok is True:
            result = self.cursor.fetchall()

            for row in result:
                produto_id = int(row[0])
                descricao = row[1]
                venda = str(row[2])
                ret.append({ 'id' : produto_id, 'descricao': descricao, 'venda' : venda })

        return ret


    def select_lojas_com_produto(self, produto_id):

        q = 'SELECT T1.LojaID, T2.Descricao, T2.CEP, T1.Quantidade FROM '
        q += self.dbname + '.' + self.table_name + ' T1'
        q += ' inner join ' + self.dbname + '.Lojas T2 on T1.LojaID = T2.ID'
        q += ' WHERE T1.ProdutoID = %s AND T1.Quantidade > 0 ORDER BY T1.Quantidade;'

        values = []
        values.append(produto_id)

        ok = self.execute_query(q, values)

        ret = []

        if ok is True:
            result = self.cursor.fetchall()

            for row in result:

                loja = int(row[0])
                descricao = row[1]
                cep = row[2]
                quantidade = int(row[3])
                ret.append({ 'loja' : loja, 'descricao' : descricao, 'quantidade' : quantidade, 'cep' : cep })

        return ret
