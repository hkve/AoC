import utils

def day1_a():
	mes = [int(m) for m in utils.read_file("day1.in")]
	n_inc = 0
	
	for i in range(1,len(mes)):
		if mes[i] > mes[i-1]:
			n_inc += 1
	
	return n_inc

def day1_b():
	mes = [int(m) for m in utils.read_file("day1.in")]
	n_inc = 0

	for i in range(1, len(mes)-2):
		if sum(mes[i:i+3]) > sum(mes[i-1:i+2]):
			n_inc += 1

	return n_inc
print(day1_b())