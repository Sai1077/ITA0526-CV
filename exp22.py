import cv2
import numpy as np
image = cv2.imread("sample1.jpg", 0)
kernel = np.ones((5,5), np.uint8)
closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Original Image", image)
cv2.imshow("Closed Image", closed)
cv2.waitKey(0)
cv2.destroyAllWindows()