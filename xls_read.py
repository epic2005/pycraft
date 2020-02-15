#!/usr/bin/python
# -*- coding: utf-8 -*-

# read from api

from pyExcelerator import *
sheets = parse_xls('./xls/vms.xls')

print sheets[0][1][(0, 0)]
print sheets[0][1][(0, 1)]
print sheets[0][1][(0, 2)]

print sheets[0][1][(1, 0)]
print sheets[0][1][(2, 0)]
print sheets[0][1][(3, 0)]
