import numpy as np
import cv2
from random import randint as ri
from random import choice
import random
# print(dir(random.randint))
# print(random.randint(10, 100))

size=500
square_size=25
pad = 2

arr = np.zeros((size,size,3))
for x in range(0,size,square_size):
	for y in range(0,size,square_size):
		colorArr = [255-x*255/size, 255-y*255/size, (x+y)*255/(2*size)]
		arr[x+pad:x+square_size-pad,y+pad:y+square_size-pad] = colorArr

# cv2.imshow('Cool', arr)
# cv2.waitKey(0)
arr = np.flip(arr)
# arr = random.shuffle(arr)
print(dir(np))

# cv2.imwrite('img.jpg', arr)