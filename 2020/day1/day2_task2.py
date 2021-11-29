import numpy as np

data = np.loadtxt("input1.txt", dtype=int)

for i in range(len(data)):
	for j in range(i+1, len(data)):
		for k in range(j+1, len(data)):
			s = data[i] + data[j] + data[k]
			if s == 2020:
				print(data[i]*data[j]*data[k])