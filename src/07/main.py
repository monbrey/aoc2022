import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir_path}/input.txt", "r").read()

path = []
sizes = {}
limit = 100_000
commands = [command.strip() for command in input.split("$")]

for c in commands:
	match c[:2]:
		case 'cd':
			path.pop() if c[3:] == '..' else path.append("".join(path)+c[3:])
			print(path)
		case 'ls':
			total = sum([int(x[0]) for x in (x.split(" ") for x in c.split("\n")[1:]) if x[0].isdigit()])
			for dir in path:
				sizes[dir] = sizes.get(dir,0) + total

print(sum([v if v <= limit else 0 for v in sizes.values()]))

total_size = 70_000_000
target_free = 30_000_000
max_used = total_size - target_free
curr_used = sizes.get("/")
to_save = curr_used - max_used

print(min([v for k,v in sizes.items() if v > to_save]))
