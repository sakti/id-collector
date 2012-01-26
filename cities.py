#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""module for grabing list of cities in indonesia from wikipedia (ID)
store result as pickle file
"""

import os
import pickle
from datetime import datetime
import re

import requests
from BeautifulSoup import BeautifulSoup

uri = 'http://id.wikipedia.org/wiki/Daftar_kota_di_Indonesia'

blacklist_token = [
    'templat', 'daftar',
]

def is_blacklisted(word):
    for token in blacklist_token:
        if word.lower().startswith(token):
            return True
    return False

def grab(url):
    '''
    Grabs people name from wikipedia
    '''
    html = requests.get(url).content
    soup = BeautifulSoup(html)
    bullets = soup.findAll('li')
    retval = {}
    list_people = []
    for bullet in bullets:
        if len(bullet.attrs) == 0:
            if is_blacklisted(bullet.text): continue
            print bullet.text
            parsed = re.split('--|[,\-)(/]',bullet.text)
            parsed = [x.strip() for x in parsed if len(x.strip()) > 0]
            list_people.append(parsed)
            print parsed
    return list_peoplels

def get_cities():
    result = grab(uri)
    print 'Dumping...'
    f = open('cities_%s.pkl' % datetime.now().strftime('%Y-%m-%d_%H:%M:%S'), 'w')
    pickle.dump(result, f)
    f.close()


if __name__ == '__main__':
    get_cities()
