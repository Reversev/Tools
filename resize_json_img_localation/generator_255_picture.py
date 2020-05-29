#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/5/22 15:12
# @Author ：''
# @FileName: generator_255_picture.py
"""
    只是一个简单的单一像素图像的生成手段
"""

import cv2
import numpy as np


def gen_pic(img_size, picture_name):
    img = np.ones(img_size, dtype=np.uint8)
    cv2.imwrite(picture_name, img)

    print('生成文件目录：', picture_name)
    print('Finish generator process!!!')


if __name__ == '__main__':
    file_name = './mother_picture.jpg'
    imgsize = (1024, 1280)
    gen_pic(imgsize, file_name)
