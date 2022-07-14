# -*- coding: utf-8 -*-

import requests
import logging

def per_year(**kwargs):
    pref_code = kwargs.get('prefCode')
    city_code = kwargs.get('cityCode')
    add_area = list(filter(lambda x: x != '', kwargs.get('addArea', '').split(',')))

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

    return response.json()

def pyramid(**kwargs):
    pref_code = kwargs.get('prefCode')
    city_code = kwargs.get('cityCode')
    year_left = kwargs.get('yearLeft')
    year_right = kwargs.get('yearRight')
    add_area = list(filter(lambda x: x != '', kwargs.get('addArea', '').split(',')))

    headers = {
        'Referer': 'https://resas.go.jp/',
    }

    url = 'https://resas.go.jp/api/population/composition/v1/pyramid/{pref_code}/{city_code}/{year_left}/{year_right}'

    payload = {}
    if len(add_area):
        payload['addArea'] = add_area

    response = requests.get(
        url.format(pref_code=pref_code, city_code=city_code, year_left=year_left, year_right=year_right),
        params=payload,
        headers=headers)

    logging.debug('RESAS: {}'.format(response.url))

    return response.json()
