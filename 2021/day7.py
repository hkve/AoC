import numpy as np

def day7_a():
	crabs = np.loadtxt("input/day7.in", delimiter=",", dtype=int)
	crabs_u = np.unique(crabs)
	fuel = np.zeros_like(crabs_u)

	for i, crab in enumerate(crabs_u):
		fuel[i] = np.sum(np.abs(crabs-crab))

	print(np.min(fuel))

def day7_b():
	crabs = np.loadtxt("input/day7.in", delimiter=",", dtype=int)
	all_pos = np.arange(np.min(crabs), np.max(crabs))	
	fuel = np.zeros_like(all_pos)

	for i, pos in enumerate(all_pos):
		n = abs(crabs-pos)
		fuel[i] = np.sum(n*(n+1)/2)

	print(np.min(fuel))

day7_b()



