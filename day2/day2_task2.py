

def isValid(i1, i2, letter, password):
	i1 -= 1
	i2 -= 1
	acceptedLetter = 0

	if password[i1] == letter:
		acceptedLetter += 1
	if password[i2] == letter:
		acceptedLetter += 1

	if acceptedLetter == 1:
		return True

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