# -*- coding: utf-8 -*-

import requests
import logging

def per_year(**kwargs):
    year = kwargs.get('year')
    pref_code = kwargs.get('prefCode')
    city_code = kwargs.get('cityCode')
    sic_code = kwargs.get('sicCode')
    simc_code = kwargs.get('simcCode')

    headers = {
        'Referer': 'https://resas.go.jp/',
    }

    url = 'https://resas.go.jp/api/municipality/value/v3/perYear' \
            '/{year}/{pref_code}/{city_code}/{sic_code}/{simc_code}'

    response = requests.get(
        url.format(year=year, pref_code=pref_code, city_code=city_code,
            sic_code=sic_code, simc_code=simc_code),
        headers=headers)

    logging.debug('RESAS: {}'.format(response.url))

    return response.json()
