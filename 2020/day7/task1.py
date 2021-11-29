def readRules(filename):
	bags = []
	contains = {}
	with open(filename) as file:
		for line  in file:
			line = line.strip()
			line = line.replace("bags", "")
			line = line.replace("bag", "")
			line = line.replace(".", "")
			line = line.split("contain")

			other = line[1].split(",")
			bag = line[0].strip()
			temp = []
			for cont in other:
				cont = cont[3:]
				cont = cont.strip()
				if cont != "other":
					temp.append(cont)
			
			if cont != "other":
				contains[bag] = temp
				bags.append(bag)
			
	return bags, contains


bags, contents = readRules("input.txt")

def part1():
	goodBags = set()
	for bag in bags:
		for cont in contents[bag]:
			if cont == "shiny gold":
				goodBags.add(bag)

	l2 = 1
	l1 = 0
	while l2 > l1:
		l1 = len(goodBags)
		for bag in bags:
			for cont in contents[bag]:
				if cont in goodBags:
					goodBags.add(bag)
		l2 = len(goodBags)

	return goodBags

print(len(part1()))