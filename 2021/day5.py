from utils import read_file
import numpy as np
import collections

def read_edges():
	s, e = [], []
	for line in read_file("day5.in"):
		s_, e_ = line.split("->")
		s.append([int(elm) for elm in s_.split(",")])
		e.append([int(elm) for elm in e_.split(",")])

	return np.array(s), np.array(e)

def mk_grid(s,e):
	l = np.max(np.c_[s[:,0], e[:,0]])
	h = np.max(np.c_[s[:,0], e[:,1]])
	
	return np.zeros((l+1,h+1), dtype=int)

def horizontal(s, e, grid):
	l_dif = e[0]-s[0]
	h_dif = e[1]-s[1]

	if any(np.array([h_dif, l_dif]) == 0):
		if l_dif != 0:
			if l_dif < 0:
				grid[e[0]:(e[0]+abs(l_dif)+1), s[1]] += 1
			else:
				grid[s[0]:(s[0]+l_dif+1), s[1]] += 1
		elif h_dif != 0:
			if h_dif < 0:
				grid[s[0], e[1]:(e[1]+abs(h_dif)+1)] += 1
			else:
				grid[s[0], s[1]:(s[1]+h_dif+1)] += 1

def vertical(s, e, grid):
	l_dif = e[0]-s[0]
	h_dif = e[1]-s[1]

	if abs(l_dif) == abs(h_dif):
		if l_dif < 0: 
			i_inc = -1
		else:
			i_inc = 1
		if h_dif < 0:
			j_inc = -1
		else:
			j_inc = 1

		try:
			i, j = s[0], s[1]
			while i != e[0]+i_inc and j != e[1]+j_inc:
				grid[i,j] += 1
				i += i_inc
				j += j_inc
		except IndexError:
			pass

def day5_a():
	s, e = read_edges()
	grid = mk_grid(s, e)

	for s_, e_ in zip(s, e):
		horizontal(s_, e_, grid)

	count = collections.Counter(grid.flat)
	sum_count = 0
	
	for i in range(2, np.max(grid)+1):
		sum_count += count[i]

	return sum_count

def day5_b():
	s, e = read_edges()
	grid = mk_grid(s, e)

	for s_, e_ in zip(s, e):
		horizontal(s_, e_, grid)
		vertical(s_, e_, grid)
	
	count = collections.Counter(grid.flat)
	sum_count = 0
	
	for i in range(2, np.max(grid)+1):
		sum_count += count[i]

	return sum_count

print(day5_b())