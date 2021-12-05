from utils import read_file
import numpy as np

def get():
	nums = []
	boards = []
	new_board = []

	for i, line in enumerate(read_file("day4.in")):
		if i == 0: nums = [int(num) for num in line.split(",")]
		else:
			if line == "":
				boards.append(np.array(new_board))
				new_board = []
			else:
				new_board.append([int(num) for num in line.split()])

	del boards[0]
	boards.append(np.array(new_board))
	return nums, boards

def bingo(mark):
	bing = np.ones(5, dtype=int)
	
	for i in range(len(mark)):
		if all(mark[i] == bing) or all(mark[:,i] == bing):
			return True

	return False

def day4_a():
	nums, boards = get()
	marks = []
	bingo_board = np.zeros_like(boards[0])
	bingo_marks	= np.zeros_like(boards[0])
	bingo_num = 0
	for board in boards:
		marks.append(np.zeros_like(board))

	for num in nums:
		for i in range(len(boards)):
			marks[i][np.where(boards[i]==num)] = 1
			found = bingo(marks[i])
			if found:
				bingo_board = boards[i]
				bingo_marks = marks[i]
				bingo_num = num
				break
		if found: break

	unmarked_sum = np.sum(bingo_board[np.where(bingo_marks==0)])
	return unmarked_sum * bingo_num

def day4_b():
	nums, boards = get()
	
	n_boards = len(boards)
	bingo_board = np.zeros_like(boards[0])
	bingo_marks	= np.zeros_like(boards[0])
	bingo_num = 0
	
	marks = []
	for board in boards:
		marks.append(np.zeros_like(board))

	found_last = False
	for num in nums:
		for i in range(len(boards)-1, -1, -1):
			marks[i][np.where(boards[i]==num)] = 1
			found = bingo(marks[i])
			if found and n_boards != 1:
				del boards[i]
				del marks[i]
				n_boards -= 1
			elif found and n_boards == 1:
				bingo_board = boards[i]
				bingo_marks = marks[i]
				bingo_num = num
				found_last = True
				break

		if found_last: break

	unmarked_sum = np.sum(bingo_board[np.where(bingo_marks==0)])
	
	return unmarked_sum * bingo_num

print(day4_b())