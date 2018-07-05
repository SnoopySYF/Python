#!/usr/bin/env python
#-*- coding:utf-8 -*-
from MySql import(
    getAllCustomers, getAllProducts, getArrears, getInventory
) 

results = getAllCustomers()
print(results)
