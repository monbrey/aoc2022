import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir_path}/input.txt", "r").read()

for i in range(4,len(input)):
	if len(set(input[i:i+4])) == 4:
		print(i+4)
		exit()

