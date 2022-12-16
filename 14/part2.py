import os
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

dir_path = os.path.dirname(os.path.realpath(__file__))
input = [list(map(lambda x: list(map(lambda y: int(y), x.split(','))), line.split(' -> '))) for line in open(f"{dir_path}/input.txt", "r").read().split('\n')]

x2 = max(c[0] for path in input for c in path)
y = max(c[1] for path in input for c in path)

print(x2,y)

pos = lambda p: [p[1], p[0]]
wall = np.full((y+1,x2+500), '.')

gap = np.full((1,wall.shape[1]),'.')
floor = np.full((1,wall.shape[1]),'#')
wall = np.concatenate((wall,gap,floor))

for i, row in enumerate(wall):
	print(i, ''.join(row))

for path in input:
	for i in range(0,len(path)-1):
		start = pos(path[i])
		end = pos(path[i+1])
		l,r = sorted([start[0],end[0]])
		u,d = sorted([start[1],end[1]])
		for x in range(l,r+1):
			wall[x,u] = '#'
		for y in range(u,d+1):
			wall[l,y] = '#'

overflowing = False
sand = tuple(pos([500,0]))
placed = 0

def fall(grain):
	global overflowing, placed
	next = tuple([grain[0]+1, grain[1]])
	while wall[next] == '.':
		grain = next
		next = tuple([grain[0]+1, grain[1]])
		
		if next[0] >= wall.shape[0]:
			return False
	if next[1]-1 < 0 or next[1]+1 >= wall.shape[1]:
		return False
	left,right = tuple([next[0],next[1]-1]), tuple([next[0],next[1]+1])
	if wall[left] == '.':
		return fall(left)
	if wall[right] == '.':
		return fall(right)

	wall[grain] = 'o'
	placed += 1

	return not grain == sand


while fall(sand):
	continue

print(placed)