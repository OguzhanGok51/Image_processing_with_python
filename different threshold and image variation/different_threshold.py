
import cv2 as cv

img=cv.imread("GAME.jpg",0)
_, th1=cv.threshold(img,50,255,cv.THRESH_BINARY)
_, th2=cv.threshold(img,150,255,cv.THRESH_BINARY_INV)
_, th3=cv.threshold(img,80,255,cv.THRESH_TRUNC)
_, th4=cv.threshold(img,200 ,255,cv.THRESH_TOZERO)

th6=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,21,2)



cv.imshow("image",img)
cv.imshow("th1",th1)
cv.imshow("th2",th2)
cv.imshow("th3",th3)
cv.imshow("th4",th4)
cv.imshow("th6",th6)

cv.waitKey(0)
cv.destroyAllWindows()
