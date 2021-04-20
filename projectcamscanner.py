import cv2
import numpy as np

#############################################
widthimg = 640
hieghtimg = 480
#############################################

cap = cv2.VideoCapture(0)
cap.set(3,widthimg)
cap.set(4,hieghtimg)
cap.set(10,130)


def preprocessing(img):
    imggry = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgblur= cv2.GaussianBlur(imggry,(5,5),1)
    imgcanny = cv2.Canny(imgblur,200,200)
    kernel = np.ones((5,5))
    imgdail=cv2.dilate(imgcanny,kernel,iterations=2)
    imgthres=cv2.erode(imgdail,kernel,iterations=1)


    return imgthres


def getcontours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgcontour,cnt,-1,(255,0,0),3)
            peri=cv2.arcLength(cnt,True)
            #print(peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objcor=len(approx)
            x, y, w, h = cv2.boundingRect(approx)



while True:
    success, img = cap.read()
    cv2.resize(img,(widthimg,hieghtimg))
    imgthres = preprocessing(img)
    cv2.imshow("result",imgthres)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break