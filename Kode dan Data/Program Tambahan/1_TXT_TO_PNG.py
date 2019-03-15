import numpy as np
import cv2

namainput = "hir001.txt"
namaoutput = "hir001.png"
img = np.empty((20, 40))
inp = open(namainput,'r')
x = 0
for line in inp:
    y = 0
    for l in line:
        if l == '.':
            img[x][y]=255
        elif l == 'X':
            img[x][y]=1
        y +=1
    x+=1
print (img)
cv2.imwrite(namaoutput, img);