from PIL import Image
import sys
import os
import re
import glob
import numpy as np
import cv2

def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None

def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

# for i in range(16):
#     files = glob.glob(f'datas/major_org/{i}/*.png')
#     for f in files:
#         img = imread(f, cv2.IMREAD_UNCHANGED)
#         for y in range(img.shape[0]):
#             for x in range(img.shape[1]):
#                 if img[y, x, 3] == 0:
#                     img[y, x] = [255, 255, 255, 255]

#         # jpg保存をもってアルファチャンネル削除に替える
#         imwrite(f[:-4]+'.jpg', img)


files = glob.glob(f'datas/tests/*.png')
for f in files:
    img = imread(f, cv2.IMREAD_UNCHANGED)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if img[y, x, 3] == 0:
                img[y, x] = [255, 255, 255, 255]

    # jpg保存をもってアルファチャンネル削除に替える
    imwrite(f[:-4]+'.jpg', img)
