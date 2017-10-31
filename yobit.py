#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

# mosia
# password yobit.io
# mo555yayobiT


def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    response = requests.get(url).json()
    price = response['ticker']['last']
    return '{} usd'.format(price)


