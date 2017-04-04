#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import cv2
import numpy as np
# reading the source image path

img = cv2.imread("C:\Users\Mahesh\Desktop\999.jpg")

# reading the co-ordinates from the user

mat_x=[[600,500],[200,400],[600,504],[717,207]]

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
gray = cv2.GaussianBlur(gray, (5, 5), 0)
_, bin = cv2.threshold(gray,120,255,1) # inverted threshold (light obj on dark bg)
bin = cv2.dilate(bin, None)  # fill some holes
bin = cv2.dilate(bin, None)
bin = cv2.erode(bin, None)   # dilate made our shape larger, revert that
bin = cv2.erode(bin, None)
bin, contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
a=[]
b=[]
rc = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(rc)

for p in box:
    pt =(p[0],p[1])
    print pt
    i=0
    a.append(int(p[0]))
    b.append(int(p[1]))
    print [a,b]
    i=i+1
    #cv2.circle(img,pt,5,(200,0,0),2)
# a list contain x-co-ordinates of source image
# b list contain y-co-ordinatesof source image

pts1 =np.float32([[a[0],b[0]],[a[1],b[1]],[a[2],b[2]],[a[3],b[3]]])
#pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 =np.float32([[mat_x[0],mat_x[1],mat_x[2],mat_x[3]]])


M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(1000,1000))

#M = cv2.getAffineTransform(pts1,pts2)

#dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('plank',dst)
cv2.waitKey()


