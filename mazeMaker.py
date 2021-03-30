import numpy as np
import cv2
from random import randint as ri
from random import choice

# print(dir(random.randint))
# print(random.randint(10, 100))

size=500
square_size=25
pad = 2

arr = np.zeros((size,size,3))

def deleteRightWall(x,y):
	arr[x+pad:x+square_size-pad,y+pad:y+square_size+pad] = [255,255,255]

for x in range(0,size,square_size):
	for y in range(0,size,square_size):
		arr[x+pad:x+square_size-pad,y+pad:y+square_size-pad] = [ri(0,255),ri(0,255),ri(0,255)]

# deleteRightWall(0,0)
# cv2.imshow('Cool', arr)
# cv2.waitKey(0)

cv2.imwrite('img.jpg', arr)