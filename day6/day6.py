import string

def getGroups(filename):
	groups = []
	newGroup = []
	with open(filename) as file:
		for line in file:
			line = line.strip()
			if line == "":
				groups.append(newGroup)
				newGroup = []
			else:
				newGroup.append(line)

	groups.append(newGroup)
	return groups


def countLetters(group):
	ansrs = 0
	alpha = string.ascii_lowercase
	for person in group:
		for letter in person:
			if letter in alpha:
				ansrs += 1
				alpha = alpha.replace(letter, "")	

	return ansrs

def countCommonLetters(group):
	ansrs = 0
	counter = {}
	groupSize = len(group)
	alpha = string.ascii_lowercase
	
	for letter in alpha:
		counter[letter] = 0
	
	for person in group:
		for letter in person:
			counter[letter] += 1

	for val in counter:
		if counter[val] == groupSize:
			ansrs += 1
	
	return ansrs

groups = getGroups("input.txt") 

s1, s2 = 0, 0
for group in groups:
	s1 += countLetters(group)
	s2 += countCommonLetters(group)

print(s1, s2)