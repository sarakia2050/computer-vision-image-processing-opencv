import cv2

img = cv2.imread("images/axx.jpg")

cv2.rectangle(img, (50, 50), (250, 250), (0, 255, 0), 3)
cv2.circle(img, (350, 150), 80, (255, 0, 0), 3)
cv2.line(img, (50, 400), (400, 400), (0, 0, 255), 3)

cv2.imshow("Draw Shapes", img)

cv2.imwrite("images/axx_gray.jpg", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

