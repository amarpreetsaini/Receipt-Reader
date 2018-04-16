import cv2
from matplotlib import pyplot as plt
import numpy as np

try:
    import Image
except ImportError:
    from PIL import Image
from pytesseract import pytesseract

path = 'rgb_dst.png'

image_obj = cv2.imread(path)

gray = cv2.cvtColor(image_obj, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

kernel = np.ones((5,5), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
img_erosion = cv2.erode(img_dilation, kernel, iterations=1)

cv2.imwrite('thresh.png', thresh)
cv2.imwrite('img_dilation.png', img_dilation)
cv2.imwrite('img_erosion.png', img_erosion)
# Now finding Contours         ###################
hierarchy, contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

coordinates = []    
for cnt in contours:
    print(cnt)
    [x, y, w, h] = cv2.boundingRect(cnt)
    cv2.rectangle(image_obj, (x, y), (x+w, y+h), (255,0,0), 2)

cv2.imwrite('contours.png', image_obj)