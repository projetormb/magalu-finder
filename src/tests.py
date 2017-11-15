# -*- coding: utf-8 -*-

import unittest2

from apis import api_distancia_google

from banco import Tabela
from lojas import Lojas
from produtos import Produtos
from estoque import Estoque

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

    tabela = Tabela()
    tabela.prepare_tests()

    print '  - OK'
    print ' '

    return True


def test_insert_loja(descricao, cep):

    print u'  - Inserindo Loja: ' + descricao + u' com CEP: ' + cep

    loja = Lojas()
    ret = loja.inserir(descricao, cep)

    if ret is True:
        print '  - OK'
    else:
        print '  - ERRO'

    print ' '

    return ret


def test_quantidade_lojas():

    loja = Lojas()
    qtd_in_db = loja.count()

    print '  - Quantidade de Lojas no Banco de Dados: ' + str(qtd_in_db)
    print '  - OK'
    print ' '

    return qtd_in_db


def test_insert_produto(descricao, valor_venda):

    print '  - Inserindo Produto: '
    print u'  - Descrição: ' + descricao
    print '  - Valor de venda: ' + str(valor_venda)

    produto = Produtos()
    ret = produto.inserir(descricao, valor_venda)

    if ret is True:
        print '  - OK'
    else:
        print '  - ERRO'

    print ' '

    return ret


def test_atualiza_produto(produto_id, descricao, valor_venda):

    print '  - Atualizando o Produto: ' + str(produto_id)
    print u'  - Descrição: ' + descricao
    print '  - Valor de venda: ' + str(valor_venda)

    produto = Produtos()
    ret = produto.atualizar(produto_id, descricao, valor_venda)

    if ret is True:
        print '  - OK'
    else:
        print '  - ERRO'

    print ' '

    return ret

def test_select_all_produtos():
    print '  - Selecionando Todos os Produtos:'

    produto = Produtos()
    result = produto.select_all()

    if len(result) > 0:

        print result[0]


        print '  - OK'
        print ' '
        return True
    else:
        print '  - ERRO'
        print ' '
        return False



def test_quantidade_produtos():

    produto = Produtos()
    qtd_in_db = produto.count()

    print '  - Quantidade de Produtos no Banco de Dados: ' + str(qtd_in_db)
    print '  - OK'
    print ' '

    return qtd_in_db


def test_insert_estoque(produto_id, loja_id, quantidade):

    estoque = Estoque()
    ret = estoque.inserir(produto_id, loja_id, quantidade)

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


        """
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
        """


        """
        print ' '
        print '> Testando banco de dados:'
        print ' '


        self.assertEqual(test_preparar_db(), True) # truncate tables ...


        print ' '
        print '> Inserindo Lojas:'
        print ' '

        self.assertEqual(test_insert_loja(u'Feira de Santana - Conselheiro', '44002-128'), True)
        self.assertEqual(test_insert_loja(u'Feira de Santana - Senhor', '44002-200'), True)
        self.assertEqual(test_insert_loja(u'Feira de Santana - Marechal', '44002-064'), True)
        self.assertEqual(test_insert_loja(u'Ribeirão Preto', '15002-069'), True)

        self.assertEqual(test_quantidade_lojas(), 4)


        for x in range(5, 11):
            filialX = 'Nome da filial ficticia numero ' + str(x)
            self.assertEqual(test_insert_loja(filialX.encode('utf-8'), '44002-064'), True)

        self.assertEqual(test_quantidade_lojas(), 10)



        print ' '
        print '> Inserindo Produtos:'
        print ' '


        self.assertEqual(test_insert_produto(u'Purificador de Água Natural, Gelada ou Fria Electrolux PE11B Branco com Painel Touch - Electrolux', 399.00), True)
        self.assertEqual(test_select_all_produtos(), True)


        self.assertEqual(test_insert_produto(u'Purifuicador de Água Natural, Gelada ou Fria Electrolux PE11B Branco com Painel Touch - Electrolux', 399.00), True)
        self.assertEqual(test_insert_produto(u'Fogão 4 Bocas Consul CFO4NAR Inox - Acendimento Automático', 693.41), True)
        self.assertEqual(test_insert_produto(u'Notebook Dell Inspiron i15-5566-D10P Intel Core i3 - 4GB 1TB LED 15,6 \" Linux', 1529.90), True)
        self.assertEqual(test_insert_produto(u'Notebook Samsung Expert X23 Intel Core i5 - 8GB 1TB LED 15,6 \" GeForce 920MX 2GB Windows 10', 2324.91), True)
        self.assertEqual(test_insert_produto(u'Smartphone Motorola Moto G5s Plus 32GB - Platinum Dual Chip 4G Cam. Duo 13MP + 13MP', 1274.15), True)
        self.assertEqual(test_insert_produto(u'Guarda-roupa Casal 10 Portas 3 Gavetas - Araplac Rusti 18490-88', 289.99), True)
        self.assertEqual(test_insert_produto(u'Guarda-roupa Casal 4 Portas 6 Gavetas - Araplac Sofia com Espelho', 599.99), True)
        self.assertEqual(test_insert_produto(u'Lava e Seca Samsung 10kg WD106UHSAWQ - 14 Programas de Lavagem Água Quente', 2369.90), True)
        self.assertEqual(test_insert_produto(u'Smart TV LED 43 \" LG 43LJ5550 webOS - Conversor Digital 1 USB 2 HDMI', 1804.91), True)
        self.assertEqual(test_insert_produto(u'Smart TV OLED 55 \" LG 4K/Ultra HD OLED55B7P - Conversor Digital Wi-Fi 4 HDMI 3 USB', 9499.05), True)
        self.assertEqual(test_insert_produto(u'Cafeteira Elétrica Cadence Single Colors CAF112 - 2 Xícaras Roxa', 59.90), True)
        self.assertEqual(test_insert_produto(u'Cooktop 5 Bocas Consul Facilite CD075AE à Gás - Acendimento Superautomático', 436.05), True)
        self.assertEqual(test_insert_produto(u'Smartphone Samsung Galaxy J5 Prime 32GB Dourado - Dual Chip 4G Câm. 13MP + Selfie 5MP Tela 5\" HD', 674.10), True)
        self.assertEqual(test_insert_produto(u'iPhone SE Apple 128GB Prateado 4G Tela 4\" - Retina Câm. 12MP iOS 10 Proc. Chip A9 Touch ID', 1759.12), True)
        self.assertEqual(test_insert_produto(u'Máquina de Costura Singer Facilita Pro 2918 - Eletrônica 18 Pontos', 806.55), True)

        self.assertEqual(test_quantidade_produtos(), 16)

        self.assertEqual(test_atualiza_produto(15, u'Máquina de Costura Singer Facilita Pro 2918 - Eletrônica 99 Pontos', 999.99), True)

        self.assertEqual(test_quantidade_produtos(), 16)

        self.assertEqual(test_select_all_produtos(), True)
        """


        self.assertEqual(test_insert_estoque(15, 4, 1), True)


        print 'Fim dos testes.'
        print '========================================================================='


if __name__ == '__main__':
    unittest2.main()
