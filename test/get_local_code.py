#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import sqlite3


def main():
    conn = sqlite3.connect('../local_code.db')
    c = conn.cursor()
    gu = '마포'
    query = '''SELECT code FROM local_code WHERE
    province='서울특별시' and district="%s구"''' % (gu)

    c.execute(query)
    data = c.fetchone()
    conn.close
    print(int(data[0]))


if __name__ == '__main__':
    main()
