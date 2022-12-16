import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
input = [pair.split('\n') for pair in open(f"{dir_path}/input.txt", "r").read().split('\n\n')]

def compare(a,b):
	for i in range(0, min(len(a),len(b))):
		x,y = a[i], b[i]

		if isinstance(x,int) and isinstance(y,int):
			if x == y: continue
			return x < y

		x2 = [x] if isinstance(x,int) else x
		y2 = [y] if isinstance(y,int) else y

		in_order = compare(x2,y2)
		if in_order == None: continue
		return in_order

	if len(a) == len(b): return None
	return len(a) < len(b)

ordered = []

for i, pair in enumerate(input):
	a, b = json.loads(pair[0]), json.loads(pair[1])
	in_order = compare(a,b)
	if in_order:
		ordered.append(i+1)

print(f"Part 1: {sum(ordered)}")

