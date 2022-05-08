import cv2

import numpy as np  
from tkinter import *  
from tkinter import ttk


def callback_val(x):
    pass


cap=cv2.VideoCapture(0)

cv2.namedWindow("Term project")
cv2.createTrackbar("LH","Term project",0,255,callback_val)
cv2.createTrackbar("LS","Term project",0,255,callback_val)
cv2.createTrackbar("LV","Term project",0,255,callback_val)
cv2.createTrackbar("UH","Term project",255,255,callback_val)
cv2.createTrackbar("US","Term project",255,255,callback_val)
cv2.createTrackbar("UV","Term project",255,255,callback_val)
cv2.createTrackbar("TH","Term project",0,255,callback_val)

while True:
    _, frame=cap.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Term project")
    l_s = cv2.getTrackbarPos("LS", "Term project")
    l_v = cv2.getTrackbarPos("LV", "Term project")
    u_h = cv2.getTrackbarPos("UH", "Term project")
    u_s = cv2.getTrackbarPos("US", "Term project")
    u_v = cv2.getTrackbarPos("UV", "Term project")
    th_val = cv2.getTrackbarPos("TH", "Term project")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    th = np.array([th_val])

    _, th1 = cv2.threshold(frame, th_val, 255, cv2.THRESH_TRUNC)
    _, th2 = cv2.threshold(frame, th_val, 255, cv2.THRESH_TRUNC)
    _, th3 = cv2.threshold(frame, th_val, 255, cv2.THRESH_TRUNC)

    cv2.imshow("region1",th1)
    cv2.imshow("region2", th2)
    cv2.imshow("region3", th3)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()

root=Tk()  

root.title("Term Project")  
ttk.Label(root, text="Separating widget").pack()  
cap=cv2.VideoCapture(0)


panedwindow=ttk.Panedwindow(root, orient=HORIZONTAL)  
panedwindow.pack(fill=BOTH, expand=True)  

fram1=ttk.Frame(panedwindow,width=100,height=300, relief=SUNKEN)  
fram2=ttk.Frame(panedwindow,width=400,height=400, relief=SUNKEN)
fram3=ttk.Frame(panedwindow,width=200,height=200, relief=SUNKEN)  
  
panedwindow.add(fram1, weight=1)  
panedwindow.add(fram2, weight=4)  
panedwindow.add(fram3, weight=4)  


root.mainloop()  


cap.release()
cv2.destroyAllWindows()


