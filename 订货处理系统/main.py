#!/usr/bin/env python
#-*- coding:utf-8 -*-
from MySql import(
    getAllCustomers, getAllProducts, getArrears, getInventory, getProductUnit
) 
import datetime

def day_count(order_num='1997-9-9',owe_num='1997-7-7'):#计算欠款天数 订货时间 欠款时间
    temp=order_num.split('-')
    order_year=int(temp[0])
    order_month=int(temp[1])
    order_day=int(temp[2])
    temp = owe_num.split('-')
    owe_year = int(temp[0])
    owe_month = int(temp[1])
    owe_day = int(temp[2])
    date1=datetime.datetime(order_year,order_month,order_day)
    date2 = datetime.datetime(owe_year, owe_month, owe_day)
    print(date1-date2)
    return date1-date2

def provide(ifowe=True,order_num=100,store_num=100):#判定发货 是否欠款 订货数量 库存数量
    if ifowe==False:
        if order_num>store_num:
            print('先按库存发货进货再补发')
        else:
            print('立即发货')
    day_num=day_count().days#欠款天数
    if day_num<=30:
        if order_num<=store_num:
            print('立即发货')
        else:
            print('先按库存发货进货再补发')
    if 30<day_num<100:
        if order_num<=store_num:
            print('先付款再发货')
        else:
            print('不发货')
    if day_num>=100:
        if order_num <= store_num:
            print('通知先付款')
        else:
            print('通知先付款')

