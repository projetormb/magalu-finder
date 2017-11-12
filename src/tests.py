# -*- coding: utf-8 -*-

import unittest2

from apis import api_distancia_google

from lojas import Lojas, Table

def test_consumo_google(cep_origem, cep_destino, distanciaEsperada, **kwargs):

    output = '  - CEP de Origem: ' + str(cep_origem) + ' para CEP de Destino ' + str(cep_destino)

    if len(kwargs) > 0:
        for k, v in kwargs.iteritems():
            if k.lower() == 'description':
                output += '  (' + str(v) + ')'

    print output

    ret = api_distancia_google(cep_origem, cep_destino)

    if 'success' in ret:
        if ret['success'] is True:
            

            if 'distance' in ret:

                if 'text' in ret['distance']:
                    print '  - Distância: ' + str(ret['distance']['text'])

                if 'value' in ret['distance']:
                    distance_value = ret['distance']['value']

                    if distance_value == distanciaEsperada:
                        print '  - OK'
                        print ' '
                        return True


    print '  - retornando False'
    print ' '

    return False


def test_preparar_db():

    print '  - Limpando tabelas para executar testes ...'
    print ' '

    table = Table()
    table.prepare_tests()

    print '  - OK'
    print ' '


    return True


def test_banco_dados(descricao, cep):

    print '  - Inserindo Loja: ' + str(descricao) + ' com CEP: ' + str(cep)

    loja = Lojas()
    ret = loja.inserir(descricao, cep)

    if ret is True:
        print '  - OK'
    else:
        print '  - ERRO'

    print ' '

    return ret



class MyTest(unittest2.TestCase):

    def test(self):

        for x in range(0, 30):  # ajuda como clear screen
            print ' '           # ajuda como clear screen



        print 'Iniciando testes ...'
        print '========================================================================='


        print ' '
        print '> Testando distância entre 2 CEPs:'
        print ' '

        self.assertEqual(test_consumo_google('13201-031', '14401-216', 347889, Description='Jundiai para Franca'), True)
        self.assertEqual(test_consumo_google('13201-031', '14401-216', 347999, Description='Jundiai para Franca com distancia errada'), False)
        self.assertEqual(test_consumo_google('69005-140', '14401-216', 3636904, Description='Manaus para Franca'), True)
        self.assertEqual(test_consumo_google('14401-216', '69005-140', 3623512, Description='Franca para Manaus'), True)
        self.assertEqual(test_consumo_google('14402-029', '02232-000', 413622, Description='Ceara para Guarulhos'), True)

        self.assertEqual(test_consumo_google('', '14402-029', 0, Description='CEP de Origem invalido'), False)
        self.assertEqual(test_consumo_google('14402-029', '', 0, Description='CEP de Destino invalido'), False)
        self.assertEqual(test_consumo_google('69005-140', '14401-216', 0, Description='Distancia nao informada'), False)



        print ' '
        print '> Testando banco de dados:'
        print ' '

        self.assertEqual(test_preparar_db(), True)

        self.assertEqual(test_banco_dados('Feira de Santana - Conselheiro', '44002-128'), True)
        self.assertEqual(test_banco_dados('Feira de Santana - Senhor', '44002-200'), True)
        self.assertEqual(test_banco_dados('Feira de Santana - Marechal', '44002-064'), True)


        for x in range(0, 10):
            filialX = 'Nome da filial ficticia numero ' + str(x)
            self.assertEqual(test_banco_dados(filialX, '44002-064'), True)



        print 'Fim dos testes.'
        print '========================================================================='


if __name__ == '__main__':
    unittest2.main()
