import numpy as np

def row(tst):
	Min = 0
	Max = 127

	for letter in tst[:-3]:
		dRow = Max-Min
		if letter == "F":
			Max = int(Max - dRow/2)
		else:
			Min = round(Min + dRow/2, 0)
		
	return Max

def column(tst):
	Min = 0
	Max = 7	
	for letter in tst[-3:]:
		dCol = Max-Min
		if letter == "L":
			Max = int(Max - dCol/2)
		else:
			Min = round(Min + dCol/2, 0)

	return Max


data = np.loadtxt("input.txt", dtype="str")
ID = np.zeros_like(data, dtype=int)

for i, seat in enumerate(data):
	ID[i] = row(seat)*8 + column(seat)
	
ID = np.sort(ID)
for i in range(len(ID)-1):
	if ID[i+1]-ID[i] == 2:
		print(ID[i-3:i+3])



