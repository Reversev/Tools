#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/5/22 16:46
# @Author ：''
# @FileName: resize_json.py
# -*- coding: utf-8 -*-
import io
import json
import os
import time

import cv2
import math
import numpy as np


def resize_json():
    source_path = '/home/ir/Desktop/resize_json_img/new_jpg'
    destination_source_path = '/home/ir/Desktop/resize_json_img/resize'
    destination_path = destination_source_path

    article_info = {}
    data_json = json.loads(json.dumps(article_info, indent=4))
    print(data_json)
    data_json['version'] = '3.16.7'
    data_json['flags'] = {}
    data_json["lineColor"] = [
        0,
        255,
        0,
        128
    ]
    data_json["fillColor"] = [
        255,
        0,
        0,
        128
    ]


    def file_name(file_dir):
        L = []
        for root, dirs, files in os.walk(file_dir):
            # print(files)
            for file in files:
                # print(file)
                if os.path.splitext(file)[1] == '.json':
                    L.append(os.path.join(root, file))
            return L


    if not os.path.isdir(destination_path):
        os.mkdir(destination_path)
    print(destination_path)
    t_3 = time.time()
    print(file_name(source_path))
    for name in enumerate(file_name(source_path)):
        shape_json = []
        m_path = name[1]
        dir = os.path.dirname(m_path)
        file_json = io.open(m_path, 'r', encoding='utf-8')
        json_data = file_json.read()
        data = json.loads(json_data)
        data_json['imageData'] = None

        data_name = m_path.split('/')[-1].split('.')[0] + '.jpg'
        # data_name = data['imagePath']

        data_path = dir + '/' + data_name
        object_name = os.path.splitext(data['imagePath'])[0]
        for i in range(len(data['shapes'])):
            point = np.array([])
            if len(data['shapes'][i]['points']) != 4:
                print(object_name + '.jpg has more than 4 points')
                print(data['shapes'][i]['label'])
                continue
            for j in range(0, 4):
                point = np.append(point, data['shapes'][i]['points'][j][0])
                point = np.append(point, data['shapes'][i]['points'][j][1])
            m_name_0 = data['shapes'][i]['label']
            data_json_line_color = data['shapes'][i]['line_color']
            data_json_fill_color = data['shapes'][i]['fill_color']
            print(point)
            img = cv2.imread(data_path)
            (filename, extension) = os.path.splitext(data_name)
            data_new_picture_name = destination_path + "/" + filename + ".jpg"
            data_new_json_name = destination_path + "/" + filename + ".json"
            data_json['imagePath'] = filename + ".jpg"
            shape_json_item = {"label": m_name_0,
                               "line_color": data_json_line_color,
                               "fill_color": data_json_fill_color,
                               "points": [[point[0] + 128, point[1] + 362],
                                          [point[2] + 128, point[3] + 362],
                                          [point[4] + 128, point[5] + 362],
                                          [point[6] + 128, point[7] + 362]]
                               }
            shape_json.append(shape_json_item)
        data_json['shapes'] = shape_json
        data_info = json.dumps(data_json, ensure_ascii=False, indent=2)
        fp = open(data_new_json_name, "w+")
        fp.write(data_info)
        fp.close()
    t_4 = time.time()
    print('t_cost: ', t_4 - t_3, 'sec')
    exit()
