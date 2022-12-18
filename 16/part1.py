import sys, re

valves = [re.search(r".*([A-Z]{2}).*rate=(\d+);.*valves? (.*)", line).groups() for line in open(sys.argv[1])]
tunnels = { a: c.split(', ') for a,b,c in valves }
rates = { a: int(b) for a,b,c in valves }

def calc_dists(graph, source):
	q = [source]
	visited = [source]
	distances = { }

	while q:
		p = q.pop(0)
		if p == source:
			distances[p] = 0
		for n in graph[p]:
			if n not in visited:
				distances[n] = distances[p]+1
				q.append(n)
				visited.append(n)

	return distances

graphs = { k: { a:b for a,b in calc_dists(tunnels, k).items() if rates[a] > 0 and a != k } for k in tunnels }
to_visit = [k for k in rates if rates[k] > 0]

def find_paths(start):
	paths = []
	count = 0
	queue = []
	queue.append((30,start,[start]))

	while queue:
		count += 1
		t,p,v = queue.pop(0)
		if set(to_visit).issubset(set(v)) or t <= 0:
			paths.append(v)
		else:
			for n in graphs[p]:
				if t-graphs[p][n] >=0 and n not in v and n != p:
					queue.append((t-graphs[p][n], n, [*v, n]))
	return paths

def calc_flow(p):
	time = 30
	flow = 0
	
	prev = p[0]
	for node in p:
		if node != prev:
			# move to the node
			time -= graphs[prev][node]
		if rates[node] != 0:
			# open the node
			time -= 1
			flow += rates[node]*time
			prev = node

	return flow


print(max([calc_flow(p) for p in find_paths('MO')]))
# print(calc_values('AA'))
# while time_left > 0:
# 	distances = calc_dist(point)
# 	values = { k: rates.get(k)**(time_left-v-1) for k,v in distances.items() if (v+1) < time_left and k not in opened }
# 	if not values:
# 		break

# 	next = max(values, key=values.get)
# 	print(distances)
# 	print(values)
# 	opened.append(next)
# 	time_left -= distances.get(next)+1
# 	time_so_far += distances.get(next)+1
# 	print(f"Opening {next}")
# 	print(f"Time so far is {time_so_far}, time remaining is {time_left}")
# 	pressure += rates.get(next)
# 	flow += rates.get(next) * time_left
# 	print(f"Total pressure being released is {pressure}")
# 	print(f"This valve will release a total of {rates.get(next) * time_left}")
# 	print(f"Total flow rate so far is {flow}")

# 	point = next
	
# print(flow)