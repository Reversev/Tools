#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2021/8/1 23:37
# @Author : 'IReverser'
# @FileName: chance_labels.py
"""
    the script usd to chance labels for yolo dataset format
"""
import glob
import os

if __name__ == '__main__':
    txt_path = './ /'
    target_path = './  /'
    origin_name = ''
    changed_name = ''
    for file_name in glob.glob(txt_path + '*.txt'):
        with open(file_name) as f:
            data = f.readlines()
            for i in range(len(data)):
                data[i].replace(origin_name, changed_name)
        if not os.path.exists(target_path + file_name):
            os.mkdir(target_path + file_name)
        with open(target_path + file_name) as p:
            p.writelines(data)
