import numpy as np
"""def count(arr,val):
	count = 0
	for c in arr:
		if c == val:
			count +=1
	return count

"""
#changes the points to match the dectectable 16 grids system
def changes(arr):
	l = arr
	for i in range(len(l)):
		for c in range(len(l[i])):
			if l[i][c] == 0:
				l[i][c] = 1 
			elif l[i][c] == 1:
				l[i][c] = 2 
			elif l[i][c] == 2:
				l[i][c] = 4 
			elif l[i][c] == 3:
				l[i][c] = 5 
			elif l[i][c] == 4:
				l[i][c] = 6 
			elif l[i][c] == 5:
				l[i][c] = 7 
			elif l[i][c] == 6:
				l[i][c] = 8 
			elif l[i][c] == 7:
				l[i][c] = 9 
			elif l[i][c] == 8:
				l[i][c] = 10 
			elif l[i][c] == 9:
				l[i][c] = 11 
			elif l[i][c] == 10:
				l[i][c] = 13 
			elif l[i][c] == 11:
				l[i][c] = 14 

	return l

#covertes identification codes to binary
def fine(arr):
	m = arr
	l = np.zeros(16)
	n = []

	l[0] = 1
	l[3] = 1
	l[12] = 1
	l[15] = 1
	for i in range(len(m)):
		l = np.zeros(16,dtype ='int')

		l[0] = 1
		l[3] = 1
		l[12] = 1
		l[15] = 1
		#print(l)
		for j in range(len(m[i])):
			#print(arr[i][j])
			l[arr[i][j]] = 1
		n.append(l)
		#print(l)
	return n



#sorts the arrays and removes one thar repeat 
def sortin(arr):
	m = []
	n = []
	#print(arr)
	for c in arr:
		b = c
		b.sort()
		#print(b)
		m.append(b)
	for d in m:
		if d not in n:
			n.append(d)
	return n


p_t = []
pu_t = []
my_list = []
for i in range(12):
	for j in range(12):
		for k in range(12):
			a = [i,j,k]
			if [i,j,k].count(a[0]) == 1 and [i,j,k].count(a[1]) == 1 and [i,j,k].count(a[2]) == 1:
				pu_t.append([i,j,k])
			else:
				continue
p_t = sortin(pu_t)
my_list = fine(changes(p_t))
#print(my_list)

#print((pu_t))
#print(p_t)
#print(changes(p_t))

#print(list(my_list[1]))
#print(my_list[0])

#print(changes(p_t))

