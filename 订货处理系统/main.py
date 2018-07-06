#!/usr/bin/env python
#-*- coding:utf-8 -*-
from MySql import(
    getAllCustomers, getAllProducts, getArrears, getInventory, getProductUnit
) 

results = getProductUnit("02")
print(results)
