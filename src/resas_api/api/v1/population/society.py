# -*- coding: utf-8 -*-

import requests
import logging

def for_area(**kwargs):
    pref_code = kwargs.get('prefCode')

    headers = {
        'Referer': 'https://resas.go.jp/',
    }

    url = 'https://resas.go.jp/api/population/society/v1/forAreaStackedBar/{pref_code}'

    response = requests.get(
        url.format(pref_code=pref_code),
        headers=headers)

    logging.debug('RESAS: {}'.format(response.url))

    return response.json()

def for_age_class(**kwargs):
    pref_code = kwargs.get('prefCode')
    city_code = kwargs.get('cityCode')

    headers = {
        'Referer': 'https://resas.go.jp/',
    }

    url = 'https://resas.go.jp/api/population/society/v1/forAgeClassStackedBar/{pref_code}/{city_code}'

    response = requests.get(
        url.format(pref_code=pref_code, city_code=city_code),
        headers=headers)

    logging.debug('RESAS: {}'.format(response.url))

    return response.json()

def for_age_class_line(**kwargs):
    pref_code = kwargs.get('prefCode')
    city_code = kwargs.get('cityCode')

    headers = {
        'Referer': 'https://resas.go.jp/',
    }

    url = 'https://resas.go.jp/api/population/society/v1/forAgeClassLine/{pref_code}/{city_code}'

    response = requests.get(
        url.format(pref_code=pref_code, city_code=city_code),
        headers=headers)

    logging.debug('RESAS: {}'.format(response.url))

    return response.json()
