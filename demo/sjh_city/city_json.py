# -*- encoding: utf-8 -*-
import json

data = None


def province(province_name=None):
    if province_name:
        for p in data['province']:
            if p['text'] == province_name:
                return p
    else:
        return data['province']


def city(province_name='北京市'):
    for p in data['province']:
        if p['text'] == province_name:
            return [x for x in data['city'] if x['id'][0:2] == p['id'][0:2]]


def district(province_name='江苏省', city_name='南京市'):
    for p in city(province_name):
        if p['text'] == city_name:
            return [x for x in data['district'] if x['id'][0:4] == p['id'][0:4]]


if __name__ == '__main__':
    with open('city.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(province())
    print(province('江苏省'))
    print(city('江苏省'))
    print(district('江苏省', '南京市'))
else:
    with open('city.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
