# -*- coding: utf-8 -*-

import unittest2

import json

from apis import api_distancia_google


# http://127.0.0.1:5000/distancia/?CEPOrigem=13201-031&CEPDestino=14401-216
# http://127.0.0.1:5000/distancia/?CEPOrigem=14403-587&CEPDestino=14401-216

def test_consumo_google(cep_origem, cep_destino, distanciaEsperada):

    print '  - CEP de Origem: ' + str(cep_origem) + ' para CEP de Destino ' + str(cep_destino)


    output = 'OK'

    ret = api_distancia_google(cep_origem, cep_destino)



    if 'success' in ret:
        if ret['success'] is True:
            

            if 'distance' in ret:

                if 'text' in ret['distance']:
                    output = '    Distância: ' + str(ret['distance']['text'])

                if 'value' in ret['distance']:
                    distance_value = ret['distance']['value']

                    if distance_value == distanciaEsperada:
                        output += ' - OK'
                        print output
                        print ' '
                        return True






    print output
    print ' '

    return False

def test_consumoTwitter(userName, maxTweets):
    tweetsRetornados = consumoTwitter(userName, maxTweets)

    for x in range(0, 30):
        print ' '


    print '    - userName : ' + userName + ' maxTweets : ' + str(maxTweets)
    print '      -- retornou : ' + str(len(tweetsRetornados)) + ' tweets ...'
    print ' '

    return len(tweetsRetornados)


class MyTest(unittest2.TestCase):
    def test(self):

        for x in range(0, 30):
            print ' '

        print 'Iniciando testes ...'
        print '========================================================================='
        print ' '
        print '> Testando distância entre 2 CEPs:'
        print ' '

        self.assertEqual(test_consumo_google('13201-031', '14401-216', 347889), True)
        self.assertEqual(test_consumo_google('13201-031', '14401-216', 347999), False)
        self.assertEqual(test_consumo_google('14401-216', '69005-140', 0), False)

        print 'Fim dos testes.'
        print '========================================================================='


if __name__ == '__main__':
    unittest2.main()
