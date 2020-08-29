#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'
"""
    预处理-去除干扰线和点
    不同的结构元素中选择
    Image和numpy array相互转换
    识别(OCR)和输出
"""
import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract as tess


def recognize_text(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    # cv.imshow("binary", binary)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    # kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 1))
    # open_out = cv.morphologyEx(bin1, cv.MORPH_OPEN, kernel)
    cv.imshow("binary-image", bin1)

    # cv.bitwise_not(open_out, open_out)
    textImage = Image.fromarray(bin1)
    text = tess.image_to_string(textImage)
    # text = tess.image_to_string(textImage)
    print("result: ", text)


print("--------------Hello Python ------------")
src = cv.imread("./images/23_line2.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
recognize_text(src)
cv.waitKey(0)   # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()

