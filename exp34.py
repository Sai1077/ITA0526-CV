import numpy as np
import cv2

def create_circle_image(height, width):
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    center = (width // 2, height // 2)
    radius = min(width, height) // 4
    cv2.circle(image, center, radius, (0, 0, 255), 2)
    cv2.imshow("Circle Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

create_circle_image(400, 500)