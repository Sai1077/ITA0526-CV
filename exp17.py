import cv2
image = cv2.imread("sample1.jpg")
overlay = image.copy()
cv2.putText(overlay, "SIMATS Engineering", (50, image.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
watermarked = cv2.addWeighted(overlay, 0.7, image, 0.3, 0)
cv2.imshow("Watermarked Image", watermarked)
cv2.imwrite("watermarked_image.jpg", watermarked)
cv2.waitKey(0)
cv2.destroyAllWindows()