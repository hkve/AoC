def read_grid():
	grid = []
	with open("input3.txt") as file:
		for line in file:
			row = []
			for char in line:
				if char != "\n":
					row.append(char)	
			grid.append(row)
	return grid

def traverse_grid(right, left, grid):
	h, w = len(grid), len(grid[0])

	r, c = 0, 0 
	threes = 0
	while r < h:
		if(c >= w):
			c -= w
			
		if grid[r][c] == "#":
			threes += 1 

		r += right
		c += left

	return threes

grid = read_grid()

rules = [[1,1],
		 [3,1],
		 [5,1],
		 [7,1],
		 [1,2]]

tot = 1
for rule in rules:
	temp = traverse_grid(rule[1], rule[0], grid)
	tot *= temp

print(tot)