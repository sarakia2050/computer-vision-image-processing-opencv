import cv2

img = cv2.imread("images/axx.jpg")

resized = cv2.resize(img, (400, 300))

cropped = img[50:300, 100:400]

cv2.imshow("Resized Image", resized)
cv2.imshow("Cropped Image", cropped)

cv2.imwrite("images/axx_gray.jpg", resized)
cv2.imwrite("images/axx_gray.jpg", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()

