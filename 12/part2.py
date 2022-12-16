import os
import numpy as np
from collections import deque as queue

dir_path = os.path.dirname(os.path.realpath(__file__))

# parse the input
graph = np.array([list(map(lambda x: ord(x) - 96, [*line.strip()])) for line in open(f"{dir_path}/input.txt", "r").readlines()])
visited = np.full(shape=graph.shape, fill_value=False)

start = None

# find start (for p2 I intend to traverse backwards)
for row in range(0,graph.shape[0]):
	for col in range(0, graph.shape[1]):
		if graph[row][col] == -27:
			graph[row][col] = 26
			start = (row,col)


dx = [-1,0,1,0]
dy = [0,-1,0,1]


def can_visit(visited, curr, next):
	if next[0] not in range(0,graph.shape[0]) or next[1] not in range(0,graph.shape[1]):
		return False
	if visited[next]:
		return False
	if graph[next] < graph[curr]-1: # p2 reverse, gotta climb down one
		return False

	return True


def bfs(graph, visited, start):
	shortest = 999999
	q = queue()
	q.append(start)
	visited[start] = True
	dist = { start: 0 }

	while len(q) > 0:
		cell = q.popleft()
		x,y = cell
		print(cell)
		if graph[cell] == 1: # its a possible starting cell
			return dist[cell]
		for i in range(4):
			next = (x+dx[i],y+dy[i])
			if can_visit(visited, cell, next):
				dist[next] = dist[cell]+1
				q.append(next)
				visited[next] = True


print(bfs(graph,visited,start))