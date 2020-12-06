
with open("input.txt") as file:
	newPassport = []
	newRequierment = []
	Passports = []
	Requierments = []
	nextPassport = False
	for line in file:
		line = line.split(" ")

		if line[0] == '\n':
			nextPassport = True
		elif nextPassport == False:
			for elm in line:
				elm = elm.split(":")
				newPassport.append(elm[0])
				newRequierment.append(elm[1])
		
		if nextPassport == True:
			Passports.append(newPassport)
			Requierments.append(newRequierment)
			newPassport = []
			newRequierment = []
			nextPassport = False

needed = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

accept = 0
for passport in Passports:
	allGood = True
	for demand in needed:
		if not demand in passport:
			allGood = False

	if allGood == True:
		accept += 1

print(accept)

