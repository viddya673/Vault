import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

points_A = []

def click_event(event, x, y, flags, param) :
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,'',y)
        font = cv2.FONT_HERSHEY_COMPLEX
        strXY = str(x) + ',' + str(y)
        cv2.putText(img, strXY, (x,y), font, 0.5, (255,255,0), 1 )
        cv2.imshow('image', img)
        z = []
        z.append(x)
        z.append(y)
        points_A.append(z)

inp = input('Enter the image')
img = cv2.imread(inp)
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows

points_A = np.float32(points_A)
points_B = np.float32([[0,0], [420,0], [0,594], [420,594]])

M = cv2.getPerspectiveTransform(points_A, points_B)
 
warped = cv2.warpPerspective(img, M, (420,594))
 
#cv2.imshow('warpPerspective', warped)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

img_grey = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
img_grey = cv2.GaussianBlur(img_grey, (3, 3), 0)
th2 = cv2.adaptiveThreshold(img_grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,3, 2)
cv2.imshow('thresh', th2 )
cv2.waitKey(0)

path = 'C:\Users\Viddya\DIP_Projects\Vault'
cv2.imwrite(os.path.join(path, 'scanned.jpg'), th2)
cv2.waitKey(0)
