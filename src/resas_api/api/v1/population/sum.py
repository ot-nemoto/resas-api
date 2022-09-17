# -*- coding: utf-8 -*-

import requests
import logging

def for_line_bar(**kwargs):
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

    url = 'https://resas.go.jp/api/population/sum/v1/forLineBar/{pref_code}/{city_code}'

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
        'result': response.json().get('result').get('bar'),
    }

def sum_line(**kwargs):
    body = kwargs.get('body')
    if ('pref_code' in body):
        pref_code = int(body['pref_code'])
        city_code = '-'

    if ('city_code' in body):
        pref_code = int(body['city_code'][:2])
        city_code = body['city_code']

    headers = {
        'Referer': 'https://resas.go.jp/',
    }

    url = 'https://resas.go.jp/api/population/sum/v1/sumLine/{pref_code}/{city_code}'

    response = requests.get(
        url.format(pref_code=pref_code, city_code=city_code),
        headers=headers)

    logging.debug('RESAS: {}'.format(response.url))

    return {
        'params': body,
        'result': response.json().get('result'),
    }

def transition_bar_line(**kwargs):
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

    url = 'https://resas.go.jp/api/population/sum/v1/transitionBarLine/{pref_code}/{city_code}'

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
