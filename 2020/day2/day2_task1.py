
def isValid(start, stop, letter, password):
	counter = 0
	for letter_ in password:
		if letter_ == letter:
			counter += 1

	if start <= counter <= stop:
		return True
	else:
		return False

accept = 0
with open("input2.txt") as file:
	for LINE in file:
		line = LINE.split()
		letter = line[1][:-1]
		start, stop = line[0].split("-")
		passwd = line[2]

		start = int(start)
		stop = int(stop)

		if isValid(start, stop, letter, passwd):
			accept += 1


print(accept)