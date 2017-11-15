# -*- coding: utf-8 -*-

import requests

from estoque import Estoque

def api_distancia_google(cep_origem, cep_destino):
    ret = { 'success' : False }

    url_target =  'http://maps.googleapis.com/maps/api/distancematrix/json?'
    url_target += 'origins=' + cep_origem
    url_target += '&destinations=' + cep_destino
    url_target += '&mode=CAR&language=PT&sensor=false'

    google_response = requests.get(url_target)

    google_json = google_response.json()

    if 'status' not in google_json:
        ret['error'] = 'Google - não retornou status'
        return ret

    if google_json['status'] != 'OK':
        ret['error'] = 'Google - status not OK'
        return ret

    if 'rows' not in google_json:
        ret['error'] = 'Google - rows não encontrada'
        return ret

    if len(google_json['rows']) == 0:
        ret['error'] = 'Google - rows zero'
        return ret

    for row in google_json['rows']:

        if 'elements' not in row:
            ret['error'] = 'elements não está em row'
            return ret

        for element in row['elements']:
            if 'distance' not in element:
                ret['error'] = 'Google - element não possui distance'
                return ret

            distance = element['distance']

            if 'text' not in distance:
                ret['error'] = 'Google - distance não possui text'
                return ret

            if 'value' not in distance:
                ret['error'] = 'Google - distance não possui value'
                return ret

            distance_text = distance['text']
            distance_value = distance['value']

            ret['success'] = True
            ret['distance'] = { 'text' : distance['text'], 'value' : distance['value'] }
            return ret

        ret['error'] = 'Google - nenhum element foi encontrado'
        return ret

    ret['error'] = 'Google - nenhuma row foi encontrada'
    return ret


def api_lojas_mais_proximas(produto_id, cep_cliente):

    estoque = Estoque()

    lojas_encontradas = estoque.select_lojas_com_produto(produto_id)

    if len(lojas_encontradas) > 0:
        print 'sim'

        for f in lojas_encontradas:

            f['distancia'] = 0
            f['km'] = ''

            cep_loja = f['cep']

            ret_google = api_distancia_google(cep_loja, cep_cliente)

            if 'distance' in ret_google:

                distance = ret_google['distance']

                if 'value' in distance:
                    f['distancia'] = distance['value']
                    f['km'] = distance['text']

        return sorted(lojas_encontradas, key=lambda k: k['distancia'])

    return lojas_encontradas
