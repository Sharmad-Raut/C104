import cv2
img=cv2.imread("butterfly.jpg")
cv2.imshow("butterflyImage",img)

cv2.waitKey(100)

grayImage=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("butterflyImage(2)",grayImage)

cv2.waitKey(1)

print(img)