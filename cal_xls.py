#!/usr/bin/python
# -*- coding: utf-8 -*-

# read from api

from pyExcelerator import *
from collections import defaultdict


def read_sku():
    book = parse_xls('./xls/vms.xls')
    parsed_dictionary = defaultdict(lambda: '', book[0][1])
    number_of_columns = 44
    number_of_rows = 500000
    result_list = [] * number_of_rows

    for i in range(0, number_of_rows):
        tag = False
        result_list.append([])
        for h in range(0, number_of_columns):
            item = parsed_dictionary[i, h]
            if type(item) is StringType or type(item) is UnicodeType:
                item = item.replace("\t", "").strip()
            result_list[i].append(item)
            if item != '':
                tag = True
        if not tag:
            break


if __name__ == "__main__":
    read_sku()
