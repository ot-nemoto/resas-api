# -*- coding: utf-8 -*-

import requests
import logging

def for_industry(**kwargs):
    year = kwargs.get('year')
    pref_code = kwargs.get('prefCode')
    city_code = kwargs.get('cityCode')
    sic_code = kwargs.get('sicCode')

    headers = {
        'Referer': 'https://resas.go.jp/',
    }

    url = 'https://resas.go.jp/api/industry/power/v2/forIndustryWideBar/{year}/{pref_code}/{city_code}/{sic_code}'

    response = requests.get(
        url.format(year=year, pref_code=pref_code, city_code=city_code, sic_code=sic_code),
        headers=headers)

    logging.debug('RESAS: {}'.format(response.url))

    return response.json()
