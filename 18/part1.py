import sys

input = [tuple(map(int, line.strip().split(','))) for line in open(sys.argv[1]).readlines()]
faces = len(input)*6
adj = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

for x,y,z in input:
	adjacents = [(x+dx,y+dy,z+dz) for dx,dy,dz in adj if (x+dx,y+dy,z+dz) in input]
	faces -= len(adjacents)

# part 1
print(faces)