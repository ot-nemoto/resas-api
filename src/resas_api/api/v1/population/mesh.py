# -*- coding: utf-8 -*-

import requests
import logging

def chart(**kwargs):
    year = kwargs.get('year')
    pref_code = kwargs.get('prefecture_cd')
    city_code = kwargs.get('city_cd')
    matter = kwargs.get('matter')
    display_method = kwargs.get('displayMethod')

    headers = {
        'Referer': 'https://resas.go.jp/',
    }

    url = 'https://resas.go.jp/api/population/mesh/v3/chart' \
        '/{year}/{pref_code}/{city_code}/{matter}/{display_method}'

    response = requests.get(
        url.format(year=year, pref_code=pref_code, city_code=city_code,
            matter=matter, display_method=display_method),
        headers=headers)

    logging.debug('RESAS: {}'.format(response.url))

    return response.json()
