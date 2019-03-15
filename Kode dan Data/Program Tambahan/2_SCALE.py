import os
import cv2
from os import listdir
from scipy import misc

for digit in range(0,10):
    os.chdir(str(digit))
    path = os.getcwd()
    i = 5000
    for f in listdir(path):
        print (digit, f)
        img = cv2.imread(f)
        for x in range(0,21):
            ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
            constant= cv2.copyMakeBorder(thresh,x,0,0,x,cv2.BORDER_CONSTANT,255)
            constant = misc.imresize(constant, (30, 20))
            constant = cv2.cvtColor(constant, cv2.COLOR_BGR2GRAY)
            ret,thresh1 = cv2.threshold(constant,127,255,cv2.THRESH_BINARY_INV)
            cv2.imwrite("../" + str(digit) + "_" + str(i) + ".png", thresh1)
            i += 1
    os.chdir("../")
#30x24