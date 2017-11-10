# -*- coding: utf-8 -*-

import MySQLdb

class Database(object):

    def __init__(self):
        pass
        self.host = 'mysql.mbcorporate.com.br'
        self.user = 'mbcorporate01'
        self.passwd = 'Desafio2017'
        self.dbname = 'mbcorporate01'

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
