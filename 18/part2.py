import sys, numpy

input = [tuple(map(int, line.strip().split(','))) for line in open(sys.argv[1]).readlines()]
adj = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

mx = max([c[0] for c in input])
my = max([c[1] for c in input])
mz = max([c[2] for c in input])

# construct an array
cells = numpy.full((mx+1,my+1,mz+1), ".")

# fill the edges with water
for x in range(mx+1):
	for y in range(my+1):
		for z in range(mz+1):
			if x in (0, mx) or y in (0, my) or z in (0, mz):
				cells[(x,y,z)] = "W"

# set the lava
for cell in input:
	cells[cell] = "L"

# let the water flow around the shape
while True:
	flow = False
	for x in range(1,mx):
		for y in range(1,my):
			for z in range(1,mz):
				if cells[(x,y,z)] == '.':
					for a in [(x+dx,y+dy,z+dz) for dx,dy,dz in adj]:
						if cells[a] == 'W':
							cells[(x,y,z)] = 'W'
							flow = True
							break
	if not flow:
		break

surface = 0
# do basically the same check as before, but only count the fact if the adjacent cell is water (or an edge)
for x,y,z in input:
	adjacents = [(x+dx,y+dy,z+dz) for dx,dy,dz in adj]
	for x2,y2,z2 in adjacents:
		try:
			# if it touches water, its exterior
			if cells[(x2,y2,z2)] == "W":
				surface += 1
		except IndexError:
			# edges are water too
			surface += 1


print(surface)

