import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread("BMW.png")
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

kernel=np.ones((5,5),np.float32)/25
dst=cv.filter2D(img,-1,kernel)
blur=cv.blur(img,(5,5))

titles=["image","2D Convolution","blur"]
images=[img,dst,blur]

for i in range(3):
    plt.subplot(1,3,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

