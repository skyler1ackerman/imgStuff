import numpy as np
import cv2
from random import randint as ri
from random import choice

# print(dir(random.randint))
# print(random.randint(10, 100))

size=1000
square_size=1

arr = np.zeros((size,size,3))	

for x in range(0,size,square_size):
	for y in range(0,size,square_size):
		colorArr = [255-x*255/size, 255-y*255/size, (x+y)*255/(2*size)]
		arr[x:x+square_size,y:y+square_size] = colorArr
		# square_size+=1


# cv2.imshow('thing', arr)
# cv2.waitKey(0)

cv2.imwrite('img.jpg', arr)