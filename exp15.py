import cv2
import numpy as np
image = cv2.imread("sample3.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
harris = cv2.cornerHarris(gray, 2, 3, 0.04)
harris = cv2.dilate(harris, None)
result = image.copy()
result[harris > 0.01 * harris.max()] = [0,0,255]
cv2.imshow("Original Image", image)
cv2.imshow("Harris Corners", result)
cv2.imwrite("harris_corners.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()