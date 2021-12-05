from utils import read_file

def day2_a():
	depth, hor = 0,0

	for line in read_file("day2.in"):
		d, n = line.split()
		n = int(n)
		d = d[0]

		if d == "f":
			hor += n
		elif d == "u":
			depth += n
		else: 
			depth -= n

	return hor, -depth

def day2_b():
	dep, hor, aim = 0,0,0

	for line in read_file("day2.in"):
		d, n = line.split()
		n = int(n)
		d = d[0]		

		if d == "d":
			aim += n
		elif d =="u":
			aim -= n
		else:
			hor += n
			dep += (n*aim)

	return hor,dep 
h, d = day2()
print(h*d)