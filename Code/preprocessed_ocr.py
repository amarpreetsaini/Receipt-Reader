import cv2
from matplotlib import pyplot as plt
import numpy as np

try:
	import Image
except ImportError:
	from PIL import Image
from pytesseract import pytesseract

file = 'Receipts/20180413_225050.jpg'

img = cv2.imread(file,0)

img_not = cv2.bitwise_not(img)
cv2.imwrite('out_not.png',img_not)

cv2.imwrite('out1.png',img)
#canny = cv2.Canny(img_not, 100, 200)
kernel = np.ones((5,5), np.uint8)

#img_erosion = cv2.erode(img, kernel, iterations=2)
img_dilation = cv2.dilate(img_not, kernel, iterations=1)

canny = cv2.Canny(img_dilation, 100, 200)

im2, contours, hierarchy  = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#cnts = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
print(len(contours))
for cnt in contours:
	cv2.drawContours(im2, [cnt], 0, (0,255,0), 3)

	# cv2.drawContours(im2,contours,-1,(0,255,0),3)
# cv2.imshow("Keypoints", im2)
# cv2.waitKey(0)

#cv2.drawContours(img, contours, -1, (0,255,255), 3)
# cnt = contours[4]
# img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
#cv2.imwrite('canny.png',canny)
# cv2.imwrite('img_dilation.png',img_dilation)
cv2.imwrite('contours.png',im2)

# titles = ['Original Image', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding','otsu']

# images = [img, th2, th3, thr4]

# for i in range(4):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()