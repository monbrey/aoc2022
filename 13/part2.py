import os
import json
from functools import cmp_to_key

dir_path = os.path.dirname(os.path.realpath(__file__))
input = [json.loads(item) for sublist in [pair.split('\n') for pair in open(f"{dir_path}/input.txt", "r").read().split('\n\n')] for item in sublist]
input.extend([[[2]],[[6]]])

def compare(a,b):
	for i in range(0, min(len(a),len(b))):
		x,y = a[i], b[i]

		if isinstance(x,int) and isinstance(y,int):
			if x == y: continue
			return x - y

		x2 = [x] if isinstance(x,int) else x
		y2 = [y] if isinstance(y,int) else y

		in_order = compare(x2,y2)
		if in_order == 0: continue
		return in_order
		
	return len(a) - len(b)

s = sorted(input, key=cmp_to_key(compare))

print(f"Part 2: {(s.index([[2]])+1)*(s.index([[6]])+1)}")


