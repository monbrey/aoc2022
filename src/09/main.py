import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
input = [line.strip().split(' ') for line in open(f"{dir_path}/input.txt", "r")]

# starting point
head = [0,0]
tail = [0,0]
# maximum distance still touching will always be the diagonal
max_dist = math.dist([0,0],[-1,-1])
# set of points tail touched
tail_pos = {(0,0)}


def move(point, dir):
	match dir:
		case 'R':
			point[0] += 1
		case 'L':
			point[0] -= 1
		case 'U':
			point[1] -= 1
		case 'D':
			point[1] += 1


for step in input:
	for i in range(1,int(step[1])+1):
		move(head, step[0])
		dist = math.dist(head,tail)
		if dist > max_dist:
			# we're out of range, determine directions - X is no move
				move(tail, 'U' if tail[1] > head[1] else ('D' if tail[1] < head[1] else 'X'))
				move(tail, 'L' if tail[0] > head[0] else ('R' if tail[0] < head[0] else 'X'))
		# add the tail position to the set
		tail_pos.add(tuple(tail))

print(len(tail_pos))

# for part 2 we need to track 10 knots
knots = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
# and reset the set of positions
tail_pos = {(0,0)}

for step in input:
	for i in range(1,int(step[1])+1):
		move(knots[0], step[0])
		# now instead of comparing the tail, we need to compare every knot from the head down to the tail
		for k in range(1,len(knots)):
			dist = math.dist(knots[k-1],knots[k])
			if dist > max_dist:
				# we're out of range, determine direction - X is no move
					move(knots[k], 'U' if knots[k][1] > knots[k-1][1] else ('D' if knots[k][1] < knots[k-1][1] else 'X'))
					move(knots[k], 'L' if knots[k][0] > knots[k-1][0] else ('R' if knots[k][0] < knots[k-1][0] else 'X'))
		# with that done, add the last knot pos to the set
		tail_pos.add(tuple(knots[9]))

print(len(tail_pos))