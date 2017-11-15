# -*- coding: utf-8 -*-

import requests

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


def api_filiais_mais_proximas(produto_id, cep_cliente):
    max_filiais = 3


    filiais_encontradas = []
    filiais_encontradas.append({ 'filial_id' : 8, 'descricao' : 'RP', 'distancia' : 118 })
    filiais_encontradas.append({ 'filial_id' : 9, 'descricao' : 'Campinas', 'distancia' : 427 })
    filiais_encontradas.append({ 'filial_id' : 10, 'descricao' : 'Franca', 'distancia' : 5 })

    #newlist = sorted(filiais_encontradas, key=lambda k: k['distancia'])

    return filiais_encontradas.sort(key=operator.itemgetter('distancia'))



    # ordenar distancia ascendente............




