import cv2

# Load an image using 'imread' specifying the path to image
# cv2.IMREAD_COLOR - Load a color image (default)

img = cv2.imread("D:\\Luminar\DL\\Open-cv\\image.png")


converted_img = cv2.resize(img,(300,300))


print(converted_img.shape)
# greyscale image
img_grey = cv2.cvtColor(converted_img,cv2.COLOR_BGR2GRAY)



# binary image
thresh,bin_img = cv2.threshold(img_grey,120,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)


# cv2.rectangle(img,pt1=(300,400),pt2=(200,300),color=(0,0,255),thickness=5)

# cv2.circle(img,center=(300,300),radius=100,color=(0,255,0),thickness=cv2.FILLED)


# cv2.imwrite("D:\\Luminar\DL\\Open-cv\\binary_image.png",img)

# Text
cv2.putText(img,
            text="Hello....",
            org=(100,250),
            fontFace=cv2.FONT_HERSHEY_DUPLEX        ,
            fontScale=1,color=(0,255,0),
            thickness=2)


print(thresh)

# Display the image using 'imshow'
cv2.imshow("Binary Image",img)
cv2.waitKey()
cv2.destroyAllWindows()