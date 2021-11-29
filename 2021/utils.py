import re
import os


def read_file(filename, pat=None):
	folder = "input"

	if not folder in os.listdir():
		os.mkdir(folder)
		exit()

	if not filename in os.listdir(folder):
		print(f"Did not find {filename}")
		exit()

	with open(f"{folder}/{filename}", "r") as file:
		for line in file:		
			if pat is not None:
				yield re.findall(pat, line)	
			else:
				yield line.strip()