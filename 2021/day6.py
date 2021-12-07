from utils import read_file
import numpy as np
import collections 

class Fish:
	def __init__(self, s0):
		self.s0 = s0
		self.state = s0
		self.dupe = False

	def check_state(self):
		if self.state == 0:
			self.dupe = True


	def do_dupe(self):
		self.dupe = False
		self.state = 7
		return Fish(8)


def day6_a():
	for e in read_file("day6.in"):
		_ = e.split(",")
		fishes = [Fish(int(j)) for j in _]

	days = 256
	for i in range(days):
		new_fishes = []
		for fish in fishes:
			if fish.dupe:
				new_fishes.append(fish.do_dupe())
	
			fish.state -= 1
			fish.check_state()

		fishes += new_fishes

	return len(fishes)


def day6_b():
	for e in read_file("day6.in"):
		_ = e.split(",")
		fishes = np.array([int(j) for j in _])

	c = collections.Counter(fishes)
	x = np.zeros(9, dtype=int)
	for i in range(len(x)):
		if i in c.keys():
			x[i] = c[i]
		else:
			x[i] = 0

	mat = np.zeros((9,9), dtype=int)
	for i in range(8): mat[i,i+1] = 1
	mat[-1,0] = 1
	mat[-3,0] = 1
	
	days = 256
	for i in range(days):
		x = np.matmul(mat, x)
	print(sum(x))
day6_b()