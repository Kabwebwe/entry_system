import cv2 as cv
import numpy as np
import test_p as tp

def nothing(x):
	pass



cap = cv.VideoCapture('http://192.168.230.126:8080/video')

cv.namedWindow("trackbar")

cv.createTrackbar("l","trackbar",0,255,nothing)
cv.createTrackbar("h","trackbar",100,255,nothing)

# compare two numpy arrays
def _is(a,b,c ='in'):

	_a = [ 1 if x == 255 else 0 for x in a]
	#print(list(_a))
	if c == "in":
		for d in b:
			#print(d)
			if _a ==list(d):
				return _a ==list(d)
	elif c == '=':
		return _a ==list(_b)


# this funtion generates coordinates of x and y from contours
def arrayrize(cons,plane='x'):

	l = []
	#print(cons)
	for c in cons:
		for i in range(len(c)):
			if plane == 'y':
				#print(c[i][0][0])
				l.append(c[i][0][0])
			elif plane == 'x':
				#print(c[i][0][1])
				l.append(c[i][0][1])
	return l
def analyzer(img):
	size = img.shape[0]
	a = size//4

	im_0 = img[a*0:a*(0+1),a*0:a*(0+1)]
	im_1 = img[a*0:a*(0+1),a*1:a*(1+1)]
	im_2 = img[a*0:a*(0+1),a*2:a*(2+1)]
	im_3 = img[a*0:a*(0+1),a*3:a*(3+1)]
	im_4 = img[a*1:a*(1+1),a*0:a*(0+1)]
	im_5 = img[a*1:a*(1+1),a*1:a*(1+1)]
	im_6 = img[a*1:a*(1+1),a*2:a*(2+1)]
	im_7 = img[a*1:a*(1+1),a*3:a*(3+1)]
	im_8 = img[a*2:a*(2+1),a*0:a*(0+1)]
	im_9 = img[a*2:a*(2+1),a*1:a*(1+1)]
	im_10 = img[a*2:a*(2+1),a*2:a*(2+1)]
	im_11 = img[a*2:a*(2+1),a*3:a*(3+1)]
	im_12 = img[a*3:a*(3+1),a*0:a*(0+1)]
	im_13 = img[a*3:a*(3+1),a*1:a*(1+1)]
	im_14 = img[a*3:a*(3+1),a*2:a*(2+1)]
	im_15 = img[a*3:a*(3+1),a*3:a*(3+1)]


	L = [im_0,im_1,im_2,im_3,im_4,im_5,im_6,im_7,im_8,im_9,im_10,im_11,im_12,im_13,im_14,im_15]

	if _is(L,tp.my_list) == True:
		print("yes")
		print([ 1 if x == 255 else 0 for x in L])
		return True


	
while True:
	isTrue, frame = cap.read()

	frame = cv.resize(frame,(480,320))
	
	a = 100

	x = (frame.shape[1]//2)-100
	y = (frame.shape[0]//2)-100
	x2= (frame.shape[1]//2)+100
	y2= (frame.shape[0]//2)+100


	a = cv.getTrackbarPos('l','trackbar')
	b = cv.getTrackbarPos('h','trackbar')
	l_black = np.array([a,a,a])
	u_black = np.array([b,b,b])
	

	cv.rectangle(frame,(x,y),(x2,y2),(0,255,0),thickness = 2)
	img2 = frame[y:y2,x:x2]
	#print((x,y),(x2,y2))
	img2 = cv.inRange(img2,l_black,u_black)
	cv.imshow('frame2',img2)
	sized = cv.resize(img2,(4,4))

	close = analyzer(sized)

	#mask = cv.cvtColor(sized, cv.COLOR_BGR2GRAY)
	
	

	
	cv.imshow('frame',frame)
	if close == True or cv.waitKey(12) & 0xFF == ord('d'):
		break
cap.release()
cv.destroyAllWindows()