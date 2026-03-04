import cv2

watch_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

image = cv2.imread("watch.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

watches = watch_cascade.detectMultiScale(gray, 1.1, 5)

for (x, y, w, h) in watches:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Detected Object", image)
cv2.waitKey(0)
cv2.destroyAllWindows()