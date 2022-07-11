# -*- coding: utf-8 -*-

import requests

def for_area(**kwargs):
    pref_code = kwargs.get('prefCode')

    headers = {
        'Referer': 'https://resas.go.jp/',
    }

    url = 'https://resas.go.jp/api/population/society/v1/forAreaStackedBar/{pref_code}'

    response = requests.get(
        url.format(pref_code=pref_code),
        headers=headers)

    return response.json()
