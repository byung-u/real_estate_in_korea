#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import sqlite3


def main():
    local_info = []
    with open('../data/loc_code.txt') as f:
        for line in f:
            local_info = line.split()
            print(local_info)
            #query = 'INSERT INTO local_code VALUES (%s, "%s", "%s")' % (
            #        local_info[0], local_info[1], local_info[2])
            #print(query)

if __name__ == '__main__':
    main()
