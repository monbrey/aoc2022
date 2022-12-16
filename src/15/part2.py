import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
input = [line.strip() for line in open(f"{dir_path}/input.txt", "r")]
coordinates = [re.search(r".*x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+)", line).groups() for line in input]

min_x = min(list(map(int, list(sum(coordinates, ())[::2]))))
max_x = max(list(map(int, list(sum(coordinates, ())[::2]))))

distance = lambda x,y: abs(x[0]-y[0])+abs(x[1]-y[1])

distances = {}
beacons = []
for coord in coordinates:
	sensor = (int(coord[0]),int(coord[1]))
	beacon = (int(coord[2]),int(coord[3]))
	beacons.append(beacon)
	distances[sensor] = distance(sensor, beacon)

def not_beacon(p):
	return all([(distance(p,q) > d) for q,d in distances.items()])

for s,d in distances.items():
	d = d+1
	p1 = [(s[0]-(i-d),s[1]-i)for i in range(0,d+1)]
	p2 = [(s[0]+(i-d),s[1]-i)for i in range(0,d+1)]
	p3 = [(s[0]-(i-d),s[1]+i)for i in range(0,d+1)]
	p4 = [(s[0]+(i-d),s[1]+i)for i in range(0,d+1)]
	points = set([*p1, *p2, *p3, *p4])
	points = list(filter(lambda p: p[0] in range(0,4000000) and p[1] in range(0,4000000), points))
	for p in points:
		if not_beacon(p):
			print(p)
			print(p[0]*4000000+p[1])
			exit()
