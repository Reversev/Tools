#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author = 'IReverser'

import cv2 as cv
import numpy as np


# 模板匹配，就是在整个图像区域发现与给定子图像匹配的小块区域，
# 需要模板图像T和待检测图像-源图像S
# 工作方法：在待检测的图像上，从左到右，从上倒下计算模板图像与重叠子图像匹配度，
# 匹配度越大，两者相同的可能性越大。
def template_demo():
    tpl = cv.imread("./images/11_2.jpg")
    target = cv.imread("./images/11_1.jpg")
    cv.imshow("template image", tpl)
    cv.imshow("target image", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCOEFF_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0] + tw, tl[1] + th)
        cv.rectangle(target, tl, br, (0, 0, 255), 2)
        cv.imshow("match-"+np.str(md), target)
        cv.imshow("result-"+np.str(md), result)
        cv.imwrite("./images/result11.png", target)


print("--------------Hello Python ------------")
src = cv.imread("./images/demo.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
template_demo()
cv.waitKey(0)  # 等有键输入或者1000ms后自动将窗口消除，0表示只用键输入结束窗口

cv.destroyAllWindows()
