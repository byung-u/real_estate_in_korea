#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    info1 = ['2012', '12', '1~10']
    info2 = ['2017', '12', '11~20']
    info3 = ['2016', '1', '21~31']
    print(info1[1], info1[2][:3])
    print(info1[1], info1[2][:-3])
    print('\n\n')
    print(info2[1], info2[2][:-3])
    print(info3[1], info3[2][:-3])


if __name__ == '__main__':
    main()
