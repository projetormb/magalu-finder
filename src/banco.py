# -*- coding: latin-1 -*-






#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 1, 1);
#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 2, 7);
#INSERT INTO `mbcorporate01`.`Estoque` (`ProdutoID`, `LojaID`, `Quantidade`) VALUES (1, 3, 13);


import MySQLdb

class Tabela(object):

    def __init__(self):
        self.host = 'mysql.mbcorporate.com.br'
        self.user = 'mbcorporate01'
        self.dbname = 'mbcorporate01'
        self.passwd = 'MagaluFinder2017'
        self.table_name = None


    def prepare_tests(self):
        return  self.execute_query("""CALL `mbcorporate01`.`clear_db`();""", [])


    def execute_query(self, query, values):
        ret = False
        connection = MySQLdb.connect(host=self.host, user=self.user, passwd =self.passwd, db=self.dbname, charset='latin1', init_command='SET NAMES latin1')
        self.cursor = connection.cursor()
        try:
            self.cursor.execute(query, values)
            connection.commit()
            ret = True
        except:
            connection.rollback()
        connection.close()
        return ret


    def count(self):
        q = """SELECT COUNT(*) FROM `mbcorporate01`.`""" + self.table_name + """`"""

        self.execute_query(q, [])

        result = self.cursor.fetchone()
        total_rows = result[0]

        return int(total_rows)
