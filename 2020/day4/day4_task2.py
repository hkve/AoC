
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
				newRequierment.append(elm[1].replace("\n", ""))
		
		if nextPassport == True:
			Passports.append(newPassport)
			Requierments.append(newRequierment)
			newPassport = []
			newRequierment = []
			nextPassport = False

needed = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eclReq = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

accept = 0
for passport, requierments in zip(Passports, Requierments):

	isValid = True
	for entry, requierment in zip(passport, requierments):
		if entry == "byr":
			if not 1920 <= int(requierment) <= 2002:
				isValid = False
		if entry == "iyr":
			if not 2010 <= int(requierment) <= 2020:
				isValid = False
		if entry == "eyr":
			if not 2020 <= int(requierment) <= 2030:
				isValid = False
		if entry == "hgt":
			if "in" in requierment:
				requierment = requierment.replace("in", "")
				if not 59 <= int(requierment) <= 76:
					isValid = False

			elif "cm" in requierment:	
				requierment = requierment.replace("cm", "")
				if not 150 <= int(requierment) <= 193:
					isValid = False
			else:
				isValid = False
		if entry == "hcl":
			if requierment[0] == "#" and len(requierment[1:]) == 6:
				pass
			else:
				isValid = False

		if entry == "ecl":
			correctEye = False
			for req in eclReq:
				if requierment == req:
					correctEye = True

			if not correctEye:
				isValid=False
		if entry == "pid":
			if len(requierment) == 9:
				try:
				 	int(requierment)
				except:
					isValid = False
			else:
				isValid = False

	allGood = True
	for demand in needed:
		if not demand in passport:
			allGood = False

	if allGood == True and isValid == True:
		accept += 1

print(accept)