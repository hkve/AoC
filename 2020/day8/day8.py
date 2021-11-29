import numpy as np

ins = np.loadtxt("input.txt", unpack=True, dtype=str, usecols=(0))
vals = np.loadtxt("input.txt", unpack=False, dtype=int, usecols=(1))

def task1(ins, vals):
	i = 1
	accumulator = 0
	ins_ = np.empty_like(ins)
	ins_[:] = ins
	while True:
		if i == len(ins_):
			return accumulator, i
		elif ins_[i] == "nop":
			ins_[i] = ""
			i += 1
		elif ins_[i] == "acc":
			accumulator += vals[i]
			ins_[i] = ""
			i += 1
		elif ins_[i] == "jmp":
			ins_[i] = ""
			i += vals[i]
		else:
			break

	return accumulator, i

def task2(ins, vals):
	chg = ["nop", "jmp"]
	term = len(ins)

	for i in range(2):
		chg_idx = np.where(ins == chg[i])[0]
		for idx in chg_idx:
			ins_ = np.empty_like(ins)
			ins_[:] = ins
			ins_[idx] = chg[-i+1]
			try:
				acc, k = task1(ins_, vals)
				
			except IndexError:
				pass
			if k == term:
				return acc



		

print(task1(ins, vals)[0])
print(task2(ins, vals))