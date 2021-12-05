from utils import read_file

def day2_a():
	with open("input/day3.in") as file: n_bits = len(file.readline().strip())

	col_bits = [ [] for _ in range(n_bits)]

	for line in read_file("day3.in"):
		for i, c in enumerate(line):
			col_bits[i].append(int(c))

	gamma = ""
	for col in col_bits:
		if col.count(1) > col.count(0):
			gamma += "1"
		else:
			gamma += "0"

	epsilon = gamma.replace("1", "2")
	epsilon = epsilon.replace("0", "1")
	epsilon = epsilon.replace("2", "0")

	return int(gamma, 2) * int(epsilon, 2)

def reduce(bits, keep, remove):
	i = 0
	
	while len(bits) != 1:
		k_c, r_c = 0,0
		for bit in bits:
			if int(bit[i]) == keep:
				k_c += 1
			else:
				r_c += 1

		if keep == 1 and remove == 0:
			if k_c >= r_c:
				r = remove
			else:
				r = keep
		else:
			if k_c <= r_c:
				r = remove
			else:
				r = keep

		for j in range(len(bits)-1, -1, -1):
			if int(bits[j][i]) == r:
				del bits[j]

		i += 1

	return int(*bits, 2)

def day2_b():
	with open("input/day3.in") as file: n_bits = len(file.readline().strip())

	bits = []
	for line in read_file("day3.in"):
		bits.append(line)
	

	bits2 = bits.copy()

	O2gr = reduce(bits, 1, 0)
	CO2sr = reduce(bits2, 0,1)

	print(O2gr*CO2sr)

day2_b()