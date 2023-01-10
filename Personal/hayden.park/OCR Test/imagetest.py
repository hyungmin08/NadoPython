from re import X
import cv2
from pytesseract import *
import numpy as np

src = cv2.imread(r"C:\Users\ParkHM\Desktop\Test\342 60.JPG", cv2.IMREAD_GRAYSCALE)
# src = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
alpha = 3
src1 = np.clip((1+alpha) * src - 128 * alpha, 0, 255).astype(np.uint8)



# dst = src[205:448, 725:1125].copy()
x=0
x_start = 725
x_d = 100
y=0
y_start = 204
y_d = 22
row_count = 11
col_count = 4
multiple = 2

y = y_start
for i in range(0,row_count):
    x = x_start
    for j in range(0,col_count):
        dst = src1[y:y+y_d, x:x+x_d].copy()
        x +=x_d
        image = cv2.resize(dst,(0,0),fx=multiple, fy=multiple, interpolation=cv2.INTER_LINEAR)

        
        text = image_to_string(image,lang="eng",config='--psm 1 -c preserve_interword_spaces=1')
        print(text)
        cv2.imshow("dst", image)
        cv2.waitKey()
        
    y += y_d
    

    
    
    