import cv2
import numpy as np

black=np.zeros([600,600])

black[200:400,200:400]=255

cv2.imshow("blackImage",black)

cv2.waitKey(0)

print(black)