import cv2

read_image=cv2.imread("poster.jpg")

#cv2.imshow("read_image1",read_image)

rocket=read_image[120:360,400:500]

#cv2.imshow("rocket1",rocket)

read_image[0:240,500:600]=rocket


cv2.putText(read_image,"I LOVE CODING",(20,220),color=(0,255,0), fontScale=1,fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)

cv2.imshow("read_image2",read_image)

cv2.waitKey(0)