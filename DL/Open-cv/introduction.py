import cv2


img = cv2.imread("D:\\Luminar\DL\\Open-cv\\image.png")


cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()