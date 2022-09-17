# -*- coding: utf-8 -*-

import requests
import logging

def transition(**kwargs):
    body = kwargs.get('body')
    if ('pref_code' in body):
        pref_code = int(body['pref_code'][0])
        city_code = '-'
        add_area = list(map(lambda x: '{}_'.format(int(x)), body['pref_code'][1:]))

    if ('city_code' in body):
        pref_code = int(body['city_code'][0][:2])
        city_code = body['city_code'][0]
        add_area = list(map(lambda x: '{}_{}'.format(int(x[:2]), x), body['city_code'][1:]))

    headers = {
        'Referer': 'https://resas.go.jp/',
    }

    url = 'https://resas.go.jp/api/population/composition/v1/perYear/{pref_code}/{city_code}'

    payload = {}
    if len(add_area):
        payload['addArea'] = add_area

    response = requests.get(
        url.format(pref_code=pref_code, city_code=city_code),
        params=payload,
        headers=headers)

    logging.debug('RESAS: {}'.format(response.url))

    return {
        'params': body,
        'result': response.json().get('result'),
    }

def pyramid(**kwargs):
    body = kwargs.get('body')
    if ('pref_code' in body):
        pref_code = int(body['pref_code'][0])
        city_code = '-'
        year = body['year']
        add_area = list(map(lambda x: '{}_'.format(int(x)), body['pref_code'][1:]))

    if ('city_code' in body):
        pref_code = int(body['city_code'][0][:2])
        city_code = body['city_code'][0]
        year = body['year']
        add_area = list(map(lambda x: '{}_{}'.format(int(x[:2]), x), body['city_code'][1:]))

    headers = {
        'Referer': 'https://resas.go.jp/',
    }

    url = 'https://resas.go.jp/api/population/composition/v1/pyramid/{pref_code}/{city_code}/{year}/2000'

    payload = {}
    if len(add_area):
        payload['addArea'] = add_area

    response = requests.get(
        url.format(pref_code=pref_code, city_code=city_code, year=year),
        params=payload,
        headers=headers)

    logging.debug('RESAS: {}'.format(response.url))

    return {
        'params': body,
        'result': { 'data': response.json().get('result').get('yearLeft'), },
    }
