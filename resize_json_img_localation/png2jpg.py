#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/5/22 15:34
# @Author ：''
# @FileName: png2jpg.py
import os
from PIL import Image


def png2jpg():
    dirname_read = "/home/ir/Desktop/resize_json_img/new_png/"
    dirname_write = "/home/ir/Desktop/resize_json_img/new_jpg/"
    names = os.listdir(dirname_read)
    count = 0
    for name in names:
        img = Image.open(dirname_read + name)
        name = name.split(".")
        if name[-1] == "png":
            name[-1] = "jpg"
            name = str.join(".", name)
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
            to_save_path = dirname_write + name
            # cv2.imwrite(to_save_path, img)
            img.save(to_save_path)
            count += 1
            print(to_save_path, "------conut：", count)
        else:
            continue
