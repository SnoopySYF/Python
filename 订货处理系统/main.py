#!/usr/bin/env python
#-*- coding:utf-8 -*-
from MySql import(
    getAllCustomers, getAllProducts, getArrears, getInventory, getProductUnit
) 
import datetime

result = getAllCustomers()
print(result)

