

grid = []
with open("input3.txt") as file:
	for line in file:
		row = []
		for char in line:
			if char != "\n":
				row.append(char)	
		grid.append(row)

h, w = len(grid), len(grid[0])

r, c = 0, 0 
threes = 0
while r < h:
	if(c >= w):
		c -= w
		
	if grid[r][c] == "#":
			threes += 1 

	r += 1
	c += 3



print(threes)