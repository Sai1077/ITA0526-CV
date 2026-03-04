import cv2
image = cv2.imread("sample2.jpg")
roi = image[100:300, 100:300]
h, w = roi.shape[:2]
image[0:h, 0:w] = roi
cv2.imshow("Modified Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()