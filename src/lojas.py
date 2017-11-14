# -*- coding: utf-8 -*-

import MySQLdb

from banco import Tabela


class Lojas(Tabela):

    def __init__(self):
        super(Lojas, self).__init__()
        self.table_name = 'Lojas'

    def inserir(self, descricao, cep):
        values = []

        values.append(descricao.encode('utf-8'))
        values.append(cep)

        q = 'INSERT INTO ' + self.dbname + '.' + self.table_name + ' (Descricao, cep) VALUES (%s, %s);'

        ret = self.execute_query(q, values)
        self.Id = self.cursor.lastrowid
        return ret


    def atualizar(self, loja_id, descricao, cep):

        values = []
        values.append(descricao.encode('utf-8'))
        values.append(cep)
        values.append(loja_id)

        q = 'UPDATE ' + self.dbname + '.' + self.table_name + ' SET Descricao = %s, cep = %s WHERE `Id` = %s;'

        return self.execute_query(q, values)


    def deletar(self, loja_id):
        values = []
        values.append(loja_id)

        q = 'DELETE FROM ' + self.dbname + '.' + self.table_name + ' WHERE Id = %s;'

        return self.execute_query(q, values)


    def select_all(self):
        ret = []

        q = 'SELECT Id, Descricao, cep FROM ' + self.dbname + '.' + self.table_name + ' ORDER BY Id'

        ok = self.execute_query(q, [])

        if ok is True:
            result = self.cursor.fetchall()

            for row in result:
                loja_id = int(row[0])
                descricao = row[1]
                cep = str(row[2])
                ret.append({ 'id' : loja_id, 'descricao': descricao, 'cep' : cep })

        return ret
