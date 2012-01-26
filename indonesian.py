#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""module for grabing list of indonesian from wikipedia (ID)
store result as pickle file
"""

import os
import pickle
from datetime import datetime
import re

import requests
from BeautifulSoup import BeautifulSoup

list_uris = [
('ekonom', 'http://id.wikipedia.org/wiki/Daftar_ekonom_Indonesia'),
('bisnis', 'http://id.wikipedia.org/wiki/Daftar_tokoh_bisnis_Indonesia'),
('olahragawan', 'http://id.wikipedia.org/wiki/Daftar_olahragawan_Indonesia'),
('sastrawan', 'http://id.wikipedia.org/wiki/Daftar_sastrawan_Indonesia'),
('seniman', 'http://id.wikipedia.org/wiki/Daftar_seniman_Indonesia'),
('sejarawan', 'http://id.wikipedia.org/wiki/Daftar_sejarawan_Indonesia'),
('sosiolog', 'http://id.wikipedia.org/wiki/Daftar_sosiolog_Indonesia'),
('sutradara', 'http://id.wikipedia.org/wiki/Daftar_sutradara_Indonesia'),
# ('pahlawan', 'http://id.wikipedia.org/wiki/Daftar_pahlawan_nasional_Indonesia'),
('politisi', 'http://id.wikipedia.org/wiki/Daftar_politisi_Indonesia'),
('agama', 'http://id.wikipedia.org/wiki/Daftar_tokoh_agama_Indonesia'),
('hukum', 'http://id.wikipedia.org/wiki/Daftar_tokoh_hukum_Indonesia'),
('militer', 'http://id.wikipedia.org/wiki/Daftar_tokoh_militer_Indonesia'),
('pers', 'http://id.wikipedia.org/wiki/Daftar_tokoh_pers_Indonesia'),
('teknologi informasi', 'http://id.wikipedia.org/wiki/Daftar_tokoh_teknologi_informasi_Indonesia'),
('keturunan', 'http://id.wikipedia.org/wiki/Daftar_tokoh_keturunan_atau_kelahiran_Indonesia'),
('aktor', 'http://id.wikipedia.org/wiki/Daftar_aktor_Indonesia'),
('aktris', 'http://id.wikipedia.org/wiki/Daftar_aktris_Indonesia'),
('penyanyi pria', 'http://id.wikipedia.org/wiki/Daftar_penyanyi_pria_Indonesia'),
('penyanyi wanita', 'http://id.wikipedia.org/wiki/Daftar_penyanyi_wanita_Indonesia'),

('arab-indonesia', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Arab-Indonesia'),
('banjar', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Banjar'),
('batak', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Batak'),
('dayak', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Dayak'),
('eropa-indonesia', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Eropa-Indonesia'),
('india-indonesia', 'http://id.wikipedia.org/wiki/Daftar_tokoh_India-Indonesia'),
('jawa', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Jawa'),
('raja jawa', 'http://id.wikipedia.org/wiki/Daftar_raja_Jawa'),
('yogyakarta', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Yogyakarta'),
('surakarta', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Surakarta'),
('minahasa', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Minahasa'),
('minangkabau', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Minangkabau'),
('sunda', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Sunda'),
('tionghoa', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Tionghoa'),

('aceh', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Aceh'),
('sumatra utara', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Sumatera_Utara'),
('sumatra barat', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Sumatera_Barat'),
('bengkulu', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Bengkulu'),
('riau', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Riau'),
('kepulauan riau', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Kepulauan_Riau'),
('jambi', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Jambi'),
('sumatra selatan', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Sumatera_Selatan'),
('lampung', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Lampung'),
('kepulauan bangka belitung', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Kepulauan_Bangka_Belitung'),
('jakarta', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Daerah_Khusus_Ibukota_Jakarta'),
('jawa barat', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Jawa_Barat'),
('banten', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Banten'),
('jawa tengah','http://id.wikipedia.org/wiki/Daftar_tokoh_Jawa_Tengah'),
('jawa timur', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Jawa_Timur'),
('kalimantan barat', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Kalimantan_Barat'),
('kalimantan tengah', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Kalimantan_Tengah'),
('kalimantan selatan', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Kalimantan_Selatan'),
('kalimantan timur', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Kalimantan_Timur'),
('bali', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Bali'),
('nusa tenggara barat', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Nusa_Tenggara_Barat'),
('nusa tenggara timur', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Nusa_Tenggara_Timur'),
('sulawesi barat', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Sulawesi_Barat'),
('sulawesi utara', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Sulawesi_Utara'),
('sulawesi tengah', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Sulawesi_Tengah'),
('sulawesi selatan', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Sulawesi_Selatan'),
('sulawesi tenggara', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Sulawesi_Tenggara'),
('gorontalo', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Gorontalo'),
('maluku', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Maluku'),
('maluku utara', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Maluku_Utara'),
('papua', 'http://id.wikipedia.org/wiki/Daftar_tokoh_Papua')
]

blacklist_token = [
    'daftar', 'tokoh', 'artikel', 'sosiolog',
    'ekonom', 'bisnis', 'profil', 'pamusuk',
    'fky', 'sastrawan', 'pujangga', 'sejarawan',
    'sutradara', 'aktor', '(', '[', 'aktris',
    'penyanyi', 'marga', 'sejarah', 'kota', 'minahasa',
    'mapalus', 'www', 'arab', 'tionghoa', 'eropa',
    'indonesia', 'india'
]

def is_blacklisted(word):
    for token in blacklist_token:
        if word.lower().startswith(token):
            return True
    return False

def grab(tag, url):
    '''
    Grabs people name from wikipedia
    '''
    print "Searching for %s" % tag
    print "-" * 80
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
    return list_people

def get_people():
    result = {}
    for uri in list_uris:
        result[uri[0]] = grab(*uri)
        print '=' * 80
    print 'Dumping...'
    f = open('indonesian_%s.pkl' % datetime.now().strftime('%Y-%m-%d_%H:%M:%S'), 'w')
    pickle.dump(result, f)
    f.close()


if __name__ == '__main__':
    get_people()
