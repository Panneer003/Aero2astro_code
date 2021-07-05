import cv2

img = cv2.imread('images/COCO_train2014_000000377417.jpg')
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()