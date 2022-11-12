# convert files in current dir to greyscale using cv2
import cv2
import os

"""files = os.listdir()


for file in files:
    if file.endswith(".bmp"):
        image = cv2.imread(file)
        print(image.shape)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # copy of image
        image_copy = image.copy()
        cv2.imwrite(file, image_copy)
"""

img = cv2.imread("100_pixels_Cherries,25,19-08-2022,18-13-50,pass.bmp", cv2.IMREAD_GRAYSCALE)
a = img.shape
print(a)
cv2.imshow("image", img)
cv2.waitKey(0)