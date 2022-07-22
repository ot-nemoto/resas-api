# -*- coding: utf-8 -*-

import requests
import logging

def for_line(**kwargs):
    pref_code = kwargs.get('prefCode')
    city_code = kwargs.get('cityCode')
    matter = kwargs.get('matter')
    unit = kwargs.get('unit')
    sic_code = kwargs.get('sicCode')
    simc_code = kwargs.get('simcCode')
    add_area = list(filter(lambda x: x != '', kwargs.get('addArea', '').split(',')))

    headers = {
        'Referer': 'https://resas.go.jp/',
    }

    url = 'https://resas.go.jp/api/industry/statisticsDistribution/v3/forLine_v2' \
            '/{pref_code}/{city_code}/{matter}/{unit}/{sic_code}/{simc_code}/-/-'

    payload = {}
    if len(add_area):
        payload['addArea'] = add_area

    response = requests.get(
        url.format(pref_code=pref_code, city_code=city_code,
            matter=matter, unit=unit, sic_code=sic_code, simc_code=simc_code),
        params=payload,
        headers=headers)

    logging.debug('RESAS: {}'.format(response.url))

    return response.json()
