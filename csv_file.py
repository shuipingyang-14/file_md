# -*- coding:utf-8 -*-
import csv

# 读取本地csv文件
with open('login_test.csv', 'r+', encoding='utf-8') as csv_file:
    data = [each for each in csv.DictReader(csv_file)]

print(data)