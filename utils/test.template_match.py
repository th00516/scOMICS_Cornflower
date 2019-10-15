#!/usr/bin/env python3


import sys
import cv2 as cv
import numpy as np

image = cv.imread(sys.argv[1], cv.IMREAD_GRAYSCALE)
templ = cv.imread(sys.argv[2], cv.IMREAD_GRAYSCALE)

theight, twidth = templ.shape[:2]

templ = cv.convertScaleAbs(templ * (np.mean(image) / np.mean(templ)))

result = cv.matchTemplate(image, templ, method=cv.TM_CCORR_NORMED)
cv.normalize(result, result, 0, 1, cv.NORM_MINMAX, -1)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

image = cv.cvtColor(image, cv.COLOR_GRAY2BGR)

cv.rectangle(image, max_loc, (max_loc[0] + twidth, max_loc[1] + theight), (0, 255, 0), 2)

cv.imwrite('debug.tif', image)
