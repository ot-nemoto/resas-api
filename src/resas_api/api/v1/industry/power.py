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

def for_area(**kwargs):
    year = kwargs.get('year')
    pref_code = kwargs.get('prefCode')
    area_type = kwargs.get('areaType')
    disp_type = kwargs.get('dispType')
    sic_code = kwargs.get('sicCode')
    simc_code = kwargs.get('simcCode')
    add_industry = list(filter(lambda x: x != '', kwargs.get('addIndustry', '').split(',')))

    headers = {
        'Referer': 'https://resas.go.jp/',
    }

    url = 'https://resas.go.jp/api/industry/power/v1/forAreaBar/{year}/{pref_code}/{area_type}/{disp_type}/{sic_code}/{simc_code}'

    payload = {}
    if len(add_industry):
        payload['addIndustry'] = add_industry

    response = requests.get(
        url.format(year=year, pref_code=pref_code, area_type=area_type, disp_type=disp_type, sic_code=sic_code, simc_code=simc_code),
        params=payload,
        headers=headers)

    logging.debug('RESAS: {}'.format(response.url))

    return response.json()

def for_manufacturer_establishments(**kwargs):
    pref_code = kwargs.get('prefCode')
    sic_code = kwargs.get('sicCode')
    simc_code = kwargs.get('simcCode')
    add_area = list(filter(lambda x: x != '', kwargs.get('addArea', '').split(',')))

    headers = {
        'Referer': 'https://resas.go.jp/',
    }

    url = 'https://resas.go.jp/api/industry/power/v1/forManufacturerEstablishmentsLine/{pref_code}/{sic_code}/{simc_code}'

    payload = {}
    if len(add_area):
        payload['addArea'] = add_area

    response = requests.get(
        url.format(pref_code=pref_code, sic_code=sic_code, simc_code=simc_code),
        params=payload,
        headers=headers)

    logging.debug('RESAS: {}'.format(response.url))

    return response.json()
