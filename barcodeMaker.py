import numpy as np
import cv2
from random import randint as ri
from random import choice

# print(dir(random.randint))
# print(random.randint(10, 100))

size=1000
square_size=25

arr = np.zeros((size,size,3))
arr[0,0] += 255

for x in range(0,size,square_size):
	for y in range(0,size,square_size):
		writeOrNo = ri(0,3)
		if writeOrNo != 1:
			upOrDown = ri(0,1)
			if upOrDown == 1:
				arr[x+square_size:x+(2*square_size),y:y+square_size] += 255
			else:
				arr[x:x+square_size,y+square_size:y+(2*square_size)] += 255


# for x in range(0,size,square_size):
# 	for y in range(0,size,square_size):
# 		randInt = ri(0,1)
# 		if arr[x-square_size,y].all()==255 or arr[x,y-square_size].all()==255:
# 			arr[x:x+square_size,y:y+square_size] = [255,255,255]
# 		if randInt == 1:
# 			arr[x:x+square_size,y:y+square_size] = [255,255,255]

# cv2.imshow('cool', arr)
# cv2.waitKey(0)
cv2.imwrite('img.jpg', arr)