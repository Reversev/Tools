# -*- coding: utf-8 -*-
# author = 'IReverser'

import os
import io
import json

import cal_IoU as cI

source_path = 'H:\\data\\train_single\\'
# print(file_name(source_path))
for name in enumerate(cI.file_name(source_path)):

    data_label_len = 8   # 检测的特定的label长度
    m_path = name[1]
    dir = os.path.dirname(m_path)
    file_json = io.open(m_path, 'r', encoding='utf-8')
    json_data = file_json.read()
    data = json.loads(json_data)
    # print(data)
    data_label = data['shapes']
    for i in range(0, len(data_label)):
        # print(len(data_label))
        # print(data_label[i])
        find_labeling = data_label[i]
        # print(find_labeling)
        find_label = find_labeling['label']
        # print(find_label)
        if len(find_label) == data_label_len:
            # print(i)
            # print(find_labeling)
            line1 = find_labeling['points']   # 四边形四个点坐标的一维数组表示，[x,y,x,y....]
            # print(find_labeling['points'])

            line1[:] = cI.multi_array2array(line1)

            # 识别后的坐标存在line2数组里面
            line2 = [923, 308, 758, 342, 741, 262, 907, 228]

            value = cI.cal_IoU(line1, line2)
            print(value)

