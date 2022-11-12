

# find all bmp images in labels_generated folder
# for each image resize y axis by 1.5 times and overwrite the image

import os
import cv2
import numpy as np

# get all bmp files in labels_generated and subfolders
bmp_files = []

for root, dirs, files in os.walk("labels_generated"):
    for file in files:
        if file.endswith(".bmp"):
             bmp_files.append(os.path.join(root, file))
print(len(bmp_files))
# resize each bmp file
for bmp_file in bmp_files:
    img = cv2.imread(bmp_file, cv2.IMREAD_UNCHANGED)
    print(img.shape)
    img = cv2.resize(img, (0,0), fx=1, fy=1.5)
    print(img.shape)
    cv2.imwrite(bmp_file, img)