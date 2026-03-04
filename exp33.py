import numpy as np
import cv2

def create_rectangle_image(height, width):
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    top_left = (width // 4, height // 4)
    bottom_right = (3 * width // 4, 3 * height // 4)
    cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)
    cv2.imshow("Rectangle Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

create_rectangle_image(400, 500)