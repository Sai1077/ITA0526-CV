import cv2

def segment_image(image_path, threshold_value=127):
    image = cv2.imread("sample1.jpg", 0)
    _, segmented = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    cv2.imshow("Original Image", image)
    cv2.imshow("Segmented Image", segmented)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

segment_image("input_image.jpg", 127)