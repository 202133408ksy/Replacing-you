import cv2
img_gray = cv2.imread('C:/test.jpg',0) # gray 사진 읽기
img_color = cv2.imread('C:/test.jpg',1) # color 사진 읽기

cv2.imshow('gray', img_gray)
cv2.imshow('color', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
