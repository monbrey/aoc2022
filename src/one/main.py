import os

dir_path = os.path.dirname(os.path.realpath(__file__))

inputfile = open(f"{dir_path}/input.txt", "r")
input = inputfile.read()
inputfile.close()

elves = input.strip().split("\n\n")

for i, elf in enumerate(elves):
	elves[i] = sum(map(int, elf.split("\n")))

print(f"Part 1: {max(elves)}")

top3 = sorted(elves, reverse=True)[:3]
print(f"Part 2: {sum(top3)}")