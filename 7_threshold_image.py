import cv2

img = cv2.imread("images/axx.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Threshold Image", threshold)

cv2.imwrite("images/axx_gray.jpg", threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()

