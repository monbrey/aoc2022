import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir_path}/input.txt", "r").read()

# literally just change 4 to 14
for i in range(14,len(input)):
	if len(set(input[i:i+14])) == 14:
		print(i+14)
		exit()

