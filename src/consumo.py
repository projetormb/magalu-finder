# -*- coding: latin1 -*-

# verificar char set !!!!!!!!!!!!!!!!!

import json

from banco import Database
from flask import jsonify
from requests_oauthlib import OAuth1Session

def responseTwitter(screen_name, max_tweets):

    API_KEY = 'u9JQJ77IwU59dPM6RXYNo3HiR'
    API_SECRET = 'vGt9rsNMl4TPp7H3g5GIsCEpUE050MREopHDNI35Xf8FLm4neI'
    ACCESS_TOKEN = '42063631-gDtvbUX5BzfIyBfkpO7zSt9j0vCy11VU5ua8HR9I0'
    ACCESS_TOKEN_SECRET = 'M0ar8Yggt0OpE4zwjyTXPt2ctFM56pAmP0TTHbMFbeUOm'

    session = OAuth1Session(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name='
    url += screen_name
    url += '&count='
    url += str(max_tweets)

    return session.get(url)

def consumoTwitter(screen_name, max_tweets):

    retorno = {}

    response = responseTwitter(screen_name, max_tweets)

    if response.status_code == 200:
        pass
    else:
        if response.status_code == 404:
            return retorno
        else:
            pass



    tweets = json.loads(response.content)

    # https://twitter.com/rmbertoni/with_replies
    # Nesta URL é possível visualizar os tweets que a API está me retornando.

    if len(tweets) > 0:
        db = Database()

        index = -1

        for tweet in tweets:
            tweetText = tweet['text'].encode('utf8')

            index += 1
            retorno[index] = tweetText

            #tweetLatin = tweetText.decode('latin1')
            #db.Inserir('rmbertoni', tweetLatin)

            ##############################################################################################
            # testar erro de caracteres como emotion icons !!!!!!!!!!!!!
            ##############################################################################################
            db.Inserir(screen_name, tweetText)
            ##############################################################################################


    if len(retorno) == 0:
        retorno[0] = 'Nenhum tweet'

    return retorno
