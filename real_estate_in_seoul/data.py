# -*- coding: utf-8 -*-
from real_estate_in_seoul.local_code import get_local_code

import re
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime


def _get_trade_price(url: str, options) -> int:
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
        if info[4].startswith(options.dong) is False:
            continue
        if info[5].find(options.apt) == -1:
            continue
        ret_msg = '%s %s(%sm²) %s층 %s만원     준공:%s 거래:%s년%s월%s일' % (
                info[4], info[5], info[8], info[11], info[1], info[2], info[3], info[6], info[7])
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

    for i in range(0, options.month_range):
        if (month == 0):
            year -= 1
            month += 12

        time_str = '%4d%02d' % (year, month)
        month = month - 1

        request_url = '%s?LAWD_CD=%s&DEAL_YMD=%s&serviceKey=%s' % (
                options.url, local_code, time_str, options.svc_key)
        # print(request_url)
        ret = _get_trade_price(request_url, options)
        if ret != 0:
            print('_get_trade_price failed, req_url=%s' % request_url)

    return
