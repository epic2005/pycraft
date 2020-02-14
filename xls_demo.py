#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyExcelerator import *


def write_price():
    w = Workbook()  # 创建一个工作簿
    ws = w.add_sheet('Hey, Hades')  # 创建一个工作表

    ws.write(0, 0, 'bit')  # 在1行1列写入bit
    ws.write(0, 1, 'huang2')  # 在1行2列写入huang
    ws.write(1, 0, 'xuan3')  # 在2行1列写入xuan

    w.save('mini.xls')


if __name__ == "__main__":
    write_price()
