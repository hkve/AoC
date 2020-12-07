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

			temp = {}
			for cont in other:
				cont = cont
				cont = cont.strip()

				if cont == "no other":
					temp["no other"] = 0
				else:
					amount, color = int(cont[:2]), cont[2:]
					temp[color] = amount
			
			contains[bag] = temp
			bags.append(bag)
		
	return bags, contains


bags, contents = readRules("input.txt")
N = []

def findCont(bag):
	n = 1
	for k in contents[bag].items():
		if k[0] == "no other":
			return n
		else:
			n += k[1]*findCont(k[0])
	return n	

print(findCont("shiny gold")-1)