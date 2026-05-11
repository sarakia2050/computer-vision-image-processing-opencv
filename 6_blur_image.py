import cv2

img = cv2.imread("images/axx.jpg")

blur = cv2.GaussianBlur(img, (15, 15), 0)

cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blur)

cv2.imwrite("images/axx_gray.jpg", blur)

cv2.waitKey(0)
cv2.destroyAllWindows

