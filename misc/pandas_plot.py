#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # data = 'a,b,c~1,2,3~4,5,6'
    # data = 'Size,Month,Trade~59.9,201612,88000~85.5,201612,99000~'
    headers = ['month', 'size', 'price']
    rc = pd.read_csv('./test.csv', header=None, names=headers)
    rc['month'] = pd.to_datetime(rc['month'])
    plt.plot(rc['month'], rc['price'])
    plt.show()


def sample1():
    nrr = np.random.randn(10)
    print(nrr)
    ts = pd.Series(nrr, index=pd.date_range('1/1/2000', periods=10))
    print(ts.index)
    df = pd.DataFrame(np.random.randn(10, 4), index=ts.index, columns=list('ABCD'))
    print(df)
    # df = df.cumsum()
    df.plot()
    plt.show()


if __name__ == '__main__':
    main()
