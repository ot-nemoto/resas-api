# -*- coding: utf-8 -*-

import requests
import logging

def to_transition(**kwargs):
    pref_code = kwargs.get('prefecture_cd')
    display_method = kwargs.get('displayMethod')
    matter = kwargs.get('matter')
    classification = kwargs.get('classification')
    display_type = kwargs.get('displayType')
    gender = kwargs.get('gender')

    headers = {
        'Referer': 'https://resas.go.jp/',
    }

    url = 'https://resas.go.jp/api/employEducation/localjobAcademic/v3/toTransition' \
        '/{pref_code}/{display_method}/{matter}/{classification}/{display_type}/{gender}'

    response = requests.get(
        url.format(pref_code=pref_code, display_method=display_method, matter=matter,
            classification=classification, display_type=display_type, gender=gender),
        headers=headers)

    logging.debug('RESAS: {}'.format(response.url))

    return response.json()
