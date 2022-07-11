# -*- coding: utf-8 -*-

import requests

def for_line_bar(**kwargs):
    pref_code = kwargs.get('prefCode')
    city_code = kwargs.get('cityCode')
    age_from = kwargs.get('ageFrom')
    age_to = kwargs.get('ageTo')

    headers = {
        'Referer': 'https://resas.go.jp/',
    }

    url = 'https://resas.go.jp/api/population/nature/v1/forLineBar/{pref_code}/{city_code}/{age_from}/{age_to}'

    response = requests.get(
        url.format(pref_code=pref_code, city_code=city_code, age_from=age_from, age_to=age_to),
        headers=headers)

    return response.json()
