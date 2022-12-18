import os
import numpy as np
from collections import deque as queue

dir_path = os.path.dirname(os.path.realpath(__file__))

# parse the input
graph = np.array([list(map(lambda x: ord(x) - 96, [*line.strip()])) for line in open(f"{dir_path}/input.txt", "r").readlines()])
visited = np.full(shape=graph.shape, fill_value=False)

start = end = None

# find start
for row in range(0,graph.shape[0]):
	for col in range(0, graph.shape[1]):
		if graph[row][col] == -13:
			start = (row,col)
			graph[row][col] = 1
		if graph[row][col] == -27:
			end = (row,col)
			graph[row][col] = 26

dx = [-1,0,1,0]
dy = [0,-1,0,1]


def can_visit(visited, curr, next):
	if next[0] not in range(0,graph.shape[0]) or next[1] not in range(0,graph.shape[1]):
		return False
	if visited[next]:
		return False
	if graph[next] > graph[curr]+1:
		return False

	return True


def bfs(graph, visited, start):
	q = queue()
	q.append(start)
	visited[start] = True
	dist = { start: 0 }

	while len(q) > 0:
		cell = q.popleft()
		x,y = cell
		if cell == end:
			return dist[cell]
		for i in range(4):
			next = (x+dx[i],y+dy[i])
			if can_visit(visited, cell, next):
				dist[next] = dist[cell]+1
				q.append(next)
				visited[next] = True


print(bfs(graph,visited,start))