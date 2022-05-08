from tkinter import *
import cv2
import numpy as np


def callback_val(x):
    pass

cv2.namedWindow("Term project")
cv2.createTrackbar("LH","Term project",0,255,callback_val)
cv2.createTrackbar("LS","Term project",0,255,callback_val)
cv2.createTrackbar("LV","Term project",0,255,callback_val)
cv2.createTrackbar("UH","Term project",255,255,callback_val)
cv2.createTrackbar("US","Term project",255,255,callback_val)
cv2.createTrackbar("UV","Term project",255,255,callback_val)
cv2.createTrackbar("TH","Term project",0,255,callback_val)

window= Tk()


window.geometry("1000x1000")
window.title("Term project")

b1=Button(window,text="Apply Threshold",width=25,bg="red",fg="black")
b1.place(x=800,y=200)

b2=Button(window,text="Calculate for region 1",width=25,bg="blue",fg="black")
b2.place(x=800,y=300)

b3=Button(window,text="Calculate for region 2",width=25,bg="blue",fg="black")
b3.place(x=800,y=400)

b4=Button(window,text="Calculate for region 3",width=25,bg="blue",fg="black")
b4.place(x=800,y=500)

label =Label(window)
label.grid(row=0, column=0)


cap= cv2.VideoCapture(0)


while True:
      _,frame=cap.read()
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

      cv2.imshow("region1", th1)
      cv2.imshow("region2", th2)
      cv2.imshow("region3", th3)

      key = cv2.waitKey(1)
      if key == 27:
          break
cap.release()
cv2.destroyAllWindows()


window.mainloop()

