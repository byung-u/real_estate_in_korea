#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import re
import urllib.request
from bs4 import BeautifulSoup
import configparser
from datetime import datetime


def _get_trade_price(gu, dong, apt):
    req = urllib.request.Request(url)
    try:
        res = urllib.request.urlopen(req)
    except UnicodeEncodeError:
        return -1

    data = res.read().decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    if (soup.resultcode.string != '00'):
        print('[TEST001][Not OK]\t')
        print('\t', soup.resultmsg.string)
        return -1

    items = soup.findAll('item')
    for item in items:
        item = item.text
        item = re.sub('<.*?>', '|', item)
        info = item.split('|')
        if info[4] != dong:
            continue
        if info[5].find(apt) == -1:
            continue
        ret_msg = '%s %s(%sm²) %s층 %s만원     준공:%s 거래:%s년%s월%s일' % (
                info[4], info[5], info[8], info[11], info[1], info[2], info[3], info[6], info[7])
        print(ret_msg)

    return 0

def get_trade_price(gu='마포', dong='대흥', apt='자이'):
    # TODO 1: module, split
    config = configparser.ConfigParser()
    config.readfp(open('./bot.ini'))
    url = config.get('TOKEN', 'apt_trade_url')
    svc_key = config.get('TOKEN', 'apt_key', raw=True)
    now = datetime.now()
    year = now.year 
    month = now.month

    for i in range(1, 13):
        if (month == 0):
            year -= 1
            month += 12

        time_str = '%4d%02d' % (year, month)
        
    # TODO 2: local code from 'gu' info
        request_url = '%s?LAWD_CD=%s&DEAL_YMD=%s&serviceKey=%s' % (
                url, 11440, time_str, svc_key)
        month = month - 1
        _get_trade_price(request_url, gu, dong, apt)


