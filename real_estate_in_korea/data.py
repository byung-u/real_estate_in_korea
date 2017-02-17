# -*- coding: utf-8 -*-
from real_estate_in_korea.local_code import get_local_code

import re
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime


def request_price(url: str, options) -> int:

    req = urllib.request.Request(url)
    try:
        res = urllib.request.urlopen(req)
    except UnicodeEncodeError:
        return -1

    data = res.read().decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    if (soup.resultcode.string != '00'):
        print('[ERR]', soup.resultmsg.string)
        return -1

    items = soup.findAll('item')
    if options.mode == 0:
        request_trade_price(items, options)
    else:
        request_rent_price(items, options)
    return 0


def request_trade_price(items, options) -> int:
    for item in items:
        item = item.text
        item = re.sub('<.*?>', '|', item)
        info = item.split('|')
        if options.dong is not None and info[4].startswith(options.dong) is False:
            continue
        if options.apt is not None and info[5].find(options.apt) == -1:
            continue
        if options.size != 0.0  and options.size != float(info[8]):
            continue
        ret_msg = '%s %s(%sm²) %s층 %s만원     준공:%s 거래:%s년%s월%s일' % (
                info[4], info[5], info[8], info[11], info[1], 
                info[2], info[3], info[6], info[7])
        #csv_msg = '%s,%s,%s,%s,%s,%s%s%s' % (
        #        info[4], info[5], info[8], info[11], info[1], 
        #        info[3], info[6], info[7][:-3])    
        # info[7][:-3]  1~10 -> 1, 21~31 -> 21
        print(ret_msg)

    return 0


def request_rent_price(items, options) -> int:
    for item in items:
        item = item.text
        item = re.sub('<.*?>', '|', item)
        info = item.split('|')
        # print(info)
        # '2005', '2017', '상암동', '62,000', '상암월드컵파크6단지', 
        # '2', '0', '1~10', '104.32', '1689', 
        #'11440', '4'
        if options.dong is not None and info[3].startswith(options.dong) is False:
            continue
        if options.apt is not None and info[5].find(options.apt) == -1:
            continue
        if options.size != 0.0  and options.size != float(info[9]):
            continue
        ret_msg = '%s %s(%sm²) %s층 %s만원(월세%s)     준공:%s 거래:%s년%s월%s일' % (
                info[3], info[5], info[9], info[12], info[4], info[7],
                info[1], info[2], info[6], info[8])
        print(ret_msg)

    return 0


def get_trade_price(options) -> None:

    local_code = get_local_code(options.gu)
    if local_code == -1:
        print('get_local_code falied, 서울시 %s' % options.gu)
        return

    now = datetime.now()
    year = now.year
    month = now.month

    if options.mode == 0:  # trade
        url = options.trade_url
    else:
        url = options.rent_url

    for i in range(0, options.month_range):
        if (month == 0):
            year -= 1
            month += 12

        time_str = '%4d%02d' % (year, month)
        month = month - 1

        request_url = '%s?LAWD_CD=%s&DEAL_YMD=%s&serviceKey=%s' % (
                url, local_code, time_str, options.svc_key)
        # print(request_url)
        print(time_str)
        ret = request_price(request_url, options)
        if ret != 0:
            print('request_price failed, req_url=%s' % request_url)

    return