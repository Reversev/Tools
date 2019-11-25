# coding=utf-8

import os
import os.path
import shutil

import numpy as np
from PIL import Image

url = '/media/jie/TOSHIBA EXT/database/moulde_img_origin_1-864_864/new_img/'  # 图片存储的文件夹名称
# classname = ''  # 图片的名字中字符部分
n = 864  # 图片的数量
array = 1 + np.arange(n)  # 产生长度为n的序列
np.random.shuffle(array)  # 将arrray序列随机排列


# 把path文件夹下以及其子文件下的所有.jpg图片移动到new_path文件夹下

# def moveImg(path, new_path):
#     img = Image.open(path)
#     img.save(os.path.join(new_path, os.path.basename(path)))


# 30%的数据生成验证集
new_path1 = '/media/jie/TOSHIBA EXT/database/moulde_img_origin_1-864_864/new_img/val/'
i = 0
while (i<=(int(n * 0.3))):
    # DatasetPath1 = url + classname + str(array[i]) + '.jpg'
    # DatasetPath2 = url + classname + str(array[i]) + '.json'
    DataPath1 = url + str(array[i]) + '.jpg'
    DataPath2 = url + str(array[i]) + '.json'
    print(DataPath2)
    # moveImg(DataPath1, new_path1)
    shutil.move(DataPath1, new_path1)
    shutil.move(DataPath2, new_path1)
    i = i + 1
# 70%的数据生成训练集
new_path2 = '/media/jie/TOSHIBA EXT/database/moulde_img_origin_1-864_864/new_img/train/'
while (i <= n):
    # DatasetPath3 = url + classname + str(array[i]) + '.jpg'
    # DatasetPath4 = url + classname + str(array[i]) + '.json'
    DataPath3 = url + str(array[i]) + '.jpg'
    DataPath4 = url + str(array[i]) + '.json'
    # moveImg(DataPath3, new_path1)
    shutil.move(DataPath3, new_path2)
    shutil.move(DataPath4, new_path2)
    i = i + 1
