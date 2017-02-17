# -*- coding: utf-8 -*-
import sqlite3


def local_code_db_create() -> None:
    conn = sqlite3.connect('local_code.db')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS local_code (
    "code" integer NOT NULL,
    "province" text,
    "district" text)''')
    conn.commit()

    query = 'SELECT * FROM local_code'
    c.execute(query)
    data = c.fetchone()
    if data is not None:
        # print('local_code already exist')
        return

    insert_local_code(c, conn)
    conn.close()
    return


def insert_local_code(c, conn) -> None:
    local_info = []
    with open('./data/loc_code.txt') as f:
        for line in f:
            local_info = line.split()
            query = 'INSERT INTO local_code VALUES (%s, "%s", "%s")' % (
                    local_info[0], local_info[1], local_info[2])
            print(query)
            c.execute(query)

    conn.commit()


def get_local_code(gu) -> int:
    conn = sqlite3.connect('local_code.db')
    c = conn.cursor()

    if (gu.endswith('구')):  # 강남구
        query = '''SELECT code FROM local_code WHERE
        province='서울특별시' and district="%s"''' % (gu)
    else:  # 강남
        query = '''SELECT code FROM local_code WHERE
        province='서울특별시' and district="%s구"''' % (gu)

    c.execute(query)
    data = c.fetchone()
    if data is not None:
        conn.close()
        return int(data[0])
    else:
        # retry
        if (gu.endswith('구')):  # 서현구
            query = '''SELECT code FROM local_code WHERE district="%s"''' % (gu)
        else:  # 강남
            query = '''SELECT code FROM local_code WHERE district="%s구"''' % (gu)

        c.execute(query)
        data = c.fetchone()
        if data is not None:
            conn.close()
            return int(data[0])
        else:
            print('[ERR]', data)
            conn.close()
            return -1
